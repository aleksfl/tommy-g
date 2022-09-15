from pin import Pin
from picarx import Picarx
import time

px = Picarx()


class Steering:
    def __init__(self, initAngle = 0, initSpeed = 0):
        self.px = Picarx()

        self.px.set_dir_servo_angle(initAngle)
        self.px.forward(initSpeed)

        self.angle = initAngle
        self.speed = initSpeed


    # negative speed is backwards
    def setSpeed(self, speed):
        for i in range(self.speed, speed):
            if i >=0:
                self.px.forward(i)
            else:
                self.px.backward(-i)
            time.sleep(0.01)

        self.speed = speed


    def stop(self):
        self.setSpeed(0)


    def setAngle(self, angle):
        for i in range(self.angle, angle):
            self.px.set_dir_servo_angle(i)
            time.sleep(0.01)

        self.angle = angle

    def move(self, time):
        self.setSpeed(1)
        time.sleep(time)
        self.stop()

    #DEPRECATED
    def setFwdSpd(self, speed):
        self.setSpeed(speed)
    def setBwdSpd(self, speed):
        self.setSpeed(-speed)
    def steer(self, angle):
        self.setAngle(angle)

class FollowLine:
    def __init__(self, steering):
        self.steering = steering



