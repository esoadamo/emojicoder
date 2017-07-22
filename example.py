#!/usr/bin/python3
# coding=utf-8
"""
THIS FILE WAS ENCODED BY EMOJICODER
https://github.com/esoadamo/emojicoder
"""
from base64 import b64decode as ee
c = "😚😖😵😰😛😷😉😴😈😇😑😩😛😖😔😍😂😠😴😊😜😇😉😩😛😧😐😨😈😤😡😥😛😆😱😯😋😢😈😩😃😐😩😰😜😦😥😮😝😂😠😢😐😶😽😵😛😧😑😩" \
    "😛😦😜😠😙😧😉😯😛😒😀😱😈😇😑😯😈😃😄😰😈😢😤😍😂😦😙😯😜😢😁😩😈😆😥😮😈😇😉😡😛😦😝😥😊😃😄😬😈😃😄😱😊😓😨😍😂😢😀😠" \
    "😈😂😁😰😜😦😥😮😝😂😡😩😊😐😴😊😈😂😀😠😈😇😑😩😛😖😔😮😜😶😱😥😙😗😀😨😌😒😤😍😂😧😁😲😚😖😹😴😊😂😝😃😛😶😽😬😋😂😁😩" \
    "😜😶😹😜😉😷😐😠😚😗😐😿😉😲😤😍😂😠🙀🙀"
e = list("😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬"
         "😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏")
b = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=")
exec(str(ee(''.join([b[e.index(ch)] for ch in list(c)])), 'utf8'))

