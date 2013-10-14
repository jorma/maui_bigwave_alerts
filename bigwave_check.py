# This Python script was created by Jorma.com to send me an email alert if it looks like there is going to be big waves headed towards Hawaii. See the ReadMe for more info

import os, sys
from PIL import Image
import subprocess
import smtplib
import email.utils
from email.mime.text import MIMEText

totalPink = 0

def main():
	# Uncomment line below to download image files
	#subprocess.call(['./download.sh'])

	imageFile = Image.open("images/test.jpg")
	rgb_imageFile = imageFile.convert('RGB')

	waveCheck(rgb_imageFile)
		
	
def waveCheck():
	numOfPts = 16570.0 # this number is from the number of coordinate points in the waveArea list
	countPink = 0
	global totalPink
	waveArea=[]
	
	for line in open( "misc/test.txt", "r" ).readlines():
			line = line.replace('\n', '')
			waveArea.append(line)

	for x in range(0, 1659):

		coordinate = waveArea[x]	
		coordinatePts = coordinate.split(",")

		x = int(coordinatePts[0])
		y = int(coordinatePts[1])

		pix = imageName.load()

		color = pix[x,y]
		#print color
		print coordinate + " : " + str(color)
	
		if color == (255, 253, 75): # Pink
			countPink += 1
	
		elif color == (255, 153, 255): # Dark Pink
			countPink += 1
			
		else:
			pass	

	percentPink = round((countPink / numOfPts) * 100)

	print "Percent Pink: " + str(percentPink)
	
	if (percentPink >= 50):
		totalPink += 1
	else:
		pass

	
def SendEmail(name,emailAddr,emailBody):
	print "********Send Email*********"

if __name__ == '__main__':
	main()