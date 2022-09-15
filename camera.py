from picamera import PiCamera
from picarx import Picarx
px = Picarx()
import io
import time
import cv2
import numpy as np

def captureQRCode():
    stream = io.BytesIO()
    with PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        camera.capture(stream, format='jpeg')
    # Construct a numpy array from the stream
    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    # "Decode" the image from the array, preserving colour
    image = cv2.imdecode(data, 1)

    decoder = cv2.QRCodeDetector()
    data, points, _ = decoder.detectAndDecode(image)

    if points is not None:
        return data
    else:
        return ""