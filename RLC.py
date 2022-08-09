import numpy
from PIL import Image
from typing import List, Tuple
import collection


# Open the image
pixels = numpy.asarray(Image.open('./img0-gray.jpg'),numpy.uint8)
pixels = pixels.reshape(-1)

# Extract binary format of image pixels
str_pixels = []
for i in pixels:
    str_pixels.append(str(bin(int(i)))[2:])

# Do padding on binary format of image pixels
for number , j in enumerate(str_pixels):
    if len(j) < 8:
        padded = ''.join(['0' for _ in range(8 - len(j))])
        str_pixels[number] = padded + str_pixels[number]


# Implementation RLC Coding     
Code_Str = ''.join(str_pixels)

cnt = 0
len_lst = []
tmp = Code_Str[0]

for number , k in enumerate(Code_Str):
    if k == tmp :
        cnt = cnt + 1
        tmp = k
    
    else:
        len_lst.append((tmp , cnt))
        tmp = k
        cnt = 1



# Decoding RLC Code
Decoded_Str = ''

for i in len_lst:
    Decoded_Str += ''.join([i[0] for j in range(i[1])])
Len_DeCoded_Str = len(Decoded_Str)

Elements = []
for j in range(0 , Len_DeCoded_Str , 8):
    Elements.append(int(Decoded_Str[j : j+8] , 2))

Elements = numpy.array(Elements)
Elements = Elements.astype(numpy.uint8)

tst = numpy.asarray(Image.open('./img0-gray.jpg') , numpy.uint8)
temp = numpy.shape(tst)

pixels = numpy.reshape(Elements , temp)
img = Image.fromarray(pixels)

img.save('result.jpg')