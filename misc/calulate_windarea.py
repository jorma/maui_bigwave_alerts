import os, sys
from PIL import Image
import pickle

im = Image.open("wave_area.jpg")
x = 0
y = 159

waveArea = []

for y in range(85, 245):
	
	for x in range(350, 550):
		pix = im.load()
		color = pix[x,y]

		if color == (0,0,0): #black
			coordinate = str(x) + "," + str(y)
			#print coordinate
			#print "********** black ***********"
			waveArea.append(coordinate)
		else:
			#print str(x) + "," + str(y)
			#print "white"
			pass
		
print waveArea


#output = open("waveArea.txt","w")
#pickle.dump(waveArea,output)
#output.close()
	
