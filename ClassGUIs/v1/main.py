from login import MyLogin
from tkinter import *

root=Tk()
root.geometry("300x300")
root.title("Menu")

def login():
    loginSuccess.config(text="Login Pending")
    loginButton.config(state="disabled")
    f = Toplevel()
    login1 = MyLogin(f)
    root.wait_window(f)
    loginButton.config(state="normal")
    loginSuccess.config(text=login1.infoText.get())
    
loginButton = Button(root,text="Login",command=login)
loginButton.grid()
loginSuccess = Label(root,text="")
loginSuccess.grid()

root.mainloop()

