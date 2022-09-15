import sys

# While this class is not used for our specific implementation, it gives an
# example of a more general implementation of our core loop based state machine.
class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
    def addState(self, name, handler):
        name = name.upper()
        self.handlers[name] = handler

    def setStart(self, name):
        self.startState = name.upper()

    def run(self, value):
        try:
            handler = self.handlers[self.startState]
        except:
            raise Exception("must call .set_start() before .run()")


        while True:
            (newState, value) = handler(value)
            handler = self.handlers(newState.upper())

