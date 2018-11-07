#encoding=utf-8
from PIL import Image, ImageDraw
import sys
import sys
sys.path.append("..")
from lib.Draw import DrawClass


# def drawSharp(filepath,x,y,width,height):
# 	im = Image.open("D:\\work\\labelimg\\data\\data4\\000056.jpg")

# 	draw = ImageDraw.Draw(im)
# 	draw.line((0, 0) + im.size, fill=128)
# 	draw.line((0, im.size[1], im.size[0], 0), fill=128)
# 	del draw

# 	# write to stdout
# 	im.save("D:\\work\\labelimg\\data\\data4\\000056.png", "PNG")

if __name__ == '__main__':

	# drawSharp("12","12","12","12")

	dc=DrawClass("D:\\work\\labelimg\\data\\data4\\000005.jpg")

	for i in range(0,20):
		dc.drawSharp(20+i*10,20+i,100,200,"yoyoyo!")

	print (dc.getColor())