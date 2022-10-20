import pyttsx3                     #Importing pyttsx3 module into the program.

print("\nWelcome to my Story-telling Program\n")  #Introduction

#Voice Change

text_to_speech = int(input('''Choose your desired voice for story-telling 
  [1] Male 
  [2] Female
  Choice: '''))


if text_to_speech == 1 :
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    
elif text_to_speech == 2 :
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)

else :
    print("Invalid! Choice")
    
#Text_to_Speech conversion of various stories in the text files

def Story1() :
             Story1 = open("Story1.txt")
             s1= Story1.read()
             engine.say(s1)
             engine.runAndWait()


def Story2() :
             Story2 = open("Story2.txt")
             s2= Story2.read()
             engine.say(s2)
             engine.runAndWait()


def Story3() :
             Story3 = open("Story3.txt")
             s3= Story3.read()
             engine.say(s3)
             engine.runAndWait()


def Story4() :
             Story4 = open("Story4.txt")#The Cursed Man or King?
             s4= Story4.read()
             engine.say(s4)
             engine.runAndWait()


def Story5() :
             Story5 = open("Story5.txt")#The Cursed Man or King?
             s5= Story5.read()
             engine.say(s5)
             engine.runAndWait()


#Selecting the story narrated by the voice by providing an input

while True :
            ch='''Alright! What kind of a story you would like to hear?
                  1)The Talkative Turtle
                  2)The Sleepless King
                  3)The Golden Bird
                  4)The Mouse Maiden
                  5)The Fox and the Crow
                  Select your option otherwise choose exit'''
 
            engine.say(ch)
            engine.runAndWait()

            sel = int(input('''\n1)The Talkative Turtle  2)The Sleepless King  3)The Golden Bird  4)The Mouse Maiden  5)The Fox and the Crow  6)Exit\nSelect your option: '''))

            if(sel == 1) :
     
                Story1()

            elif(sel == 2) :

                Story2()
   
            elif(sel == 3) :

                Story3()

            elif(sel == 4) :
    
                Story4()

            elif(sel == 5) :
    
                Story5()

            elif(sel == 6) :

                exit()

            else:

                print("Invalid! Selection")       
                continue
#---------------------------------------------End of the program-------------------------------------------------------