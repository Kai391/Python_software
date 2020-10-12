import datetime
while(True):
    def date_time():
        d= datetime.datetime.now()
        return d
    print("enter 1 for registration, enter 2 for edit file, 3 for show list, 4 for exit: ",end="")
    try:
        n=int(input())
        if n == 1:
            File = input("enter the name: ")
            f= open("{}_food.txt".format(File), "w")
            e = open("{}_excersice.txt".format(File),"w")
            List= open("List.txt","a")
            List.write("{}\n".format(File))
            List.close()
            con1 = f.write("Food diet of {}\nItem\t\t\tTime\t\t\t\t\t\t\t\t\t\t\t\tQuantity\n".format(File))
            con2 = e.write("Excersice planning for {}\nWorkout Name\t\t\tTime\t\t\t\t\t\t\t\tTimeDuration\n".format(File))
            print(con1,con2)
            f.close()
            e.close()

        elif n == 2:
            while(True):
                print("enetr 1 for food diet, enter 2 for excersice, 3 for exit: ",end="")
                try:
                    n=int(input())
                    if n == 1:
                        print("Food Diet")
                        name=input("Pls tell your name that you register first: ")
                        while(True):
                            try:
                                Open = open("{}_food.txt".format(name),"r")
                                Open.close()
                                break
                            except:
                                print("name doesn't exit")
                                name=input("Pls tell your name that you register first: ")
                        Open = open("{}_food.txt".format(name),"a")
                        i=input("Item: ")
                        q=input("Qunatity: ")
                        t=date_time()
                        Open.write("{}\t\t\t".format(i))
                        Open.write("{}\t\t\t\t\t\t".format(t))
                        Open.write("{}\n".format(q))
                        Open.close()
                        Open = open("{}_food.txt".format(name),"r")
                        r=Open.read()
                        print(r)
                        Open.close()
                        break
                    elif n == 2:
                        print("Excersice Plan")
                        name=input("Pls tell your name that you register first: ")
                        while(True):
                            try:
                                Open = open("{}_excersice.txt".format(name),"r")
                                Open.close()
                                break
                            except:
                                print("name doesn't exit")
                                name=input("Pls tell your name that you register first: ")
                        Open = open("{}_excersice.txt".format(name),"a")
                        w=input("workout Name: ")
                        td=input("TimeDuration: ")
                        t=date_time()
                        Open.write("{}\t\t\t".format(w))
                        Open.write("{}\t\t\t\t\t\t".format(t))
                        Open.write("{}\n".format(td))
                        Open.close()
                        Open = open("{}_excersice.txt".format(name),"r")
                        r=Open.read()
                        print(r)
                        Open.close()
                        break
                    elif n == 3:
                        break
                except:
                    print("invalid No.")
        elif n == 3:
            Open = open("List.txt","r")
            print(Open.read())
        elif n == 4:
            break
    except:
        print('invalid No.')