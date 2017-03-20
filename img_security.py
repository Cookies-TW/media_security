import base64

"""img = open("elaine_g_512x512.bmp",'rb')
line = img.readline()
while line:
    print(line)
    line = img.readline()
img.close()"""

with open("watermark.bmp",'rb') as imageFile:
    img = base64.b64encode(imageFile.read())
    print(img)
