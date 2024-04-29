import speech_recognition as sr
import os
import wikipedia
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello i am Jarvis")
engine.runAndWait()
engine.stop()

