from pygame import mixer 
from gtts import gTTS
t= " kya haal hai"

s=gTTS(t,slow='False')
s.save("h.mp3")
mixer.init()
mixer.music.load('h.mp3')
mixer.music.set_volume(0.7)
mixer.music.play()