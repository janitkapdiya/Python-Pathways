# 3. Install an external module and use it to perform an operation of your interest.
# For this problem we are going to install pyttsx3 (Text to Speech (TTS) library for Python 3).

import pyttsx3
engine = pyttsx3.init()
engine.say("Welcome Kapadiya, How are you?") #Place your text here!
print("Speaking...")
engine.runAndWait()
print("Completed")