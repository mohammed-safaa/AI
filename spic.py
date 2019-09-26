from gtts import gTTS

teXt = "I love you Shler"
tts = gTTS(text=teXt, lang='ar', slow=False)
tts.save('hello.mp3')
