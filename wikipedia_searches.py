#importing required modules
import pyttsx3
import speech_recognition as sr
import wikipedia

assistantVoice = int(input('''Select you assistant's Voice
                               1) Male
                               2) Female : '''))

if assistantVoice == 1:
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
elif assistantVoice == 2:
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
else:
    print("Invalid Input")

# giving user some tips to search your query
print('''for your query to be answered speak in such way''')
print('''use {"google" or "search" or "wikipedia"} and then your_query''')
print('''For example: Search united nations''')

# defining various functions

# it will take the text obtained from wikipedia and then turn it into speech
def speak(audio):
    newVoiceRate = 131
    engine.setProperty('rate',newVoiceRate)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(type(query))
        print(f"User said: {query}\n")
        # converting user input into list of string to get keyword which need to be searched
        query_keyword = query.split()
        for i in query_keyword:
            if i == 'search' :
                query_keyword.remove('search')
            elif  i == 'google':
                query_keyword.remove('google')
            elif i == 'wikipedia':
                query_keyword.remove('wikipedia')   
                break
        # converting filtered input to string for obtaining output
        query_keyword_chr = " ".join(query_keyword)
        engine.say(f'searching {query_keyword_chr}' )

    # is program is unable to catch any words, it will repeat the process after some time 
    except Exception as e:
         print(e)  
         print("Say that again please...")
         return "None"
    return query_keyword_chr
            
    
 
if __name__ == "__main__":
   while True:
       query_keyword_chr = takeCommand().lower()
        # searching query
       if 'wikipedia' or 'search' or 'google' in query:
           
           query_keyword_chr = query_keyword_chr.replace("wikipedia", "")
           try:
               results = wikipedia.summary(query_keyword_chr, sentences=3)
               speak("According to Wikipedia")
               print(results)
               speak(results)
           except:
               engine.say("Error","Check your internet connection or Enter proper word")
       else:
           print("Error","Check your internet connection or Enter proper word")
      

