import os
import time
from picamera2 import Picamera2
from libcamera import controls

# Set up the camera
picam2 = Picamera2()
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})  # Auto-focus mode
picam2.start()
time.sleep(1)

# Define the number of images and save path
num_images = 20  # Change this as needed
raspi_save_path = "/home/tuftsrobot/imagesMLTM"  # Folder on Raspberry Pi

# Ensure the folder exists
os.makedirs(raspi_save_path, exist_ok=True)

for i in range(1, num_images + 1):
    img_name = f"image_{i}.jpg"
    img_path = os.path.join(raspi_save_path, img_name)
    time.sleep(1)
    # Capture image
    picam2.capture_file(img_path)
    print(f"Captured {img_path}")
    
    # Wait 1 second before capturing the next image
    time.sleep(1)

picam2.stop()
