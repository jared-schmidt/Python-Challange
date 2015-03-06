# http://www.pythonchallenge.com/pc/return/evil.html

### COULD NOT GET THIS CODE TO OPEN THE IMG CORRECTLY

# from PIL import Image

# evil = open('evil2.gfx', 'rb+').read()
# im1 = open('im1.jpg', 'wb')
# im2 = open('im2.jpg', 'wb')
# im3 = open('im3.jpg', 'wb')
# im4 = open('im4.jpg', 'wb')
# im5 = open('im5.jpg', 'wb')

# for b in range(0, len(evil), 5):
#     im1.write(bytes(evil[b], 'utf-8'))
#     # im2.write(evil[b+1])
#     # im3.write(evil[b+2])
#     # im4.write(evil[b+3])
#     # im5.write(evil[b+4])

# im1.close()
# im2.close()
# im3.close()
# im4.close()
# im5.close()

# COPIED THIS CODE FROM INTERNET
# IMAGE3 STILL DOES'T OPEN?
f = open('evil2.gfx','rb').read()

for i in range(0,5):
    open("image"+str(i)+".jpg", "wb").write(f[i::5])


# The images read "dis" "pro" "port" "ional" "ity", where the "ity" is crossed out. Changing the page on the url to disproportional