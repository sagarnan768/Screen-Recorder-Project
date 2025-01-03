import cv2
from PIL import ImageGrab
import numpy as np
from win32api import GetSystemMetrics
import time
import os

# Get screen width and height
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

# Create video directory if it doesn't exist
if not os.path.exists("video"):
    os.makedirs("video")

#------------file_name------------
file_name = f"video/video_{time.strftime('%d-%m-%y %H-%M-%S')}.mp4"

# Initialize video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use * to unpack the string
capture_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

while True:
    # Capture the screen image
    screen_img = ImageGrab.grab(bbox=(0, 0, width, height))
    
    # Convert the image to a NumPy array
    array_img = np.array(screen_img)
    
    # Color conversion (if needed for display)
    color_img=cv2.cvtColor(array_img,cv2.COLOR_BGR2RGB)
    
    # Write the frame to the video
    capture_video.write(array_img)  # Write the BGR image to the video
    
    # Display the image in a window
    cv2.imshow('Screen Recorder By Sagar', color_img)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Clean up resources
capture_video.release()  # Release the video writer
cv2.destroyAllWindows()   # Destroy all OpenCV windows
