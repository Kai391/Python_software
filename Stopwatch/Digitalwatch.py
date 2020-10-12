import os
import time
def stopwatch():    
    # here 's' is second, 'm' is minute and 'h' is hour.
    s=0
    m=0
    h=0
    def clr():
        os.system('cls')
    clr()
    # S=int(input("set second: "))
    # M=int(input("set minute: "))
    # H=int(input("set hour: "))    
    clr()
    while True:
        while s <=59:
            if h < 10:
                if m < 10:
                    if s < 10 :
                        s=str(s)
                        m=str(m)
                        h=str(h)
                        print("0"+h+":0"+m+":"+"0"+s)
                        s=int(s)
                        s+=1
                        m=int(m)
                        h=int(h)
                        time.sleep(1)
                        clr()                        
                    else:
                        s=str(s)
                        m=str(m)
                        h=str(h)
                        print("0"+h+":0"+m+":"+s)
                        s=int(s)
                        s+=1
                        m=int(m)
                        h=int(h)
                        time.sleep(1)
                        clr()                           
                elif m>=10:
                    if s < 10 :
                        s=str(s)
                        m=str(m)
                        h=str(h)
                        print("0"+h+":"+m+":0"+s)
                        s=int(s)
                        s+=1
                        m=int(m)
                        h=int(h)
                        time.sleep(1)
                        clr()                           
                    else:
                        print("0"+str(h)+":"+str(m)+":"+str(s))
                        time.sleep(1)
                        clr()
                        s=int(s)
                        s+1
            else:
                if m < 10:
                    if s < 10 :
                        s=str(s)
                        m=str(m)
                        h=str(h)
                        print(h+":0"+m+":0"+s)
                        s=int(s)
                        s+=1
                        m=int(m)
                        h=int(h)
                        time.sleep(1)
                        clr()                          
                    else:
                        s=str(s)
                        m=str(m)
                        h=str(h)
                        print(h+":0"+m+":"+s)
                        s=int(s)
                        s+=1
                        m=int(m)
                        h=int(h)
                        time.sleep(1)
                        clr()                            
                elif m>=10:
                    if s < 10 :
                        s=str(s)
                        m=str(m)
                        h=str(h)
                        print(h+":"+m+":0"+s)
                        s=int(s)
                        s+=1
                        m=int(m)
                        h=int(h)
                        time.sleep(1)
                        clr()                          
                    else:
                        print(str(h)+":"+str(m)+":"+str(s))
                        time.sleep(1)
                        clr()
                        s=int(s)
                        s+=1                            
        if s>=59:
            s=0
            m=int(m)
            m+=1
            if m>=59:
                m=0
                h=int(h)
                h+=1
                if h>12:
                    h=0
                
stopwatch()