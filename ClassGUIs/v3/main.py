from login import MyLogin
from tkinter import *
from tkinter import font

root=Tk()
root.geometry("300x300")
root.title("Menu")
myFont = font.Font(family="Comic Sans MS",size=22,weight="bold",slant="italic")
backColour = "Green"
fontColour = "Black"
buttonColour = "Red"
pwAttempts = 3

def login():
    loginSuccess.config(text="Login Pending")
    loginButton.config(state="disabled")
    f = Toplevel()
    login1 = MyLogin(f,title="Login",geometry="800x800",backColour=backColour,
                     font=myFont,pwAttempts=pwAttempts,fontColour=fontColour,buttonColour=buttonColour)
    root.wait_window(f)
    loginButton.config(state="normal")
    loginSuccess.config(text=login1.infoText.get())
    
loginButton = Button(root,text="Login",command=login,font=myFont,fg=fontColour,bg=buttonColour)
loginButton.grid()
loginSuccess = Label(root,text="")
loginSuccess.grid()

root.mainloop()

