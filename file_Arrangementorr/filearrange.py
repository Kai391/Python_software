import os
def soldier(path,files,format):
    os.chdir(path)
    File=os.listdir(path)
    l=1
    with open(files) as f:
        main=f.read().split('\n')
    for F in File:
        if F not in main:
            os.rename(F,F.capitalize())
        if f".{format}" in F:
            os.rename(F,f"{l}.{format}")
            l+=1
if __name__ == "__main__":
    p=input("enter the address of your folder: "r"")
    # enter that file which contain that data or file name that you don't want change
    fn=input("enter the main filename:" r"")
    # enter the file format like jpg, png etc. Please in lowercase 
    fmt=input("enter the format: ")
    soldier(p,fn,fmt)