from ultrasonic import Ultrasonic
from pin import Pin
import talk


trig_pin = Pin("D2")
echo_pin = Pin("D3")

sonar = Ultrasonic(trig_pin, echo_pin)

def readDistance():
    return sonar.read()

def isObstructed():
    distance = readDistance()
    if distance >= 0:
        return distance < 15 #Roughly length of the car
    else:
        return False

def atWall():
    distance=readDistance()
    return distance>0 and distance<25
