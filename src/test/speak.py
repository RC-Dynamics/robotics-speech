import pyttsx3
engine = pyttsx3.init() # object creation

engine.say("pick up blue bow")
engine.say("pick up blue bowl")
engine.runAndWait()
engine.stop()