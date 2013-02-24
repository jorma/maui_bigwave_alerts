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

	images = ["images/hi_comp_1.png"]
	
	for x in range(0, 1):
		im = Image.open(images[x])
		waveCheck(im)
	
	print "Total Pink: " + str(totalPink)
	
	if totalPink >= 5:
		SendEmail("Jorma","aloha@jorma.com","Looks like Big Swell is on the way!")
	else:
		pass
		
	
def waveCheck(imageName):
	numOfPts = 16570.0 # this number is from the number of coordinate points in the waveArea list
	countPink = 0
	global totalPink
	waveArea=[]
	
	for line in open( "misc/test.txt", "r" ).readlines():
			line = line.replace('\n', '')
			waveArea.append(line)

	for x in range(0, 200):

		coordinate = waveArea[x]	
		coordinatePts = coordinate.split(",")

		x = int(coordinatePts[0])
		y = int(coordinatePts[1])

		pix = imageName.load()

		color = pix[x,y]
		#print color
		print coordinate + " : " + str(color)
	
		if color == (102,255,255): # Pink
			countPink += 1
	
		elif color == (255, 153, 255): # Dark Pink
			countPink += 1
			
		else:
			pass	

	percentPink = round((countPink / numOfPts) * 100)

	#print "Percent Pink: " + str(percentPink)
	
	if (percentPink >= 50):
		totalPink += 1
	else:
		pass

	
def SendEmail(name,emailAddr,emailBody):
	print "********Send Email*********"
	msg = MIMEText('Aloha -\n\n ' + emailBody) 
	msg['To'] = email.utils.formataddr((name, emailAddr))
	msg['From'] = email.utils.formataddr(('Jorma', 'jorma@minustide.net'))
	msg['Subject'] = 'Email Alert: Calm day in Lahaina'

	conn = smtplib.SMTP('mail.minustide.net')
	conn.login('jorma@minustide.net', 'xxxxxxxx')
	conn.sendmail(msg['From'], msg['To'], msg.as_string())
	conn.quit()

if __name__ == '__main__':
	main()