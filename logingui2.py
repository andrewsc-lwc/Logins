from tkinter import *
import csv

root = Tk()
root.title("Login Interface")
root.geometry("500x500")

def login():
    userCSV = open("userandpw.csv","r",newline='')
    reader = csv.reader(userCSV)
    success = False
    for row in reader:
        if row[0]==uEntry.get():
            if row[1]==pEntry.get():
                print("Login Successful")
                success = True
                successLabel.config(text="Login Successful")
                break
            else:
                pass
    if success == False:
        print("Username or Password not found")
        successLabel.config(text="Username or Password not found")
    userCSV.close()

uEntry = Entry(root,width=30)
pEntry = Entry(root,width=30)
submitButton = Button(root,text="Submit",command=login)
successLabel = Label(root,text="Login")

uEntry.grid(row=0,column=0)
pEntry.grid(row=1,column=0)
submitButton.grid(row=2,column=0)
successLabel.grid(row=3,column=0)
