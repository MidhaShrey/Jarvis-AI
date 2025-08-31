import pyttsx3

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    # print(voices) # To see all voices
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    # eel.DisplayMessage(text)
    engine.say(text)
    # eel.receiverText(text)
    engine.runAndWait()

speak("Hello Sir, I am JARVIS")