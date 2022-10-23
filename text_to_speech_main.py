#pip install pyttsx3
#pip install comtypes if working with windows only

import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

x = 'Hello Everyone I am Contributing in Hacktoberfest'


engine.say(x)

engine.runAndWait()




