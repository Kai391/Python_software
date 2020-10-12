import time
def timer(Hon,Min,Sec):
    """
    Hon,Min,Sec are these integar.
    This is timer progarm which add int(Hon) to Hour,int(Min) to minutes and 
    int(Sec) to seconds which were given by user.
    """
    # h= "08"
    # m= "02"
    # s= "02"
    # print(h+":"+m+":"+s)
    # the above 4 lines is for check 
    # r= time.strftime("%I:%M:%S")
    # print(r)
    # Hon = int(input("enter hour: "))
    # Min= int(input("enter mins: ")) 
    # Sec= int(input("enter sec: ")) 
    # the above 3 lines is for code internal
    h = time.strftime("%I")
    m = time.strftime("%M")
    s = time.strftime("%S")
    h = int(h)
    m = int(m)
    s = int(s)
    H = h+Hon
    M = m+Min
    S= s+Sec
    if H >12:
        H-=12
        if H < 10:
            H=str(H)
            H1="0"+H
            if M >=60:
                M-=60
                H=int(H)
                H+=1
                H=str(H)
                H1="0"+H
                if M < 10:
                    if S >=60:
                        S-=60
                        M=int(M)
                        M=M+1
                        M=str(M)
                        p1="0"+M
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{p1}:{p2}")
                            # print(N)
                            return n
                        else:    
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{p1}:{ss}")
                            # print(N)
                            return n
                    else:
                        M=str(M)
                        p1="0"+M
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{p1}:{p2}")
                            # print(N)
                            return n 
                        else:   
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{p1}:{ss}")
                            # print(N)
                            return n        
                else:    
                    if S >=60:
                        S-=60
                        M=int(M)
                        M=M+1
                        M=str(M)
                        p1=M
                        if S < 10:
                            S=str(S)
                            p="0"+S
                            n=time.strftime(f"{H1}:{p1}:{p}")
                            # print(N)
                            return n
                        else:   
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{p1}:{ss}")
                            # print(N)
                            return n 
                    else:
                        M=str(M)
                        mm=M   
                        if S < 10:
                            S=str(S)
                            p="0"+S
                            n=time.strftime(f"{H1}:{mm}:{p}")
                            # print(N)
                            return n
                        else:   
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{mm}:{ss}")
                            # print(N)
                            return n             
            else:
                if M < 10:
                    M=str(M)
                    p1="0"+M
                    if S >=60:
                        S-=60
                        M=int(M)
                        M+=1
                        M=str(M)
                        p1="0"+M
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{p1}:{p2}")
                            # print(N)
                            return n
                        else:    
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{p1}:{ss}")
                            # print(N)
                            return n 
                    else:    
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{p1}:{p2}")
                            # print(N)
                            return n
                        else:    
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{p1}:{ss}")
                            # print(N)
                            return n   
                else:    
                    M=str(M)
                    mm=M
                    if S >=60:
                        S-=60
                        M=int(M)
                        M+=1
                        M=str(M)
                        mm=M                        
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{mm}:{p2}")
                            # print(N)
                            return n
                        else:    
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{mm}:{ss}")
                            # print(N)
                            return n
                    else:
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{mm}:{p2}")
                            # print(N)
                            return n
                        else:    
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{mm}:{ss}")
                            # print(N)
                            return n
        else:
            H=str(H)
            H1=H
            if M >=60:
                M-=60
                H=int(H)
                H+=1
                if H <=12:
                    H=str(H)
                    H1=H
                else:
                    H=int(H)
                    H=-12
                    H=str(H)
                    H1="0"+H
                if M < 10:
                    M=str(M)
                    p1="0"+M
                    if S >=60:
                        S-=60
                        M=int(M)
                        M+=1
                        M=str(M)
                        p1="0"+M
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{p1}:{p2}")
                            # print(N)
                            return n
                        else:    
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{p1}:{ss}")
                            # print(N)
                            return n
                    else:
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{p1}:{p2}")
                            # print(N)
                            return n 
                        else:   
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{p1}:{ss}")
                            # print(N)
                            return n        
                else:    
                    M=str(M)
                    mm=M
                    if S >=60:
                        S-=60
                        M=int(M)
                        M+=1
                        M=str(M)
                        mm=M
                        if S < 10:
                            S=str(S)
                            p="0"+S
                            n=time.strftime(f"{H1}:{mm}:{p}")
                            # print(N)
                            return n
                        else:   
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{mm}:{ss}")
                            # print(N)
                            return n 
                    else:   
                        if S < 10:
                            S=str(S)
                            p="0"+S
                            n=time.strftime(f"{H1}:{mm}:{p}")
                            # print(N)
                            return n
                        else:   
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{mm}:{ss}")
                            # print(N)
                            return n      
            else:
                if M < 10:
                    M=str(M)
                    p1="0"+M
                    if S >=60:
                        S-=60
                        M=int(M)
                        M+=1
                        M=str(M)
                        p1="0"+M
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{p1}:{p2}")
                            # print(N)
                            return n
                        else:    
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{p1}:{ss}")
                            # print(N)
                            return n 
                    else:    
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{p1}:{p2}")
                            # print(N)
                            return n
                        else:    
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{p1}:{ss}")
                            # print(N)
                            return n   
                else:    
                    M=str(M)
                    mm=M
                    if S >=60:
                        S-=60
                        M=int(M)
                        M+=1
                        M=str(M)
                        mm=M
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{mm}:{p2}")
                            # print(N)
                            return n
                        else:    
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{mm}:{ss}")
                            # print(N)
                            return n
                    else:    
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{mm}:{p2}")
                            # print(N)
                            return n
                        else:    
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{mm}:{ss}")
                            # print(N)
                            return n
    else:
        if H < 10:
            H=str(H)
            H1="0"+H
            if M >=60:
                M-=60
                H=int(H)
                H+=1
                H=str(H)
                H1="0"+H
                if M < 10:
                    M=str(M)
                    p1="0"+M
                    if S >=60:
                        S-=60
                        M=int(M)
                        M+=1
                        M=str(M)
                        p1="0"+M
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{p1}:{p2}")
                            # print(N)
                            return n
                        else:    
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{p1}:{ss}")
                            # print(N)
                            return n
                    else:
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{p1}:{p2}")
                            # print(N)
                            return n 
                        else:   
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{p1}:{ss}")
                            # print(N)
                            return n        
                else:    
                    M=str(M)
                    mm=M
                    if S >=60:
                        S-=60
                        M=int(M)
                        M+=1
                        M=str(M)
                        mm=M
                        if S < 10:
                            S=str(S)
                            p="0"+S
                            n=time.strftime(f"{H1}:{mm}:{p}")
                            # print(N)
                            return n
                        else:   
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{mm}:{ss}")
                            # print(N)
                            return n 
                    else:   
                        if S < 10:
                            S=str(S)
                            p="0"+S
                            n=time.strftime(f"{H1}:{mm}:{p}")
                            # print(N)
                            return n
                        else:   
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{mm}:{ss}")
                            # print(N)
                            return n            
            else:
                if M < 10:
                    M=str(M)
                    p1="0"+M
                    if S >=60:
                        S-=60
                        M=int(M)
                        M+=1
                        M=str(M)
                        p1="0"+M
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{p1}:{p2}")
                            # print(N)
                            return n
                        else:    
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{p1}:{ss}")
                            # print(N)
                            return n 
                    else:
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{p1}:{p2}")
                            # print(N)
                            return n
                        else:    
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{p1}:{ss}")
                            # print(N)
                            return n    
                else:    
                    M=str(M)
                    mm=M
                    if S >=60:
                        S-=60
                        M=int(M)
                        M+=1
                        M=str(M)
                        mm=M
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{mm}:{p2}")
                            # print(N)
                            return n
                        else:    
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{mm}:{ss}")
                            # print(N)
                            return n
                    else:    
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{mm}:{p2}")
                            # print(N)
                            return n
                        else:    
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{mm}:{ss}")
                            # print(N)
                            return n
        else:
            H=str(H)
            H1=H
            if M >=60:
                M-=60
                H=int(H)
                H+=1
                if H <=12:
                    H=str(H)
                    H1=H
                else:
                    H=int(H)
                    H-=12
                    H=str(H)
                    H1="0"+H
                if M < 10:
                    M=str(M)
                    p1="0"+M
                    if S >=60:
                        S-=60
                        M=int(M)
                        M+=1
                        M=str(M)
                        p1="0"+M
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{p1}:{p2}")
                            # print(N)
                            return n
                        else:    
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{p1}:{ss}")
                            # print(N)
                            return n
                    else:
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{p1}:{p2}")
                            # print(N)
                            return n 
                        else:   
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{p1}:{ss}")
                            # print(N)
                            return n        
                else:    
                    M=str(M)
                    mm=M
                    if S >=60:
                        S-=60
                        M=int(M)
                        M+=1
                        M=str(M)
                        mm=M
                        if S < 10:
                            S=str(S)
                            p="0"+S
                            n=time.strftime(f"{H1}:{mm}:{p}")
                            # print(N)
                            return n
                        else:   
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{mm}:{ss}")
                            # print(N)
                            return n 
                    else:
                        if S < 10:
                            S=str(S)
                            p="0"+S
                            n=time.strftime(f"{H1}:{mm}:{p}")
                            # print(N)
                            return n
                        else:   
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{mm}:{ss}")
                            # print(N)
                            return n   
            else:
                if M < 10:
                    M=str(M)
                    p1="0"+M
                    if S >=60:
                        S-=60
                        M=int(M)
                        M+=1
                        M=str(M)
                        p1="0"+M
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{p1}:{p2}")
                            # print(N)
                            return n
                        else:    
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{p1}:{ss}")
                            # print(N)
                            return n 
                    else:    
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{p1}:{p2}")
                            # print(N)
                            return n
                        else:
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{p1}:{ss}")
                            # print(N)
                            return n   
                else:    
                    M=str(M)
                    mm=M
                    if S >=60:
                        S-=60
                        M=int(M)
                        M+=1
                        M=str(M)
                        mm=M
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{mm}:{p2}")
                            # print(N)
                            return n
                        else:    
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{mm}:{ss}")
                            # print(N)
                            return n
                    else:    
                        if S < 10:
                            S=str(S)
                            p2="0"+S
                            n=time.strftime(f"{H1}:{mm}:{p2}")
                            # print(N)
                            return n 
                        else:    
                            S=str(S)
                            ss=S
                            n=time.strftime(f"{H1}:{mm}:{ss}")
                            # print(N)
                            return n  
# t=timer()
# print(t)
