import time
from Timer import timer 
from pygame import mixer
def music(n):
    mixer.init()
    mixer.music.load(n)
    mixer.music.set_volume(1.7)
    mixer.music.play()
def tim():
    t=time.strftime("%I%M%S")
    # t=int(t)
    return t
# set time you as manually as you want
"""
Here w for water e, for eye and p for physical.
Here h for hour, m for minute and s for second.
"""
wh=1
wm=0
ws=0
eh=3
em=30
es=0
ph=4
pm=30
ps=0
wtrtim=timer(wh,wm,ws)
print("water: "+wtrtim)
# r1=wtrtim.replace(":","")
# r1=int(r1)
# print(r1)
eyetim=timer(eh,em,es)
print("eye: "+eyetim)
# r2=eyetim.replace(":","")
# r2=int(r2)
# print(r2)
acttim=timer(ph,pm,ps)
print("physical: "+acttim)
# r3=acttim.replace(":","")
# r3=int(r3)
# print(r3)
timdur = "080000"
timdur=int(timdur)
T=tim()
while T!=timdur:   
    T=tim()
    time.sleep(1)
    if T==wtrtim:
        """ put water.mp3 or other music as alarm in music function"""
        music()
        while True:
            a = input("\t\t\t\t\t\tplease drink water.\nFor stop write 'stop' and press enter: ")
            if a == 'stop':
                print("\n\t\t\t\t\t\tVery Good programmer\n\n\t\t\t\t\tI remember you at every set hour.")
                mixer.music.stop()
                wtrtim=timer(wh,wm,ws)
                print("water: "+wtrtim)
                # r1=wtrtim.replace(":","")
                # r1=int(r1)
                break
    elif T == eyetim:
        """ put eye.mp3 or other music as alarm in music function"""
        music()
        while True:
            a = input("\t\t\t\t\t\tplease rest your eye.\nFor stop write 'stop' and press enter: ")
            if a == 'stop':
                print("\n\t\t\t\t\t\tVery Good programmer\n\n\t\t\t\t\tI remember you at every set hour.")
                mixer.music.stop()
                eyetim=timer(eh,em,es)
                print("eye: "+eyetim)
                # r2=eyetim.replace(":","")
                # r2=int(r2)
                break
    elif T == acttim:
        """ put physical.mp3 or other music as alarm in music function"""
        music()
        while True:
            a = input("\t\t\t\t\t\tplease do some activity.\nFor stop write 'stop' and press enter: ")
            if a == 'stop':
                print("\n\t\t\t\t\t\tVery Good programmer\n\n\t\t\t\t\tI remember you at every set hour.")
                mixer.music.stop()
                acttim=timer(ph,pm,ps)
                print("physical: "+acttim)
                # r3=acttim.replace(":","")
                # r3=int(r3)
                break
print("Time to get sleep")