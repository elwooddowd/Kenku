import difflib
from pydub import AudioSegment
from pydub.playback import play
from playsound import playsound

memes = {'okay':'okay.mp3', 'ja':'ja.mp3'}

print(difflib.get_close_matches('ok', memes))
print(difflib.get_close_matches('ja', memes))

#playsound('Stefan.mp3') #Playsound_alternative

play(AudioSegment.from_mp3("okay2.mp3")) #pydub

while True:
    eingabe = input("Sound?")
    closeeingabe = difflib.get_close_matches(eingabe, memes)
    try:
        x = closeeingabe[0]
        #print("x ", x)
        print("get ", memes.get(x))
        playsound(memes.get(x))
    except:
        pass
    try:
        eingabe = None
        closeeingabe[0] = None
        x = None
    except:
        pass