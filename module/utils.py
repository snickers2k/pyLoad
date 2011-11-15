# -*- coding: utf-8 -*-

""" Store all usefull functions here """

import os
import sys
import time
import re
from os.path import join
from string import maketrans
from htmlentitydefs import name2codepoint

def chmod(*args):
    try:
        os.chmod(*args)
    except:
        pass


def decode(string):
    """ decode string with utf if possible """
    try:
        return string.decode("utf8", "replace")
    except:
        return string


def removeChars(string, repl):
    """ removes all chars in repl from string"""
    if type(string) == str:
        return string.translate(maketrans("", ""), repl)
    elif type(string) == unicode:
        return string.translate(dict([(ord(s), None) for s in repl]))

def save_path(name):
    #remove some chars
    if os.name == 'nt':
        return removeChars(name, '/\\?%*:|"<>')
    else:
        return removeChars(name, '/\\"')

def save_join(*args):
    """ joins a path, encoding aware """
    paths = []
    for i, path in enumerate(args):
        # remove : for win comp, but not for first segment
        if i:
            path = path.replace(":", "")

        path = decode(path)

        tmp = fs_encode(path)
        paths.append(tmp)
    return join(*paths)

def fs_encode(string):
    """ Encodes with filesystem encoding
    
    :param string: string to decode
    :return:
    """
    try:
       return string.encode(sys.getfilesystemencoding(), "replace")
    except:
        return string

def fs_decode(string):
    """ Decodes with filesystem encoding

    :param string: string to decode
    :return:
    """
    try:
       return string.decode(sys.getfilesystemencoding(), "replace")
    except:
        return string

def compare_time(start, end):
    start = map(int, start)
    end = map(int, end)

    if start == end: return True

    now = list(time.localtime()[3:5])
    if start < now and end > now: return True
    elif start > end and (now > start or now < end): return True
    elif start < now and end < now and start > end: return True
    else: return False


def formatSize(size):
    """formats size of bytes"""
    size = int(size)
    steps = 0
    sizes = ["B", "KiB", "MiB", "GiB", "TiB"]
    while size > 1000:
        size /= 1024.0
        steps += 1
    return "%.2f %s" % (size, sizes[steps])


def formatSpeed(speed):
    return formatSize(speed) + "/s"


def freeSpace(folder):
    if os.name == "nt":
        import ctypes

        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value
    else:
        from os import statvfs

        s = statvfs(folder)
        return s.f_bsize * s.f_bavail


def uniqify(seq, idfun=None):
# order preserving
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        # in old Python versions:
        # if seen.has_key(marker)
        # but in new ones:
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result


def parseFileSize(string): #returns bytes
    m = re.match(r"(\d*[\.,]?\d+)(.*)", string.strip().lower())
    if m:
        traffic = float(m.group(1).replace(",", "."))
        unit = m.group(2).strip()
        if unit in ("gb", "gig", "gbyte", "gigabyte", "gib"):
            traffic *= 1 << 30
        elif unit in ("mb", "mbyte", "megabyte", "mib"):
            traffic *= 1 << 20
        elif unit in ("kb", "kib", "kilobyte", "kbyte"):
            traffic *= 1 << 10
        return traffic

    return 0


def lock(func):
    def new(*args):
        #print "Handler: %s args: %s" % (func,args[1:])
        args[0].lock.acquire()
        try:
            return func(*args)
        finally:
            args[0].lock.release()

    return new


def fixup(m):
    text = m.group(0)
    if text[:2] == "&#":
        # character reference
        try:
            if text[:3] == "&#x":
                return unichr(int(text[3:-1], 16))
            else:
                return unichr(int(text[2:-1]))
        except ValueError:
            pass
    else:
        # named entity
        try:
            name = text[1:-1]
            text = unichr(name2codepoint[name])
        except KeyError:
            pass
        
    return text # leave as is

def html_unescape(text):
    """Removes HTML or XML character references and entities from a text string"""
    return re.sub("&#?\w+;", fixup, text)

if __name__ == "__main__":
    print freeSpace(".")

    print removeChars("ab'cdgdsf''ds'", "'ghd")
