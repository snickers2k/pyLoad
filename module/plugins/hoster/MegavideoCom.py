#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from time import time
from module.plugins.Plugin import Plugin
from module.unescape import unescape

class MegavideoCom(Plugin):
    def __init__(self, parent):
        Plugin.__init__(self, parent)
        props = {}
        props['name'] = "MegavideoCom"
        props['type'] = "hoster"
        props['pattern'] = r"http://(www\.)?megavideo.com/\?v=.*"
        props['version'] = "0.1"
        props['description'] = """Megavideo.com Download Plugin"""
        props['author_name'] = ("jeix","mkaay")
        props['author_mail'] = ("jeix@hasnomail.de","mkaay@mkaay.de")
        self.props = props
        self.parent = parent
        self.html = None
        
    def download_html(self):
        url = self.parent.url
        self.html = self.req.load(url)

    def get_file_url(self):
        """ returns the absolute downloadable filepath
        """
        if self.html == None:
            self.download_html()

        # get id
        id = re.search("previewplayer/\\?v=(.*?)&width", self.html).group(1)
        
        # check for hd link and return if there
        if "flashvars.hd = \"1\";" in self.html:
            content = self.req.load("http://www.megavideo.com/xml/videolink.php?v=%s" % id)
            return unescape(re.search("hd_url=\"(.*?)\"", content).group(1))
            
        # else get normal link
        s = re.search("flashvars.s = \"(\\d+)\";", self.html).group(1)
        un = re.search("flashvars.un = \"(.*?)\";", self.html).group(1)
        k1 = re.search("flashvars.k1 = \"(\\d+)\";", self.html).group(1)
        k2 = re.search("flashvars.k2 = \"(\\d+)\";", self.html).group(1)
        return "http://www%s.megavideo.com/files/%s/" % (s, self.__decrypt(un, int(k1), int(k2)))
        
    def __decrypt(self, input, k1, k2):
        req1 = []
        req3 = 0
        for c in input:
            c = int(c, 16)
            tmp = "".join([str((c >> y) & 1) for y in range(4 -1, -1, -1)])
            req1.extend([int(x) for x in tmp])            
        
        req6 = []
        req3 = 0
        while req3 < 384:
            k1 = (k1 * 11 + 77213) % 81371
            k2 = (k2 * 17 + 92717) % 192811
            req6.append((k1 + k2) % 128)
            req3 += 1
            
        req3 = 256
        while req3 >= 0:
            req5 = req6[req3]
            req4 = req3 % 128
            req8 = req1[req5]
            req1[req5] = req1[req4]
            req1[req4] = req8
            req3 -= 1
            
        req3 = 0
        while req3 < 128:
            req1[req3] = req1[req3] ^ (req6[req3+256] & 1)
            req3 += 1
            
        out = ""
        req3 = 0
        while req3 < len(req1):
            tmp = req1[req3] * 8
            tmp += req1[req3+1] * 4
            tmp += req1[req3+2] * 2
            tmp += req1[req3+3]
            
            out += "%X" % tmp
            
            req3 += 4
            
        return out.lower()
    
    def get_file_name(self):
        if self.html == None:
            self.download_html()
            
        name = re.search("flashvars.title = \"(.*?)\";", self.html).group(1)
        name = "%s.flv" % unescape(name.encode("ascii", "ignore")).decode("utf-8").encode("ascii", "ignore").replace("+", " ")
        return name

    def file_exists(self):
        """ returns True or False
        """
        if self.html == None:
            self.download_html()
            
        if re.search(r"Dieses Video ist nicht verfügbar.", self.html) != None or \
           re.search(r"This video is unavailable.", self.html) != None:
            return False
        else:
            return True
            
