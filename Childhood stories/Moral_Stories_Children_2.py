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
file = open("story1.txt","w+")#The Loyal Dog
s1 = """There was a stray dog in a village. That dog used to sit outside a school in the village.

A boy studying in the fifth standard used to feed both the pieces of bread of his tiffin to that dog.

He was doing this for the last five months. One day some boys in his class started beating him outside the school.

As soon as the dog saw the incident, he ran fast. Seeing the dog coming near to them, all the boys ran away.

The boy hugs the dog and thanks to him."""
file.write(s1)
'''-----------------------------------------------------------------------------------------------------------'''



'''-----------------------------------------------------------------------------------------------------------'''
file1 = open("story2.txt","w+")#Greedy snake

s2="""A snake was wandering in the forest. He saw a mouse bill on the way and entered it.

There were about seven rats in that bill. He ate all the rats one by one out of greed, but when he came out of the bill, he found it difficult to crawl.

When he got tired, he stopped. Then, he thought, “what to do now?”

At the same time, an eagle saw the snake and ate after killing him."""
file1.write(s2)
'''-----------------------------------------------------------------------------------------------------------'''



'''-----------------------------------------------------------------------------------------------------------'''
file2 = open("story3.txt","w+")#Dog and the Bone
s3="""Once there was a dog who wandered the streets night and day in search of food. One day, he found a big juicy bone and he immediately grabbed it between his mouth and took it home.
On his way home, he crossed a river and saw another dog who also had a bone in its mouth. He wanted that bone for himself too. 
But as he opened his mouth, the bone he was biting fell into the river and sank. That night, he went home hungry."""
file2.write(s3)
'''-----------------------------------------------------------------------------------------------------------'''


'''-----------------------------------------------------------------------------------------------------------'''
file3 = open("story4.txt","w+")#Lazy John
s4="""There was a boy named John who was so lazy, he couldn’t even bother to change his clothes. One day, he saw that the apple tree in their yard was full of fruits.
He wanted to eat some apples but he was too lazy to climb the tree and take the fruits. So he lay down underneath the tree and waited for the fruits to fall off. 
John waited and waited until he was very hungry but the apples never fell."""
file3.write(s4)
'''-----------------------------------------------------------------------------------------------------------'''




'''-----------------------------------------------------------------------------------------------------------'''
file4 = open("story5.txt","w+")#The Elephant and the Ants
s5= """There was once a proud elephant who always bullied smaller animals. He would go to the anthill near his home and spray water at the ants. 
The ants, with their size, could do nothing but cry. The elephant just laughed and threatened the ants that he would crush them to death. One day, the ants had enough and decided to teach the elephant a lesson. 
They went straight into the elephant’s trunk and started biting him. The elephant could only howl in pain. He realized his mistake and apologized to the ants and all the animals he bullied.
"""
file4.write(s5)
'''-----------------------------------------------------------------------------------------------------------'''
choice="""Which story you want to hear
1)The Loyal Dog
2)Greedy snake
3)Dog and the Bone
4)Lazy John
5)The Elephant and the Ants
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
