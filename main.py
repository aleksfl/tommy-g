# Base imports for car code
import time
import sys
sys.path.append(r'/home/pi/picar-x/lib')
from utils import reset_mcu
reset_mcu()
from grayscale_module import Grayscale_Module
from ultrasonic import Ultrasonic
from pin import Pin
from tts import TTS
tts = TTS()

from picarx import Picarx
px = Picarx()

# our own imports
import camera

import steering
from steering import Steering
import lineFollower
from lineFollower import TapeFollower
import talk
import ultrasensor

#IMPORTANT CONSTANTS
trig_pin = Pin("D2")
echo_pin = Pin("D3")
grayscaleRef = 500
dirtLimit = 5
dirt=0

# This is from the specific QR code used to delimit room in demo
QRCodePartialUrl = "innsida.ntnu.no"

#Step size in seconds, most important variable for the operation of the system.
stepSize = 0.01

def main():
    dirtNumber = 0

    gm = Grayscale_Module(grayscaleRef)
    sonar = Ultrasonic(trig_pin, echo_pin)
    #gmFloor = lineFollower.getFloorLight()
    tapeFollower = TapeFollower()
    #Main loop goes here

    steering = Steering(0,0)

    while(True):
        #End previous movement and return to baseline state
        steering.setSpeed(0)
        steering.setAngle(0)

        dirtNumber+=lineFollower.detectDirt()
        if ultrasensor.isObstructed():
            talk.sayWarning()
            continue

        if ultrasensor.atWall():
            break
        state = lineFollower.tapeFollowerNew()
        tapeFollower.actOnState(state)
        time.sleep(stepSize)

    steering.stop()
    # Here we assume that the QR code is directly in front of the car
    # but it is relatively straightforward to orient towards a specific direction.
    if (QRCodePartialUrl in camera.captureQRCode()):
        # Here the data about level of dirt can be stored for each room and uploaded
        # for further use.
        if dirtNumber >= dirtLimit:
            talk.say("This room is dirty.")
        else:
            talk.say("This room is clean.")

if __name__ == "__main__":
    main()




