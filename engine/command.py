import pyttsx3  # used for text to speech
import speech_recognition as sr
import eel


def speak(text):
    text = str(text)
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty(
        "voices"
    )  # command used to get the voices installed on system
    # print(voices) # To see all voices
    engine.setProperty("voice", voices[0].id)  # command used to set the voice of choice
    engine.setProperty("rate", 174)  # command to set the speed of speech
    # eel.DisplayMessage(text)
    engine.say(text)
    # eel.receiverText(text)
    engine.runAndWait()


# speak("Hello Sir, I am JARVIS")
# speak("How can I assist you today?")


@eel.expose
def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening....")
        eel.DisplayMessage("listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

    try:
        print("recognizing")
        eel.DisplayMessage("recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        # time.sleep(2)

    except Exception as e:
        return ""

    return query.lower()


# text = takecommand()
# speak(text)
