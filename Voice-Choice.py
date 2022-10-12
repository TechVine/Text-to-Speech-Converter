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
file = open("story1.txt","w+")#A midsummer night's dream
s1 = """In Athens, Greece, a young man, Demetrius, has a problem.
‘Please, Hermia. I love you!’
‘No, Demetrius. I love Lysander!’
‘Love is never easy! Let’s run away together!’
Helena is Hermia’s friend. She loves Demetrius.
‘Demetrius, you know Hermia is running away to the forest with Lysander ...’
‘I’m going to follow them.’
‘Well, I’m going to follow you.’
In the forest, the fairy king Oberon wants to play a trick on Titania, his queen.
‘Go and find a magic flower! I’ll put the juice in your eyes. It will make you fall in love
with the first thing you see.’
Oberon sees Demetrius and Helena. He doesn’t like the way Demetrius talks to Helena.
‘Helena, go away! I don’t like you!’
‘Puck! Put this on Demetrius’s eyes so he will fall in love with Helena!’
Puck sees Lysander sleeping, and thinks it is Demetrius. Lysander wakes up and sees
Helena.
‘Helena, I love you!’
He doesn’t love Hermia any more!
A group of actors are in the forest, practising their play. Puck plays a trick on them
and changes Bottom’s head into a donkey’s. Naughty Puck!
‘What’s wrong? Hee-haw, hee-haw.’
‘Hee-haw, hee-haw.’
Titania falls in love with Bottom!
Oberon knows Puck put the juice on Lysander, not Demetrius, so he makes Demetrius
fall in love with Helena.
‘Helena, I love you!’
‘No, I love Helena!’
Lysander and Demetrius want to fight over Helena.
‘Why does no one love me?’
Oberon tells Puck to make a magic fog to put them all to sleep. Puck takes the love
spell away from Lysander.
Next Puck gives Bottom his human head again. Oberon takes the love spell away from
Titania.
In the morning, everybody wakes up.
‘I love you, Helena!’
‘I love you too, Demetrius!’
‘I love you, Hermia!’
‘I love you too, Lysander!’
Nobody remembers what happened! But now everybody is in love with the right
person, they decide to go home. Perhaps it was all just a dream!"""
file.write(s1)
'''-----------------------------------------------------------------------------------------------------------'''



'''-----------------------------------------------------------------------------------------------------------'''
file1 = open("story2.txt","w+")#A dog’s life
s2="""Hi. I’m Dino, the family dog. I help keep people safe, especially on the
roads. Take a look at my diary to see what I did last week.
Sunday
Some children really don’t think. Our neighbour’s boy ran in front of a
car to get his ball. The car almost hit him. I saved him though.
Remember, always look and listen.
Monday
Walking on the street at night can be very dangerous, especially if you wear dark clothes. Car drivers
can’t see you very well, just like these two I had to take home. Luckily I never go out without my
reflective jacket and collar. Remember, BE SEEN!
Tuesday
People can get very angry when driving, usually for silly reasons. One driver started shouting at Mum
today when she stopped to let some children cross the road. I soon made him stop.
Wednesday
One thing makes me really mad. Grrrrrr. People walking on a dangerous road when they can walk on
the safe pavement. I saw two girls doing that today but I soon made them change their minds.
Thursday
Seat belts can save your life! I make sure everyone in our car wears their seat belt. If they forget, I
soon remind them. Even I’ve got one.
Friday
I like Fridays. The roads are quieter. But you still have to be careful. I caught Dad talking on his mobile
phone while driving. I soon stopped him though. Don’t worry, he got his phone back.
Saturday
Today Mum took me for a walk. One car was parked in a very dangerous place. It was right on the
corner of the street. Don’t worry though. I left him a message"""
file1.write(s2)
'''-----------------------------------------------------------------------------------------------------------'''



'''-----------------------------------------------------------------------------------------------------------'''
file2 = open("story3.txt","w+")#ABC ZOO
s3="""It’s a special day at the ABC Zoo. A new animal is here.
‘What’s in it?’
‘It’s a zorilla from Africa. She needs a home.’
‘Mmm, zorilla, eh? OK, let’s find you a home.’
‘Let’s see. An aardvark, a boa constrictor, a coyote and a duck-billed platypus. The
zorilla doesn’t go here.’
‘Let’s see. An emu, a flamingo, a giraffe and a hyena. The zorilla doesn’t go here.’
‘Let’s see. An impala, a jellyfish, a koala and a lemur. The zorilla doesn’t go here.’
‘Let’s see. A meerkat, a narwhal, an orangutan and a puma. The zorilla doesn’t go here.’
‘Let’s see. A quetzal, a rhea, a sloth and a tarantula. The zorilla doesn’t go here.’
‘Let’s see. An umbrella bird, a vulture and a walrus. The zorilla doesn’t go here.’
‘Let’s see. A xenops, a yak, a zorilla! Here’s your home!'
'Sorry boys'"""
file2.write(s3)
'''-----------------------------------------------------------------------------------------------------------'''


'''-----------------------------------------------------------------------------------------------------------'''
file3 = open("story4.txt","w+")#Ali and the magic carpet
s4="""One very hot day Ali finds a carpet in his uncle’s shop.
‘What’s this?’
Suddenly the carpet jumps! It moves and flies off into the air.
‘Hey! What’s happening?’
A loud booming voice comes from the carpet.
‘Welcome, O master. I am a magic carpet.’
First they fly high up into the sky and then they land in a jungle. It is hot and wet and it’s raining.
‘It’s raining! Yuck!’
Then they fly to the desert. It is very, very hot and dry.
‘It is very, very hot today!’
After that they fly to the South Pole. There is lots of ice and snow. It’s freezing.
‘Brrr!’
‘Where are we now? I can’t see!’
‘In the mountains. Can you see me?’
‘It’s very foggy.’
Then they fly to a forest. It’s very windy there.
‘Oh, it’s windy in the forest!’
Then they fly to an island in the sea. There is thunder and lightning.
‘Aaagh! Let’s go home!’
‘What a storm!’
Finally they fly back home. The carpet lands in the shop and Ali gets off.
‘Wow! What an adventure!’"""
file3.write(s4)
'''-----------------------------------------------------------------------------------------------------------'''




'''-----------------------------------------------------------------------------------------------------------'''
file4 = open("story5.txt","w+")#Angel! Look out!
s5= """Angel and his grandpa live on the Great Barrier Reef in Australia.
Grandpa is tired.
‘I’m going to sleep now, Angel. Be good, and don’t go past the coral!
There are lots of dangerous animals out there.’
‘Hi, Angel. What are you doing?’
‘I’m bored. Grandpa is asleep.’
‘Do you want to come and play?’
‘Yes, let’s go!’
‘Look, Turtle! A ball!’
‘Look out! That isn’t a ball! It’s a dangerous octopus! Swim!’
‘Angel! Look out! There’s a dangerous fish behind you! Angel, you must be careful here. You’ve got to
stay with me!’
‘I’m sorry, Turtle. Look! I’ve got a present for you.’
‘Aargh! This is a dangerous cone shell! Drop it quickly, Angel!’
‘I’m tired, Turtle. Can we rest here?’
‘Don’t sit here, Angel! There’s a dangerous sea snake! Quick! Swim!’
‘Where are we?’
‘I don’t know. I think we’re lost. Look out, Angel! That’s a box jellyfish! Swim!’
‘Look out, Turtle! A dangerous animal is behind you!’
‘That’s not a dangerous animal. It’s Doug. He’s my friend.’
‘Hello, Doug. We’re lost. Can you help us?’
‘Yes, I can help you. I’ll take you home.’
‘Hello, Angel.’
‘Hello, Grandpa.’
‘Oh, you’ve been a very good fish, Angel. Here’s a present for you.’
‘Thanks, Grandpa!’
"""
file4.write(s4)
'''-----------------------------------------------------------------------------------------------------------'''
choice="""Which story you want to hear
1)A midsummer night's dream
2)A dog’s life
3)ABC ZOO
4)Ali and the magic carpet
5)Angel! Look out!
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