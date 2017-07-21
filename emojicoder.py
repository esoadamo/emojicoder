#!/usr/bin/python3
# coding=utf-8
"""
 _____ __  __  ___      _ ___ ____ ___  ____  _____ ____
| ____|  \/  |/ _ \    | |_ _/ ___/ _ \|  _ \| ____|  _ \
|  _| | |\/| | | | |_  | || | |  | | | | | | |  _| | |_) |
| |___| |  | | |_| | |_| || | |__| |_| | |_| | |___|  _ <
|_____|_|  |_|\___/ \___/|___\____\___/|____/|_____|_| \_\
😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿🙀🙁🙂🙃
🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏
 ___   ____  _____ ____ ____  _____ _____
|_ _| |  _ \| ____/ ___|  _ \| ____|_   _|
 | |  | |_) |  _|| |  _| |_) |  _|   | |
 | |  |  _ <| |__| |_| |  _ <| |___  | |
|___| |_| \_\_____\____|_| \_\_____| |_|

 _   _  ___ _____ _   _ ___ _   _  ____
| \ | |/ _ \_   _| | | |_ _| \ | |/ ___|
|  \| | | | || | | |_| || ||  \| | |  _
| |\  | |_| || | |  _  || || |\  | |_| |
|_| \_|\___/ |_| |_| |_|___|_| \_|\____|
😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿🙀🙁🙂🙃
🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏
https://github.com/esoadamo/emojicoder
"""
import base64

EMOJIS = list("😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬"
              "😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏")
BASE64CHARS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=")


def encode(string: str) -> str:
    """
    Encodes string into EMOJIS!
    :param string: string supposed to be encoded into EMOJIS
    :return: EMOJIS!
    """
    return ''.join([EMOJIS[BASE64CHARS.index(ch)] for ch in list(str(base64.b64encode(bytes(string, 'utf8')), 'utf8'))])


def decode(string: str) -> str:
    """
    Decodes EMOJIS back into utf-8 string
    :param string: EMOJIS!
    :return: original utf-8 string
    """
    return str(base64.b64decode(''.join([BASE64CHARS[EMOJIS.index(ch)] for ch in list(string)])), 'utf8')


if __name__ == '__main__':
    from os.path import isfile
    from sys import argv
    from shutil import copyfile
    from codecs import open

    if len(argv) < 2 or argv[1] == '-h' or argv[1] == '--help' or argv[1] == '/?':
        print('Usage: emojicoder [--backup] [--no-decoder] file')
        print('file: path to the file that is supposed to be encoded')
        print('--backup: if not omitted then backup of the input file is crated')
        print('--no-decoder: will not add any plain text decoding function into the file')
        exit(0)

    input_file = argv[3 if '--backup' in argv and '--no-decoder' in argv else 2 if '--backup' in argv or '--no-decoder'
                                                                                                         in argv else 1]
    if not isfile(input_file):
        print('"%s" is not file! Traitor!' % input_file)
        exit(1)
    if '--backup' in argv:
        backup_file = input_file + '.bck'
        print('Creating backup to "%s"' % backup_file)
        copyfile(input_file, backup_file)
    with open(input_file, 'r+', 'utf8') as f:
        code = encode(f.read())
        f.seek(0)
        if '--no-decoder' not in argv:
            code = decode(
                "😈😲😄😯😝😗😍😲😋😶😉😩😛😢😽😰😞😗😑😨😛😶😸😳😃😐😨😣😈😆😍😯😙😆😥😮😙😳😵😵😝😆😘😭😎😀😴😊😈😢😈😢😃😐😩😔"
                "😒😄😥😓😈😄😙😉😓😄😔😠😕😴😅😓😈😄😕😎😐😴😽😄😑😔😐😠😐😥😤😠😑😔😵😏😒😤😥😃😓😴😑😅😔😠😴😊😚😇😑😴😜😇😌😺"
                "😋😲😽😧😚😗😑😨😝😖😈😮😘😶😽😭😋😶😕😳😛😶😅😤😘😖😵😯😋😶😕😭😛😶😩😩😘😶😽😤😙😗😈😍😂😠😴😊😎😣😩😃😓😴😑😅"
                "😎😣😨😍😂😢😕😳😃😐😨😢😈😢😈😍😂😦😙😲😛😶😴😠😘😦😅😳😙😓😘😴😈😆😥😭😜😆😽😲😝😂😁😢😍😣😑😤😙😖😍😯😙😆😔😠"
                "😘😗😌😠😙😖😔😍😂😦😙😲😛😶😴😠😘😶😽😤😙😖😍😳😈😆😥😭😜😆😽😲😝😂😁😯😜😆😕😮😈😆😅😳😈😆😼😍😂😦😔😠😏😒😁😬"
                "😚😗😍😴😊😂😋😰😧😹😢😀😼😉😾😘😠😟😂😟😦😈😋😰😧😹😢😃😼😉😾😘😡😏😂😟😦😈😗😰😧😹😢😆😼😉😾😘😡😿😂😟😦😈😣😰"
                "😧😹😢😉😼😉😾😘😢😯😂😟😦😈😯😰😧😹😢😌😼😉😾😘😣😟😂😟😦😈😻😰😧😹😢😏😼😉😾😘😤😏😂😟😦😉😇😰😧😹😢😒😼😉😾😘"
                "😤😿😂😟😦😉😓😰😧😹😢😕😼😉😾😘😥😯😂😟😦😉😟😰😧😹😢😘😼😉😾😘😦😟😂😟😦😉😫😰😧😹😢😛😼😉😾😘😧😏😂😟😦😉😷😰"
                "😧😹😢😞😼😉😾😘😧😿😂😟😦😊😃😰😧😹😢😡😼😉😾😘😨😯😂😟😦😊😏😰😧😹😢😤😼😉😾😘😩😟😂😟😦😊😛😰😧😹😢😧😼😉😾😘"
                "😪😏😂😟😦😊😧😰😧😹😢😪😼😉😾😘😪😿😂😟😦😊😰😢😃😐😨😠😈😂😀😠😈😂😀😠😈😂😀😢😼😉😾😘😫😟😂😟😦😊😻😰😧😹😢😯"
                "😼😉😾😘😬😏😂😟😦😋😇😰😧😹😢😲😼😉😾😘😬😿😂😟😦😋😓😰😧😹😢😵😼😉😾😘😭😯😂😟😦😋😟😰😧😹😢😸😼😉😾😘😮😟😂😟"
                "😦😋😫😰😧😹😢😻😼😉😾😘😯😏😂😟😦😋😷😰😧😹😢😾😼😉😾😘😯😿😂😟😦😘😃😰😧😹😦😁😼😉😾😙😠😯😂😟😦😘😏😰😧😹😦😄"
                "😼😉😾😙😡😟😂😟😦😘😛😰😧😹😦😇😼😉😾😙😢😏😂😟😦😘😧😰😧😹😦😊😼😉😾😙😢😿😂😟😦😘😳😰😧😹😦😍😼😉😾😙😣😯😂😟"
                "😦😘😼😢😊😐😴😊😘😢😀😽😈😆😱😩😜😷😐😨😈😤😅😂😐😴😑😅😑😤😝😈😒😔😩😋😓😄😵😎😓😵😁😑😔😥😍😔😕😕😙😗😖😅😥😚"
                "😘😖😉😣😙😆😕😦😙😶😡😩😚😦😭😬😛😖😹😯😜😇😅😲😜😷😑😵😝😧😝😸😞😗😨😰😌😓😈😳😍😃😔😶😍😳😠😹😊😲😼😽😈😢😤😍"
                "😂😧😝😩😝😆😠😠😛😲😡😟😗😶😙😩😛😆😕😟😗😲😰😠😉😷😈😧😋😂😀😧😝😗😑😦😎😂😜😩😈😆😅😳😈😆😘😺😃😐😨😠😈😂😀😠"
                "😘😲😀😽😈😄😙😡😛😇😍😥😃😐😨😠😈😂😀😠😙😦😽😲😈😆😰😠😚😖😸😠😙😢😹😲😙😖😅😤😊😂😤😮😜😷😁😬😚😗😑😬😚😖😹😥"
                "😜😲😠😩😎😠😴😊😈😂😀😠😈😂😀😠😈😂😁😩😙😢😁😣😎😠😴😊😈😂😀😠😈😂😀😠😈😂😀😠😈😂😀😠😙😗😡😥😘😲😡😳😝😇😈😨"
                "😙😖😔😨😉😲😜😮😚😦😽😩😛😢😡😛😘😥😭😥😋😦😥😮😙😆😕😸😊😆😍😨😊😕😴😠😙😦😽😲😈😆😍😨😈😆😥😮😈😆😱😩😜😷😐😨"
                "😛😂😥😝😊😒😤😬😈😂😝😵😝😆😘😸😉😲😤😩😃😐😨😠😈😂😀😠😈😂😀😠😈😂😀😠😈😂😁😢😜😦😕😡😚😰😴😊😈😂😀😠😈😂😀😠"
                "😈😂😁😥😛😆😥😦😈😆😰😮😜😷😑😡😜😧😑😳😝😶😥😴😚😂😠😧😎😣😩😃😓😴😑😅😎😣😨😧😊😓😨😍😂😢😀😠😈😂😀😠😈😂😀😠"
                "😈😂😀😠😈😆😌😠😏😒😁😔😜😧😕😥😃😐😨🙀"
            ) % code
        else:
            print('Oh, I see. You do not want a decoder. You')
            print(decode("😈😂😀😠😈😂😀😠😈😂😀😠😈😂😀😠😈😂😀😠😈😂😀😠😈😂😀😠😈😂😁😟😃😐😨😠😗😲😁😟😗😲😁😟😗😵😼😠😈😂😁😟😗😲"
                         "😁😟😈😅😼😠😗😵😼😠😊😅😼😩😈😅😽😟😈😅😼😠😈😅😽😟😗😰😴😊😟😂😀😧😗😲😁😠😈😅😼😠😗😂😀😯😈😅😽😠😈😇😰😠"
                         "😉😵😼😠😗😇😰😠😟😂😼😠😗😶😀😠😟😂😼😠😗😵😽😼😃😐😩😼😈😇😰😠😟😂😁😼😈😇😰😠😟😂😀😨😗😷😰😠😟😂😁😼😈😇"
                         "😰😠😟😂😁😼😈😂😡😟😟😂😁😼😈😂😡😟😗😰😴😊😟😅😽😼😈😇😱😟😟😂😁😼😗😷😱😜😗😵😼😬😗😷😱😟😟😂😁😼😗😷😱😟"
                         "😟😅😱😟😗😲😱😟😟😅😱😟😗😵😽😼😃😐😨🙀"))
        f.write(code)
        f.truncate()
    print('Done')
