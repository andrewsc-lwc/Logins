from tkinter import *
from tkinter import font
import csv



class MyLogin():
    def __init__(self,window,title="Login",geometry="800x800",font=("Arial",20),
                 backColour="Blue",fontColour="Black",buttonColour="Green",pwAttempts=3):
                
        self.window=window
        self.window.title(title)
        self.window.geometry(geometry)
        self.font=font
        self.window.config(bg = backColour)
        #Set the weightings of each column, 0, 1 and 2. Higher weight grows faster into space
        self.window.grid_columnconfigure(0,weight=1)
        self.window.grid_columnconfigure(1,weight=2)
        self.window.grid_columnconfigure(2,weight=1)
        #Set for the column and set a minimum size. This is so that there is a blank row at the top 
        self.window.grid_rowconfigure(0,minsize=20)
        
        self.fontColour = fontColour
        self.buttonColour = buttonColour
        self.pwAttempts = pwAttempts

        self.success = False
        self.infoText = StringVar()
        self.infoText.set("Login")
        self.uEntry = Entry(self.window,width=30,font=self.font,fg=self.fontColour)
        self.pEntry = Entry(self.window,width=30,font=self.font,fg=self.fontColour)
        self.submitButton = Button(self.window,text="Submit",command=self.login,font=self.font,
                                   bg=self.buttonColour,fg=self.fontColour)
        self.successLabel = Message(self.window,textvariable=self.infoText,font=self.font,fg=self.fontColour)

        #Sticky is where in the grid cell the widget goes. All moved down one row
        self.uEntry.grid(row=1,column=1,sticky="nsew")
        self.pEntry.grid(row=2,column=1,sticky="ew")
        self.submitButton.grid(row=3,column=1,sticky="ew")
        self.successLabel.grid(row=4,column=1,sticky="ew")
        
                

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
            self.pwAttempts -= 1#pwAttempts started from 3 so attempts remaining goes down every failed attempt
            print (self.pwAttempts,"remaining")
            self.infoText.set(("Username or Password not found you have "+str(self.pwAttempts)+" attempt(s) remaining"))
            if self.pwAttempts <= 0:#Basic if statement when attempts reaches zero, sets the infotext and destroys the window
                self.infoText.set("Number of password attempts exceeded")
                self.window.destroy()
            
        userCSV.close()
        
        

    
    
