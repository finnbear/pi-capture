import os
import picamera
from SimpleCV import *

image_path = 'image.png'

camera = picamera.PiCamera()

#camera.resolution = (3280, 2464)
camera.sharpness = 0
camera.contrast = 0
camera.brightness = 50
camera.saturation = 0
camera.ISO = 0
camera.video_stabilization = False
camera.exposure_compensation = 0
camera.exposure_mode = 'auto'
camera.meter_mode = 'average'
camera.awb_mode = 'auto'
camera.image_effect = 'none'
camera.color_effects = None
#camera.rotation = 90
camera.hflip = False
camera.vflip = False
camera.zoom = (0.2,0,1,1)

def main():
	while disk() < 90:
		# Capture an image
		camera.capture(image_path, format='png')

		# Process the image
		image = Image(image_path)
		image = image.rotate(-90)
		image.save(image_path)
	camera.close()

def disk():
	p = os.popen("df -h /")
	i = 0
	while 1:
		i = i + 1
		line = p.readline()
		if i==2:
			return int(line.split()[1:5][3][:-1])

print disk()

