# Download zip: http://www.pythonchallenge.com/pc/def/channel.zip

import os
import zipfile

nothing = '90052'

zf = zipfile.ZipFile(open('channel.zip', 'r'))

comments = ''

while True:
    try:
        num = ''
        fi = nothing + '.txt'
        txt = zf.read(fi)
        
        read_data = txt[txt.find("nothing is"):]
        
        for n in str(read_data):
            if n.isdigit():
                num += str(n)
        
        comment = zf.getinfo(fi).comment
        comments += comment

        nothing = num
    except:
        break;

print( comments )
