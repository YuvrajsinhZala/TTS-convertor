from gtts import gTTS
text=""
with open("tts.txt","r") as file:
    for line in file:
        text=text + line
        
speech=gTTS(text)

speech.save("hello.mp3")
