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
file = open("story1.txt","w+")#The Talking Birds
s1 = """Once upon a time, there lived two talking birds with their parents. One day when their parents were away, a villager who always had an eye on those special birds captured them and took them away. 

One of the birds escaped from the trap and searched for his parents. The Bird finally reached a hermitage where it was invited and had some food. He lived happily. 

A traveler once came across the other bird that was captured by the villager. He spoke very rudely to him. He was surprised to see a talking bird but was also upset with his behavior. 

The traveler visited the hermitage and recognized the similar talking bird but this bird spoke politely and invited him to stay there."""
file.write(s1)
'''-----------------------------------------------------------------------------------------------------------'''



'''-----------------------------------------------------------------------------------------------------------'''
file1 = open("story2.txt","w+")#Cotton Crop

s2="""In a village, there used to live a farmer named Raju, who worked hard to cultivate his crops and lead his family. Every other farmer would receive good benefits from their crops as they used to grow the crops that do not take much time to grow. 

Raju cultivated cotton crops and believed in his hard work to look after their growth. After 6 to 8 months, the cotton crops were fully grown. There was more demand for cotton during that time. 

A cotton textile manager bought all the cotton from Raju and paid a huge amount to him. This way Raju earned profit and was successful in supporting his family."""
file1.write(s2)
'''-----------------------------------------------------------------------------------------------------------'''



'''-----------------------------------------------------------------------------------------------------------'''
file2 = open("story3.txt","w+")#Old woman and her family
s3="""In a city, there lived a family with two children. The father’s mother was too old to be taken care of. She was a widow and lived alone in the village. The father brought her to the city and took care of her living.
While the father and mother were away his kids mistreated the old woman and asked her to leave.The old woman never complained to her son even though it happened every day. One day, the father found out that they have been treating his mother in a bad way. The father punished the children and explained to them the value of elders. 

He taught the children that like he’s their father, the old woman is his mother and she worked hard to give him a good life. Therefore, they should respect elders and behave nicely with old people."""
file2.write(s3)
'''-----------------------------------------------------------------------------------------------------------'''


'''-----------------------------------------------------------------------------------------------------------'''
file3 = open("story4.txt","w+")#Ideal student
s4="""In a school, every year the committee conducted the best student award. Every student tried their best to impress the managing team of the committee to select them for the school’s best student award. 

Ajay was not interested in winning the best student award, but he was an ideal student that the school admired. He used to go to school on time and reach home on time. He completed his homework and was always on the merit list. 

He maintained his records in other curriculum activities as well. He was selected for the best student award as he maintained discipline and respected everyone."""
file3.write(s4)
'''-----------------------------------------------------------------------------------------------------------'''




'''-----------------------------------------------------------------------------------------------------------'''
file4 = open("story5.txt","w+")#Lion Family
s5= """A Lion family lived happily in a jungle. There were two cubs in the family. The elder one was always careless of the younger cub. The mother lion always said positive words to the elder cub about family and the jungle.
One day, a hunter killed both the parent lions.The younger cub cried and did not know how to talk to his elder brother. The elder one remembered his mother’s words that he ignored and took the responsibility to look after his younger brother and the jungle.
From then, the elder one supported the younger cub and took care of him. Both the brothers lived happily and ruled the jungle.
"""
file4.write(s5)
'''-----------------------------------------------------------------------------------------------------------'''
choice="""Which story you want to hear
1)The Talking Birds
2)Cotton Crop
3)Old woman and her family
4)Ideal student
5)Lion Family
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
