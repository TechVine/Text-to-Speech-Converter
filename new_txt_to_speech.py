import pyttsx3
import argparse
import traceback
import sys

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--text", help="string input")
parser.add_argument("-l", "--language", help="english or hindi")
parser.add_argument("-a", "--accent", help="indian, australian, us & uk")
parser.add_argument("-g", "--gender", help="male or female")
parser.add_argument("-i", "--index", help="reader index, start from zero.")

args = parser.parse_args()


text_to_read = "Hi there! I'll read text for you."
gender = "male"
language = "english"
accent = "us"

if args.text:
    text_to_read = args.text

if args.language:
    language = args.language
    if language == "hindi":
        accent = "indian"

if args.accent:
    accent = args.accent


if args.gender:
    gender = args.gender


def filter_rule(voice, gender, language, accent, default):
    if default:
        return voice.gender in gender and voice.languages[0] == (language + '_' + accent)
    return voice.languages[0] == (language + '_' + accent) or voice.name in ["default", "Alex"]


# Filtering voices based on given critaria
def filter_voice(voices, gender, language, accent, default=True):
    filter_list = [voice for voice in voices if filter_rule(
        voice, gender, language, accent, default)]
    if len(filter_list):
        return filter_list
    return filter_voice(voices, gender, language, accent, False)

def update_language(reader, language, accent, gender):
    languages = {"english": "en", "hindi": "hi"}
    genders = {"male": ["VoiceGenderMale", "male"], "female": ["VoiceGenderFemale", "female"], "none": ["None"]}
    accents = {"indian": "IN", "us": "US", "australian": "AU", "uk": "GB"}

 
    filtered_voice_list = filter_voice(reader.getProperty(
        'voices'), genders[gender], languages[language], accents[accent])

    if len(filtered_voice_list):
 
        print("AVAILABLE READERS")
        for index, voice in enumerate(filtered_voice_list):
            print("\nVoice Index : %d" % index)
            print("ID: %s" % voice.id)
            print("Name: %s" % voice.name)
            print("Age: %s" % voice.age)
            print("Gender: %s" % voice.gender)
            print("Languages Known: %s" % voice.languages)

        index = 0
        try:
            if args.index and filtered_voice_list[int(args.index)]:
                index = int(args.index)
        except IndexError:
            pass

        print("\n%s is reading for you." % filtered_voice_list[index].name)
        reader.setProperty('voice', filtered_voice_list[index].id)
    else:
        print("No reader available.\nAlex is reading for you.")


try:
    reader = pyttsx3.init()
    update_language(reader, language, accent, gender)

    reader.say(text_to_read)

    reader.runAndWait()
    reader.stop()

except OSError as error:
    traceback.print_exception(*sys.exc_info())
    print("There is a chance that some required system lib is missing, install the lib and try again")

except Exception as error:
    traceback.print_exception(*sys.exc_info())
    print("Someting went wrong; please report the issue at https://github.com/vishalnagda1/text-to-speech/issues")
