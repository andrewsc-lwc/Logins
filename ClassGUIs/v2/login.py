from tkinter import *
from tkinter import font
import csv



class MyLogin():
    def __init__(self,window,title="Login",geometry="800x800",font=("Arial",20),backColour="Blue",fontColour="Black",buttonColour="Green",pwAttempts=3):
                
        self.window=window
        
        self.window.title(title)
        self.window.geometry(geometry)
        self.font=font
        self.window.config(bg = backColour)
        self.fontColour = fontColour
        self.buttonColour = buttonColour

        self.success = False
        self.infoText = StringVar()
        self.infoText.set("Login")
        self.uEntry = Entry(self.window,width=30,font=self.font,fg=self.fontColour)
        self.pEntry = Entry(self.window,width=30,font=self.font,fg=self.fontColour)
        self.submitButton = Button(self.window,text="Submit",command=self.login,font=self.font,bg=self.buttonColour,fg=self.fontColour)
        self.successLabel = Label(self.window,textvariable=self.infoText,font=self.font,fg=self.fontColour)

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
        
        

    
    
