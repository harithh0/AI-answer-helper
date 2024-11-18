from goprocam import GoProCamera
import time

# Connect to GoPro via Wi-Fi
gopro = GoProCamera.GoPro()

def take_photo():
	gopro.take_photo(timer=5)
	gopro.downloadLastMedia(custom_filename="selfie.jpg")
	gopro.shoot_video(10)
	gopro.downloadLastMedia(custom_filename="selfie.mp4")



take_photo()
