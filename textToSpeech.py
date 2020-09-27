from gtts import gTTS
import os

textToRead = open("demo.txt", 'r')

tts = gTTS(textToRead.read())
tts.save('demo.mp3')

os.system("demo.mp3")