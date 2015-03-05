def trans(s):
    n = ''
    for l in s:
        num = ord(l)
        if num >= 97 and num <= 123:
            if (l == 'y'):
                num = 97 - 2
            if (l == 'z'):
                num = 97-1

            l = chr(num + 2)
        n += l

    return n

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(trans(s))

s = "http://www.pythonchallenge.com/pc/def/map.html"
print(trans('map'))
