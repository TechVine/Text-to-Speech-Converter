from gtts import gTTS  


from playsound import playsound  

text_to_convert = 'All the best for your exam.'  

language = 'en'  

obj = gTTS(text=text_to_convert, lang=language, slow=False)  

obj.save("exam.mp3")  

playsound("exam.mp3") 