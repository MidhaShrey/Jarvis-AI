import os
import eel

from engine.features import *

playAssistantSound()

eel.init('frontend')
# Command to open in App Mode
os.system('start msedge.exe --app=http://localhost:8000/index.html')

eel.start('index.html', mode=None, host='localhost', block=True)