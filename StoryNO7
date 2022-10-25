
import pyttsx3

assistantVoice = int(input('''Select you assistants Voice 
  [1] DAVID 
  [2] HAZEL
  [3] ZIRA : '''))


if assistantVoice == 1:
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
elif assistantVoice == 2:
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
elif assistantVoice == 3:
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[2].id)
else:
    print("Invalid Input")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

r1= open("STORY_NO7.txt","r")
s1 = """Two friends and the Bear. Once there were two friends who were crossing the jungle. After some time they saw a bear coming towards them. 
Then, one of the friends quickly climbed the nearby tree and the other one did not know how to climb the tree. So he lays down on the ground holding his breath.
The bear reaches near him and sniffs him in the ear. After some time bear left the place, thinking the man is dead.
Now the other friend climbs down and asked his friend, what did bear said to him in his ear? He replied,” to be safe from the fake friends.”"""

if __name__=="__main__":
    for s1 in r1:
        print(s1)
        speak(s1)
    r1.close()   

    
