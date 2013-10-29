import os, sys
from PIL import Image
import subprocess

# black is 255, 255, 255
# white is 0, 0, 0



def bigSwellCheck():
	### create an array of coordinates for the aoi
	waveArea=[]

	for line in open( "waveArray_complete.txt", "r" ).readlines():
			line = line.replace('\n', '')
			waveArea.append(line)

	numOfPts = len(waveArea)

	#print str(numOfPts) + " coordinate points"

	numOfPts = numOfPts + 0.0
	#print waveArea

	color00 = "(0, 0, 204)" #darkest blue
	color01 = "(0, 102, 204)" #dark blue
	color02 = "(0, 153, 255)" #blue
	color03 = "(102, 204, 255)" #light blue
	color04 = "(102, 255, 255)" #lightest blue
	color05 = "(0, 255, 204)" #cyan
	color06 = "(0, 255, 153)" #aqua
	color07 = "(153, 255, 0)" #green
	color08 = "(204, 255, 0)" #light green
	color09 = "(255, 255, 51)" #yellow
	color10 = "(255, 204, 102)" #light orange
	color11 = "(255, 153, 102)" #orange
	color12 = "(255, 102, 0)" #dark orange
	color13 = "(255, 0, 0)" #red
	color14 = "(204, 0, 0)" #dark red
	color15 = "(255, 204, 255)" # light pink .... big swell starts here....
	color16 = "(255, 153, 255)" #pink
	color17 = "(255, 102, 255)" #light purple
	color18 = "(204, 0, 255)" #purple
	color19 = "(153, 0, 204)" #dark purple
	color20 = "(192, 192, 192)" #light grey
	color21 = "(153, 153, 153)" #grey
	color22 = "(102, 102, 102)" #dark grey
	color23 = "(51, 51, 51)" #black
	color24 = "(255, 255, 255)" #white *** Don't include this... direction bars will confuse results
	color25 = "(255, 255, 153)" #light yellow

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
	countColor25 = 0

	waveImage = Image.open("../images/hi_comp_1.png")
	rgb_waveImage = waveImage.convert('RGB')

	for x in range(0, int(numOfPts)):
	
		#take each coordinate in array and create x and y points
		coordinate = waveArea[x]

		coordinatePts = coordinate.split(",")

		x = int(coordinatePts[0])
		y = int(coordinatePts[1])

		color = rgb_waveImage.getpixel((x, y))
	
		#print "color: " + str(color) + " For coordinate: " + str(x) + "," + str(y) + "\n"
	
		#rgb_waveImage.putpixel((x, y), (205, 7, 185))
	
	
		if str(color) == color00:
			#print "darkest blue"
			countColor00 += 1
	
		elif str(color) == color01:
			#print "dark blue"
			countColor01 += 1
		
		elif str(color) == color02:
			#print "blue"		
			countColor02 += 1
		
		elif str(color) == color03:
			#print "light blue"
			countColor03 += 1
		
		elif str(color) == color04:
			#print "lightest blue"
			countColor04 += 1
		
		elif str(color) == color05:
			#print "cyan"
			countColor05 += 1
		
		elif str(color) == color06:
			#print "aqua"
			countColor06 += 1
		
		elif str(color) == color07:
			#print "green"
			countColor07 += 1
		
		elif str(color) == color08:
			#print "light green"
			countColor08 += 1
		
		elif str(color) == color09:
			#print "yellow"
			countColor09 += 1
		
		elif str(color) == color10:
			#print "light orange"
			countColor10 += 1
		
		elif str(color) == color11:
			#print "orange"
			countColor11 += 1
		
		elif str(color) == color12:
			#print "dark orange"
			countColor12 += 1
		
		elif str(color) == color13:
			#print "red"
			countColor13 += 1
		
		elif str(color) == color14:
			#print "dark red"
			countColor14 += 1
		
		elif str(color) == color15: # big swell starts here....
			#print "light pink"
			countColor15 += 1
		
		elif str(color) == color16: # big swell....
			#print "pink"
			countColor16 += 1
		
		elif str(color) == color17: # big swell....
			#print "light purple"
			countColor17 += 1
		
		elif str(color) == color18: # big swell....
			#print "purple"
			countColor18 += 1
				
		elif str(color) == color19: # big swell....
			#print "dark purple"
			countColor19 += 1

		elif str(color) == color20:
			#print "light grey"
			countColor20 += 1
					
		elif str(color) == color21:
			#print "grey"
			countColor21 += 1
		
		elif str(color) == color22:
			#print "dark grey"
			countColor22 += 1
		
		elif str(color) == color23:
			#print "black"
			countColor23 += 1
		
		elif str(color) == color24:
			#print "white *** Don't include this... direction bars will confuse results"
			countColor24 += 1
		
		elif str(color) == color25:
			#print "light yellow"
			countColor25 += 1
	
		else:
			pass


	totalBlueCount = float(countColor00 + countColor01 + countColor02 + countColor03 + countColor04)
	totalGreenYellowCount = float(countColor05 + countColor06 + countColor07 + countColor08 + countColor09)
	totalRedCount = float(countColor10 + countColor11 + countColor12 + countColor13 + countColor14)
 	totalPinkCount = float(countColor15 + countColor16 + countColor17 + countColor18 + countColor19)   
        
	#totalPinkCount = float(countColor03) #... use this for testing other colors

	percentBlue = 100 * (totalBlueCount / (numOfPts - countColor24))
	percentGreenYellow = 100 * (totalGreenYellowCount / (numOfPts - countColor24))
	percentRed = 100 * (totalRedCount / (numOfPts - countColor24))
	percentPink = 100 * (totalPinkCount / (numOfPts - countColor24)) # subtract white to remove white direction arrows from calculations.

	print str(percentBlue) + " percent blue "
	print str(percentGreenYellow) + " percent green-yellow "
	print str(percentRed) + " percent red "
	print str(percentPink) + " percent pink "
	
	return percentPink

bigSwellCheck()

#rgb_waveImage.save("/Users/jorma/Code/maui_bigwave_alerts/misc/foo_new.png")