import os, sys
from PIL import Image
import subprocess

# black is 255, 255, 255
# white is 0, 0, 0

### This first part just gets an array or coordinates of the aoi

waveArea=[]
for line in open( "waveArray_complete.txt", "r" ).readlines():
		line = line.replace('\n', '')
		waveArea.append(line)

numOfPts = len(waveArea)
#print numOfPts

numOfPts = numOfPts + 0.0
#print waveArea

countColor00 = 0
countColor01 = 0
countColor02 = 0
countColor03 = 0
countColor04 = 0
countColor05 = 0
countColor06 = 0
countColor07 = 0
countColor08 = 0
countColor09 = 0
countColor10 = 0
countColor11 = 0
countColor12 = 0
countColor13 = 0
countColor14 = 0
countColor15 = 0
countColor16 = 0
countColor17 = 0
countColor18 = 0
countColor19 = 0
countColor20 = 0
countColor21 = 0
countColor22 = 0
countColor23 = 0
countColor24 = 0

color00 = "0, 0, 204"
color01 = "0, 102, 204"
color02 = "0, 153, 255"
color03 = "102, 204, 255"
color04 = "102, 255, 255"
color05 = "0, 255, 204"
color06 = "0, 255, 153"
color07 = "153, 255, 0"
color08 = "204, 255, 0"
color09 = "255, 255, 51"
color10 = "255, 204, 102"
color11 = "255, 153, 102"
color12 = "255, 102, 0"
color13 = "255, 0, 0"
color14 = "204, 0, 0"
color15 = "255, 204, 255" # pink
color16 = "255, 153, 255"
color17 = "255, 102, 255"
color18 = "204, 0, 255"
color19 = "153, 0, 204"
color20 = "192, 192, 192"
color21 = "153, 153, 153"
color22 = "102, 102, 102"
color23 = "51, 51, 51"
color24 = "255, 255, 255"
color24 = "255, 255, 153"







waveImage = Image.open("../images/hi_comp_1.png")
rgb_waveImage = waveImage.convert('RGB')


#for x in range(0, 16580):
for x in range(300, 500):
	
	#take each coordinate in array and create x and y points
	coordinate = waveArea[x]

	coordinatePts = coordinate.split(",")

	x = int(coordinatePts[0])
	y = int(coordinatePts[1])

	color = rgb_waveImage.getpixel((x, y))
	
	print "color: " + str(color) + " For coordinate: " + str(x) + "," + str(y) + "\n"
	
	#rgb_waveImage.putpixel((x, y), (205, 7, 185))
	
	
	if color == color00: #dark blue
		print "darkblue"
		countColor00 += 1
	
	elif color == (63, 63, 255): # blue
		print "blue"
		countBlue += 1
			
	else:
		#print "not blue"
		#print color
		pass



rgb_waveImage.save("/Users/jorma/Code/maui_bigwave_alerts/misc/foo_new.png")