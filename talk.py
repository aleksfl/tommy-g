from tts import TTS
tts = TTS()

def say(text):
    tts.say(text)

def sayWarning():
    say("Please move!")