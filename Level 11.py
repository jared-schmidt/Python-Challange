# http://www.pythonchallenge.com/pc/return/5808.html

# img -> http://www.pythonchallenge.com/pc/return/cave.jpg

from PIL import Image

im = Image.open('cave.jpg')
size = im.size

first_layer_colors = []
first_layer_coords = []

for y in range(im.size[1]):
    for x in range(im.size[0]):
        cood = (x, y)
        p = im.getpixel(cood)
        if p[2] == 0:
            first_layer_colors.append(p)
            first_layer_coords.append(cood)


img = Image.new('RGB', size)
for i, p in enumerate(first_layer_coords):
    img.putpixel(p, first_layer_colors[i])

img.save("first_layer.png")
