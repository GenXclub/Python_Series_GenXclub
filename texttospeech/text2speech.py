'''
Youtube Title:Text to Speech in Python|Python Series|Ep 2|GenXclub|Prajwal Mani
A small python program to convert text to speech using gtts
'''

from gtts import gTTS #pip install gtts
import os

s="Hello World!"
g=gTTS(text=s)
g.save("speech1.mp3") #to save the speech in mp3 format 
os.system("speech1.mp3") #to play the speech

# gtts-cli --all terminal command to check which and all languages are available under gtts
sj="ありがとうございました" #'Thank You in japanese'
gj=gTTS(text=sj,lang="ja") #ja is to select japanese language
gj.save("speech2.mp3")
os.system("speech2.mp3")

with open('text.txt','r') as myfile: #to open the text file
    data=myfile.read() #read the textfile
tg=gTTS(text=data)
tg.save("speech3.mp3")
os.system('speech3.mp3')

ts=gTTS(text=data,slow=True)
# slow is bool value if its true then the speech will be slower
ts.save("speech4.mp3")
os.system("speech4.mp3")