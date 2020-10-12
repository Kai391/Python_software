from time import sleep
import json
import requests
from win32com.client import Dispatch
def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
def req(a):
    r = requests.get(a)
    R=r.text
    return R
if __name__ == "__main__":
    try:
        req("https://www.google.com/")
        try:
            news=json.loads(req("http://newsapi.org/v2/top-headlines?country=in&apiKey=7e87bf5d606a45788859329f41b3bba3"))
            speak('News for Today')
            n=0
            for l in news["articles"]:
                try:
                    if i == 1:
                        speak("Next headline is")
                except:
                    pass
                n+=1
                print(f"{n}.",l['title'])
                speak(l['title'])
                sleep(1)
                i=1
            speak("Today's news is to be end")
            speak("Thank you")
        except:
            print("Connection lost or site have server issue........")
            speak("Connection lost or site have server issue")
    except:
        print("No connection\nPlease make sure that you have internet connection.......")
        speak("No connection\nPlease make sure that you have internet connection")
        