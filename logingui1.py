#This is a comment at the top
from tkinter import *

root = Tk()
root.title("Login Interface")
root.geometry("500x500")

def login():
    if uEntry.get() == "Bob" and pEntry.get() == "123":
        print("Login Successful")
    else:
        print("Username or Password incorrect")

uEntry = Entry(root,width=30)
pEntry = Entry(root,width=30)
submitButton = Button(root,text="Submit",command=login)

uEntry.grid(row=0,column=0)
pEntry.grid(row=1,column=0)
submitButton.grid(row=2,column=0)
