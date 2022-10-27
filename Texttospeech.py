import speech_recognition as sr
sec= sr.Recognizer()

mic = sr.Microphone()

print('start')
with mic as source:
    audio = sec.listen(source)
print('end')
print(sec.recognize_google(audio))
