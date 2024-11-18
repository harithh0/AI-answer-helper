from goprocam import GoProCamera
import time
import easyocr

# Connect to GoPro via Wi-Fi
gopro = GoProCamera.GoPro()

def take_photo():
	gopro.take_photo(timer=1)
	gopro.downloadLastMedia(custom_filename="selfie.jpg")
	# gopro.shoot_video(10)
	# gopro.downloadLastMedia(custom_filename="selfie.mp4")



take_photo()


reader = easyocr.Reader(['en'])

# Path to your image file
image_path = './selfie.jpg'

# Use EasyOCR to extract text from the image
results = reader.readtext(image_path)

# Loop through the results and print the extracted text
for result in results:
    print(result[1])  # result[1] contains the detected text
