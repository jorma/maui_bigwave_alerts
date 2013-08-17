import os, sys
from PIL import Image

im = Image.open("../images/test3.png")

rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((200, 400))

print r, g, b
