from tkinter import *
import csv


import logging

logFormat = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="myLog.log",level=logging.DEBUG, format = logFormat)
logger = logging.getLogger()
logger.info("Login Program Started")


root = Tk()
root.title("Login Interface")
root.geometry("500x500")

def login():
    logger.info("Login attempted")
    userCSV = open("userandpw.csv","r",newline='')#Saved as csv MS DOS. NOT UTF8
    logger.info("Username and password database accessed")
    reader = csv.reader(userCSV)
    success = False
    for row in reader:
        if row[0]==uEntry.get():
            if row[1]==pEntry.get():
                print("Login Successful")
                success = True
                successLabel.config(text="Login Successful")
                logger.info(''.join(["User ",uEntry.get()," signed in successfully"]))
                break
            else:
                logger.warning("Incorrect Password entered")
    if success == False:
        print("Username or Password not found")
        logger.warning("Failed login attempt recorded")
        successLabel.config(text="Username or Password not found")
    userCSV.close()
    logger.info("File closed")

uEntry = Entry(root,width=30)
pEntry = Entry(root,width=30)
submitButton = Button(root,text="Submit",command=login)
successLabel = Label(root,text="Login")

uEntry.grid(row=0,column=0)
pEntry.grid(row=1,column=0)
submitButton.grid(row=2,column=0)
successLabel.grid(row=3,column=0)
