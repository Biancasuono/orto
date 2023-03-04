import os

def cat(fname):
    with open(fname,"r") as file:
        print(file.read())

def write_in_file(fname,text):
    with open(fname,"w") as file:
        file.write(text)

def ls():
    print(os.listdir())
