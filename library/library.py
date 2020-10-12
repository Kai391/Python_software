"""
This contains two Library which contain one class.
After some time I will link it as a backend in website.
"""
class library:
    def __init__(self,listbooks,name):
    # this is the constructor which made one object when call.
        self.l=listbooks
        self.name=name
        self.dic={}
    def displaybook(self):
        # this is the method to display books in library.
        print("\n")
        for i in self.l:
            print(i)
        print("\n")
    def lendbook(self,book):
        # this is the method for lend books.
        l=self.l.count(book)
        # count will gives output as 1 for true or 0 for false.
        if l == 1: 
            if book not in self.dic.keys() :
                # check keys(books) in dictionary.
                name=input('Enter your name: ')
                self.dic.update({book:name})
                # print(self.dic)
                print("conragulation you got book\n\n\n")
            else:
                print(f'sorry the book is alreay taken by {self.dic[book]} \n\n\n') 
        else:
            print("\n\t\t\t\tSorry we don't have that book.\n")  
    def addbook(self,book):
        # this is the method for add books. 
        self.l.append(book)
        print("congratulation we added your new book to our database.\n\n\n")
        # print(self.l)
    def returnbook(self,book):
        # this is the method for return books.
        del self.dic[book]
        print("Thankyou for returning book. We hope you coming soon.\n\n\n")
if __name__ == "__main__":
    print("\n\t\t\t\tChoose Your Library:")
    print("Enter 1 for Krishna's Library")
    print("Enter 2 for Ayushi's Library")
    i=int(input())
    if i == 1:
        # krishna is one object
        krishna=library(['python','C++','node'] ,"Krishna's Library")
        print(f"\n\t\t\t\tWelcome to {krishna.name}\n")
        while(True):
            print("Enter 1 for display books,")
            print("Enter 2 for lend book")
            print("enter 3 for Donate or add book, ")
            print("enter 4 for return book")
            print("Enter 5 for exit")
            try:
                p= int(input())
                if p == 1:
                    krishna.displaybook()
                elif p == 2:
                    b=input("enter book name: ")
                    krishna.lendbook(b)
                elif p == 3:
                    b=input("upload your book: ")
                    krishna.addbook(b)
                elif p == 4:
                    r=input("Name of book you return: ")
                    krishna.returnbook(r)
                elif p == 5:
                    break
                else:
                    print("\n\n\t\t\t\tYou type invalid no.\n\n")
            except:
                print("\n\n\t\t\t\tYou type invalid character\n\n")
    elif i == 2:
        # ayushi is second object.
        ayushi=library(['Java','HTML Basics','CSS Endless'],"Ayushi's Library")
        print(f"\n\t\t\t\tWelcome to {ayushi.name}\n")      
        while(True):
            print("Enter 1 for display books,")
            print("Enter 2 for lend book")
            print("enter 3 for Donate or add book, ")
            print("enter 4 for return book")
            print("Enter 5 for exit")
            try:
                a= int(input())
                if a == 1:
                    ayushi.displaybook()
                elif a == 2:
                    c=input("enter book name: ")
                    ayushi.lendbook(c)
                elif a == 3:
                    c=input("upload your book: ")
                    ayushi.addbook(c)
                elif a == 4:
                    d=input("Name of book you return: ")
                    ayushi.returnbook(d)
                elif a == 5:
                    break
                else:
                    print("\n\n\t\t\t\tYou type invalid no.\n\n")
            except:
                print("\n\n\t\t\t\tYou type invalid character\n\n")
                
