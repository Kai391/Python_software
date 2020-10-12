import requests
from googletrans import Translator
from win32com.client import Dispatch
def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
def trans(a,b):
    translator=Translator()
    trans=translator.translate(a,dest=b)
    p=trans.pronunciation
    if p == None:
        t=trans.text
        print('Tranlated:',t)
        speak(t)
    else:
        print('Tranlated:',p)
        speak(p)
	
if __name__ == "__main__":
    try:
        r=requests.get("https://www.google.com/")
        a=str(input("Type here: "))
        print("1.Hindi\n2.English")
        b=int(input("Type that no. which language you want to tranlate: "))
        while(True):
            try:
                if b == 1:
                    c="hi"
                    trans(a,c)
                elif b == 2:
                    c='en'
                    trans(a,c)
                a=input()
                break
                # elif b == 3:
                #     c='hy'
                #     trans(a,c)
                # elif b == 4:
                #     c='bn'
                #     trans(a,c)
            except:
                print("Connection Error\nPress any key for try again")
                i=input()
    except:
        print("No connection\nPlease make sure that you have internet connection......")
        a=input()
    