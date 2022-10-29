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
file = open("story1.txt","w+")#Two Friends 
s1 = """There were two very close friends. One friend was rich and the other was poor. The rich friend would often ask the other to tell him whenever he needed money so that he could help him.

But, the poor friend never got such a chance. One day the poor friend really needed money, and he thought that he would ask his friend.

When he asked him, he refused by giving an excuse.”"""
file.write(s1)
'''-----------------------------------------------------------------------------------------------------------'''



'''-----------------------------------------------------------------------------------------------------------'''
file1 = open("story2.txt","w+")# An intelligent farmer

s2="""A farmer was returning home after selling all his vegetables. On the way, he met a miscreant. The miscreant looked very dangerous as he had a sword-like knife.
The farmer got scared and gave all his money to the miscreant.

When the miscreant started leaving from there, the farmer said, “You have looted all my money, please give me something that I can show my wife so that she will be happy.”

The miscreant took pity and gave his knife to him. The farmer was so intelligent that he took back all his money from him with the help of the knife."""
file1.write(s2)
'''-----------------------------------------------------------------------------------------------------------'''



'''-----------------------------------------------------------------------------------------------------------'''
file2 = open("story3.txt","w+")#The woman without her husband 
s3="""A couple was living their life happily. The woman’s husband had a clothing business. One day suddenly his health deteriorated very much and he died. Now calamity had arisen in front of the woman.

She was very depressed about how she would take care of herself and her children. Her husband’s shop was closed. She had no idea what to do.

One day she courageously went ahead and reopened the shop. She was very scared about how everything would be managed but gradually everything got better and now she was living happy life again without her husband.”"""
file2.write(s3)
'''-----------------------------------------------------------------------------------------------------------'''


'''-----------------------------------------------------------------------------------------------------------'''
file3 = open("story4.txt","w+")#Old parents
s4="""A man was very upset with his old parents. He sometimes beat them in anger. One day he threw them out of his house. They both left the house sadly and never came back.

Now, the man lived happily with his wife and children. Twenty years later, now his children had grown up, and all of them had got married. They were doing the same with the man as he used to with his parents.

He remembered those days and was deeply saddened for the atrocities that he had done against his parents."""
file3.write(s4)
'''-----------------------------------------------------------------------------------------------------------'''




'''-----------------------------------------------------------------------------------------------------------'''
file4 = open("story5.txt","w+")#The dog and the shadow
s5= """A Dog was carrying a piece of meat in his mouth to eat it in peace at home. On his way he had to cross a bridge across a brook. As he crossed, he looked down and saw his own reflection in the water. 
Thinking it was another dog with another piece of meat, he made up his mind to have that also. 
So he made a snap at the shadow in the water, but as he opened his mouth the piece of meat fell out, dropped into the water and was lost.”
"""
file4.write(s5)
'''-----------------------------------------------------------------------------------------------------------'''
choice="""Which story you want to hear
1)Two Friends 
2) An intelligent farmer
3)The woman without her husband 
4)Old parents
5)The dog and the shadow
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
