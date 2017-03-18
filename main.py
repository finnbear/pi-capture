import os
import time
import picamera
from SimpleCV import *

motion_threshold = 2.0
image_path = 'image.png'
gallery_path = './gallery'

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
	if not os.path.exists(gallery_path):
		os.makedirs(gallery_path)

	prev_image = None

	while disk() < 90:
		# Capture an image
		camera.capture(image_path, format='png')

		# Process the image
		image = Image(image_path)
		image = image.rotate(-90)

		# Detect motion
		if not prev_image == None:
			motion_image, motion_amount = detectMotion(image, prev_image)

			if motion_amount > motion_threshold:
				image.save(image_path)

		# Swap image into prev_image
		prev_image = image
	camera.close()

def disk():
	p = os.popen("df -h /")
	i = 0
	while 1:
		i = i + 1
		line = p.readline()
		if i==2:
			return int(line.split()[1:5][3][:-1])

def detectMotion(motion_image_1, motion_image_2):
	motion_image_1 = motion_image_1.toGray()
	motion_image_2 = motion_image_2.toGray()
	motion_image_diff = motion_image_1 - motion_image_2
	motion_image_diff = motion_image_diff.binarize(25)
	motion_image_diff = motion_image_diff.invert()
	motion_matrix_diff = motion_image_diff.getNumpy()
	motion_average = motion_matrix_diff.mean()

	return motion_image_diff, motion_average

main()
