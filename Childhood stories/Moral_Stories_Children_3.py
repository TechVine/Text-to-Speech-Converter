import pyttsx3


assistantVoice = int(input('''Select you assistants Voice 
  [1] Male 
  [2] Female : '''))


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



'''-----------------------------------------------------------------------------------------------------------'''
file = open("story1.txt","w+")#The Farmer And The Crane
s1 = """Once there was a farmer who was worried about his crops. His crops were being eaten by the birds every day.

Agitated, he decided to trap the birds the next day. When the birds came, he managed to capture them with a big net. A crane too got trapped with them.

The crane pleaded the farmer to free him.

To this request, the farmer answered, “You were found in the company of these birds who destroyed my crops. I cannot let you go. I won’t spare you either.”"""
file.write(s1)
'''-----------------------------------------------------------------------------------------------------------'''



'''-----------------------------------------------------------------------------------------------------------'''
file1 = open("story2.txt","w+")#The Lion and the Poor Slave

s2="""There was once a slave whose master was cruel to him. One day, he couldn’t stand it anymore, so he fled into the forest. On his way, he encountered a lion that was unable to walk because of a thorn in its paw.
Even though he was scared, the slave mustered his courage and pulled out the thorn in the lion’s paw. 

When the lion was free from the thorn, he ran into the forest without hurting the slave. Soon after, the slave was caught by his master in the forest. The slave was then thrown into the lion’s den by his master.

As soon as he saw the lion, the slave recognized it as the same lion he had rescued previously. As a result, the slave escaped unharmed."""
file1.write(s2)
'''-----------------------------------------------------------------------------------------------------------'''



'''-----------------------------------------------------------------------------------------------------------'''
file2 = open("story3.txt","w+")#Haughty Oak Tree
s3="""In the oak tree’s eyes, he was a robust tree. He thought to himself, “I am way stronger than these weak reeds. Unlike them, I stand alone in the storm, never bend to the wind’s will.”

The same night nature took a toll, a powerful storm came.

In the morning, reeds found the mighty oak tree uprooted. They said, “Oh lord, we are grateful that we can bend and don’t just break.”"""
file2.write(s3)
'''-----------------------------------------------------------------------------------------------------------'''


'''-----------------------------------------------------------------------------------------------------------'''
file3 = open("story4.txt","w+")#The Fox and the Grapes
s4="""One afternoon, a fox was walking through the forest and spotted a bunch of grapes hanging from a lofty branch. “Just the thing to quench my thirst,” said the fox.

Taking a few steps back, the fox jumped and just missed the hanging grapes. Again, the fox took a few paces back and tried to reach them, but still failed.

Short StoriesFinally, giving up, the fox turned up his nose and said, “They’re probably sour anyway.” Then he walked away."""
file3.write(s4)
'''-----------------------------------------------------------------------------------------------------------'''




'''-----------------------------------------------------------------------------------------------------------'''
file4 = open("story5.txt","w+")#Two friends and the bear
s5= """Once there were two friends who were crossing a jungle when they saw a bear approaching. Both of them got frightened and one of them quickly climbed up the tree leaving behind his friend who did not know how to climb a tree.  
So he got an idea and laid on the ground pretending to be dead by holding his breath. The bear soon came to him, sniffed his ears, and left him after a few minutes. 
When the bear went into the jungle again leaving them two. The other friend on the tree came down and asked his friend “what the bear told you in your ears?”. That is when the friend replied “the bear said to be aware of the fake friends.”
"""
file4.write(s5)
'''-----------------------------------------------------------------------------------------------------------'''
choice="""Which story you want to hear
1)The Farmer And The Crane
2)The Lion and the Poor Slave
3)Haughty Oak Tree
4)The Fox and the Grapes
5)Two friends and the bear
"""
file.close()
file1.close()
file2.close()
file3.close()
file4.close()
r1= open("story1.txt","r")
r2= open("story2.txt","r")
r3= open("story3.txt","r")
r4= open("story4.txt","r")
r5= open("story5.txt","r")
engine.say(choice)
engine.runAndWait()
inp = int(input("1/2/3/4/5 :- "))
if(inp == 1):
    for x in r1:
        print(x)
        engine.say(x)
        engine.runAndWait()
        r1.close()
elif(inp == 2):
    for x in r2:
        engine.say(x)
        engine.runAndWait()
        r2.close()
elif(inp == 3):
    for x in r3:
        engine.say(x)
        engine.runAndWait()
        r3.close()
elif(inp == 4):
    for x in r4:
        engine.say(x)
        engine.runAndWait()
        r4.close()
elif(inp == 5):
    for x in r5:
        engine.say(x)
        engine.runAndWait()
        r5.close()
else:
    print("Invalid Input")
