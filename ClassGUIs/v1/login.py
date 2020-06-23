import csv
from tkinter import *
##window=Tk()

class MyLogin():
    def __init__(self,window):
                
        self.window=window
        
        self.success = False
        self.infoText = StringVar()
        self.infoText.set("Login")

        self.uEntry = Entry(self.window,width=30)
        self.pEntry = Entry(self.window,width=30)
        self.submitButton = Button(self.window,text="Submit",command=self.login)
        self.successLabel = Label(self.window,textvariable=self.infoText)

        self.uEntry.grid(row=0,column=0)
        self.pEntry.grid(row=1,column=0)
        self.submitButton.grid(row=2,column=0)
        self.successLabel.grid(row=3,column=0)
        

    def login(self):
        userCSV = open("userandpw.csv","r",newline='')
        reader = csv.reader(userCSV)
        
        for row in reader:
            if row[0]==self.uEntry.get():
                if row[1]==self.pEntry.get():
                    print("Login Successful")
                    self.success= True
                    self.infoText.set("Login Successful")
                    self.window.destroy()
                    break
                else:
                    pass
        if self.success == False:
            print("Username or Password not found")
            self.infoText.set("Username or Password not found")
        userCSV.close()
        
        
##login = MyLogin(window)
    
    
