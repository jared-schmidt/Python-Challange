# http://www.pythonchallenge.com/pc/return/disproportional.html
import requests

# req = requests.get('http://www.pythonchallenge.com/pc/phonebook.php')

# print(req.content)

from PIL import Image

# FROM level 12
# http://www.pythonchallenge.com/pc/return/evil4.jpg
# im = open('evil4.jpg')
# print(im.read()) # Bert is evil! go back! # http://www.pythonchallenge.com/pc/return/bert.html
# im.close()
# http://www.pythonchallenge.com/pc/return/remote.html
# the phone is remote

im = Image.open('bert.gif')
im = im.convert('RGB')
for y in range(im.size[1]):
    for x in range(im.size[0]):
        cood = (x, y)
        p = im.getpixel(cood)
        print(p)
# print(im.tobytes())


# phone that <remote /> evil