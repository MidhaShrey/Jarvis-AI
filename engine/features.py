from playsound import playsound
import eel

# Playing Assistant Sound function
@eel.expose
def playAssistantSound():
    music_dir = "frontend\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)
