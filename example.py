#!/usr/bin/python3
# coding=utf-8
"""
THIS FILE WAS ENCODED BY EMOJICODER
https://github.com/esoadamo/emojicoder

::CODE::
😜😇😉😩😛😧😐😨😉😶😡😥😛😆😱😯😈😇😝😯😜😦😱😤😉😲😤🙀
"""
from base64 import b64decode as ee
from codecs import open as o
e = list("😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬"
         "😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏")
b = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=")
with o(__file__, 'r', 'utf8') as f:
    c = False
    for l in f.read().splitlines():
        if c:
            exec(str(ee(''.join([b[e.index(ch)] for ch in list(l)])), 'utf8'))
            break
        elif l.startswith('::CODE::'):
            c = True
# prints "hello world"
