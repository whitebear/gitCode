#!/usr/bin/env python
#encoding=utf-8
import Image,ImageEnhance,ImageFilter
import sys
image_name = "./sample.jpg"
im = Image.open(image_name)
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.show()
			  #all by pixel
s = 0          #start postion of first number
w = 9          #width of each number
h = 13          #end postion from top
t = 0           #start postion of top
num = 10

im_new = []
#split four numbers in the picture
for i in range(num):
  im1 = im.crop((s+w*i, t, s+w*(i+1), h))
  im_new.append(im1)
  
f = file("Data.py","w")
f.write("N=[")
for k in range(num):
  l = []
  #im_new[k].show()
  for i in range(h):
	  for j in range(w):
		  if (im_new[k].getpixel((j,i)) == 255):
			  l.append(0)
		  else:
			  l.append(1)

			  
  f.write("[")
  n = 0
  for i in l:
	  if (n%w==0):
		  f.write("\n")
	  f.write(str(i)+",")
	  n+=1
  if(k != num-1):  
    f.write("],\n")
  else:
    f.write("]\n")
    
f.write("]")
f.flush()

print("export done!")
exit()
