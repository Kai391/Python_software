"""
This contains two Library which contain one class.
After some time I will link it as a backend in website.
"""
class library:
    def __init__(self,dictbooks1,dictbooks2,name):
    # this is the constructor which made one object when call.
        self.l=dictbooks1
        self.name=name
        self.dic=dictbooks2
        self.d=[]
    def displaybook(self):
        # this is the method to display books in library.
        print("\n")
        for i in self.l.keys():
            print(i)
        print("\n")
    def display_no_of_book(self,book):
        print("\n\n"+book,end=": ")
        print(self.l[book],"\n\n")
    def no_of_book(self):
        print("\n\n")
        for books in self.dic:
            # print(books+":\t",self.dic[books])
            print(books+":",end="")
            print("\t\t\t\t\t",self.dic[books])
        print('\n\n')
    def lendbook(self,book):
        # this is the method for lend books.
        if book in self.l.keys() :
            # check keys(books) in dictionary.
            t=self.l[book]
            if self.l[book] > 0:
                name=input('Enter your name: ')
                t-=1
                self.l.update({book:t})
                # print(self.l)
                # print(self.dic)
                self.d.append(f'{book}:{name}')
                # def personowned(self):
                #     print(self.d)
                print("\n\t\t\t\tConragulation you got book\n\n\n")
            else:
                print('\n\t\t\t\tSorry the book is out off stock\n\n\n') 
        else:
            print("\n\t\t\t\tSorry we don't have that book.\n")  
    def addbook(self,book,no):
        # this is the method for add books. 
        self.l.update({book:no})
        self.dic.update({book:no})
        print("congratulation we added your new book to our database.\n\n\n")
        # print(self.l)
    def returnbook(self,book):
        # this is the method for return books.
        if book in self.l.keys():
            t=self.l[book]
            n=input('Enter your name: ')
            # print(t)
            # print(self.dic[book])
            if self.l[book] < self.dic[book]:
                t+=1
                self.l.update({book:t})
                # print(self.l)
                print("\n\t\t\t\tThankyou for returning book. We hope you coming soon.\n\n\n")
                self.d.remove(f"{book}:{n}")
            else:
                print("\n\t\t\t\tWe have limited books, that is not mine\n\n\n")
        else:
            print("\n\t\t\t\tThat book is not belonds to our library.\n\n\n")
    def personowned(self):
        print("\n\n",self.d,"\n\n")
if __name__ == "__main__":
    krishna=library({'Python':2,'C++':3,'Node':4},{'Python':2,'C++':3,'Node':4},"Krishna's Library")
    print(f"\n\t\t\t\tWelcome to {krishna.name}\n")
    while(True):
        print("Enter 1 for display books,")
        print("enter 2 for to see how many no. of that books are available")
        print("Enter 3 for lend book")
        print("enter 4 for return book")
        print("enter 5 for Donate or add book, ")
        print("Enter 6 for exit")
        try:
            p= int(input())
            if p == 1:
                krishna.displaybook()
            elif p == 3:
                b=input("enter book name: ")
                krishna.lendbook(b)
            elif p == 5:
                b=input("upload your book: ")
                s=int(input("no of: "))
                krishna.addbook(b,s)
            elif p == 4:
                r=input("Name of book you return: ")
                krishna.returnbook(r)
            elif p == 6:
                break
            elif p == 2:
                b=input("enter book name: ")
                krishna.display_no_of_book(b)
            elif p == 7:
                krishna.personowned()
            elif p == 8:
                krishna.no_of_book()
            else:   
                print("\n\n\t\t\t\tYou type invalid no.\n\n")
        except:
            print("\n\n\t\t\t\tYou type invalid character\n\n")
    