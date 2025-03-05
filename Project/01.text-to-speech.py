# To Install Library Text to Speech (TTS) library for Python "pip install pyttsx3"
import pyttsx3

user_text = input("✍️  Enter a text to speak: ")

engine = pyttsx3.init()
engine.say(user_text)
print("🗣️  Speaking...")
engine.runAndWait()
print("✅ Completed")