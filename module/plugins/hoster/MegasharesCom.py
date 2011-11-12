# -*- coding: utf-8 -*-
"""
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License,
    or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, see <http://www.gnu.org/licenses/>.

    @author: zoidberg
"""

import re
from time import time
from module.plugins.internal.SimpleHoster import SimpleHoster, parseFileInfo
from module.network.RequestFactory import getURL

def getInfo(urls):
    result = []

    for url in urls:
        file_info = parseFileInfo(MegasharesCom, url, getURL(url, decode=True)) 
        result.append(file_info)
            
    yield result

class MegasharesCom(SimpleHoster):
    __name__ = "MegasharesCom"
    __type__ = "hoster"
    __pattern__ = r"http://(\w+\.)?megashares.com/.*"
    __version__ = "0.12"
    __description__ = """megashares.com plugin - free only"""
    __author_name__ = ("zoidberg")
    __author_mail__ = ("zoidberg@mujmail.cz")

    FILE_NAME_PATTERN = '<h1 class="black xxl"[^>]*title="([^"]+)">'
    FILE_SIZE_PATTERN = '<strong><span class="black">Filesize:</span></strong> ([0-9.]+) (KB|MB|GB)<br />'
    DOWNLOAD_URL_PATTERN = '<div id="show_download_button_2" style="display:none">\s*<a href="([^"]+)">'
    PASSPORT_LEFT_PATTERN = 'Your Download Passport is: <[^>]*>(\w+).*\s*You have\s*<[^>]*>\s*([0-9.]+) ([kKMG]i?B)'
    PASSPORT_RENEW_PATTERN = 'Your download passport will renew in\s*<strong>(\d+)</strong>:<strong>(\d+)</strong>:<strong>(\d+)</strong>'
    REACTIVATE_NUM_PATTERN = r'<input[^>]*id="random_num" value="(\d+)" />'
    REACTIVATE_PASSPORT_PATTERN = r'<input[^>]*id="passport_num" value="(\w+)" />'
    REQUEST_URI_PATTERN = r'var request_uri = "([^"]+)";'
    NO_SLOTS_PATTERN = r'<dd class="red">All download slots for this link are currently filled'
    FILE_OFFLINE_PATTERN = r'<dd class="red">(Invalid Link Request|Link has been deleted)'

    def process(self, pyfile):
        self.html = self.load(pyfile.url, decode=True)
        if self.NO_SLOTS_PATTERN in self.html:
            self.retry(wait_time = 300)
        self.getFileInfo()
        self.handleFree()

    def handleFree(self):
        if self.pyfile.size > 576716800: self.fail("This file is too large for free download")

        # Reactivate passport if needed
        found = re.search(self.REACTIVATE_PASSPORT_PATTERN, self.html)
        if found:
            passport_num = found.group(1)
            request_uri = re.search(self.REQUEST_URI_PATTERN, self.html).group(1)

            for i in range(5):
                random_num = re.search(self.REACTIVATE_NUM_PATTERN, self.html).group(1)

                verifyinput = self.decryptCaptcha("http://megashares.com/index.php?secgfx=gfx&random_num=%s" % random_num)
                self.logInfo("Reactivating passport %s: %s %s" % (passport_num, random_num, verifyinput))

                url = "http://d01.megashares.com%s&rs=check_passport_renewal" % request_uri + \
                    "&rsargs[]=%s&rsargs[]=%s&rsargs[]=%s" % (verifyinput, random_num, passport_num) + \
                    "&rsargs[]=replace_sec_pprenewal&rsrnd=%s" % str(int(time()*1000))
                self.logDebug(url)
                response = self.load(url)

                if 'Thank you for reactivating your passport.' in response:
                    self.correctCaptcha()
                    self.retry(0)
                else:
                    self.invalidCaptcha()
            else: self.fail("Failed to reactivate passport")

        # Check traffic left on passport
        found = re.search(self.PASSPORT_LEFT_PATTERN, self.html)
        if not found: self.fail('Passport not found')
        self.logInfo("Download passport: %s" % found.group(1))
        data_left = float(found.group(2)) * 1024 ** {'KB': 1, 'MB': 2, 'GB': 3}[found.group(3)]
        self.logInfo("Data left: %s %s (%d MB needed)" % (found.group(2), found.group(3), self.pyfile.size / 1048576))
        if self.pyfile.size > data_left:
            found = re.search(self.PASSPORT_RENEW_PATTERN, self.html)
            if not found: self.fail('Passport renew time not found')
            renew = found.group(1) + 60 * (found.group(2) + 60 * found.group(3))
            self.retry(renew, 3, "Unable to get passport")

        # Find download link
        found = re.search(self.DOWNLOAD_URL_PATTERN, self.html)
        if not found: self.fail('Download link not found')
        download_url = found.group(1)

        # Download
        self.logDebug("Download URL: %s" % download_url)
        self.download(download_url)