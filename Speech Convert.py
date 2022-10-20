from gtts import gTTS  
  
# This module is imported so that we can  
# play the converted audio  
  
from playsound import playsound  
  
# It is a text value that we want to convert to audio  
text_val = 'Hello Hacktoberfest'  
  
# Here are converting in English Language  
language = 'en'  
  
 
obj = gTTS(text=text_val, lang=language, slow=False)  
  
#Here we are saving the transformed audio in a mp3 file named  
# exam.mp3  
obj.save("hacktoberfest.mp3")  
  
# Play the exam.mp3 file  
playsound("hacktoberfest.mp3")  
