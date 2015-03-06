# http://www.pythonchallenge.com/pc/def/oxygen.html
from PIL import Image
import ast

# http://www.pythonchallenge.com/pc/def/oxygen.png
im = Image.open('oxygen.png')
rgb = im.convert('RGB')

shades = []

for x in range(0, im.size[0], 7):
    r, g, b = rgb.getpixel((x, 50))
    shades.append(r)

s = ''

for x in shades:
    s += chr(x)

print(s)

s = s[s.find('the next level is'):]
lvl = ast.literal_eval(s[s.find('['):s.find(']') + 1])

s = ''
for x in lvl:
    s += chr(x)

print(s)
