from grayscale_module import Grayscale_Module
from picarx import Picarx
import steering
import talk
import time
from steering import Steering
from enum import Enum

steering = Steering()
class State(Enum):
    Initial = 0
    Forward = 1
    Left = 2
    Right = 3
    Broken = 4
    Both = 5

def measureToBool(value):
    return value>1250

def measureGS(gm):
    return gm.get_grayscale_data()

def detectDirt():
    gm = Grayscale_Module(1300)
    gm_val_list = measureGS(gm)
    gm_status = gm.get_line_status(gm_val_list)

    if gm_status=='forward'or gm_status=='left' or gm_status=='right':
        return 0
    else:
        return 1

class TapeFollower():
    def __init_subclass__(self):
        self.prevState = State.Initial

    def actOnState(self, currentState):
        if currentState == State.Initial or currentState == State.Forward:
            self.steer(0) # Not strictly neccesary but nice to do in any case
            self.setFwdSpd(1)
        elif currentState == State.Left:
            self.steer(-6)
            self.setFwdSpd(1)
        elif currentState == State.Right:
            self.steer(-6)
            self.setFwdSpd(1)
        elif currentState == State.Broken:
            raise Exception("Invalid greyscale measurement")
        elif currentState == State.Both:
            if self.prevState == State.Both:
                self.steer(-6)
                self.setFwdSpd(1)
            else:
                self.steer(6)
                self.setFwdSpd(1)
        self.prevState = currentState

def tapeFollowerNew():
    gm=Grayscale_Module(500)
    dataArray=gm.get_grayscale_data()

    left = measureToBool(dataArray[0])
    middle = measureToBool(dataArray[1])
    right = measureToBool(dataArray[2])
    state = State.Initial
    if (left and middle and right) or (not left and middle and not right):
        state = State.Forward
    elif (not left and not middle and right) or (not left and middle and right):
        state = state.Right
    elif (left and not middle and not right) or (left and middle and not right):
        state = state.Left
    elif left and not middle and right:
        state = state.Broken
    elif not left and not middle and not right:
        state = state.Both
    else:
        raise Exception("Invalid greyscale states")
    return state


