from tkinter import *
app = Tk()
app.title("Login Page")
app.geometry("500x500")
# GUI
### Input
## Name
nplbl = Label(app,text="Name: ")
nplbl.place(relx=0.4,rely=0.1,anchor=CENTER)

ntry = Entry(app)
ntry.place(relx=0.5,rely=0.1,anchor=W)
## Password
plbl = Label(app,text="Password: ")
plbl.place(relx=0.4,rely=0.2,anchor=CENTER)

ptry = Entry(app)
ptry.place(relx=0.5,rely=0.2,anchor=W)
## Captcha
cplbl = Label(app,text="Captcha: ")
cplbl.place(relx=0.4,rely=0.3,anchor=CENTER)

ctry = Entry(app)
ctry.place(relx=0.5,rely=0.3,anchor=W)
### Output
## Name
dnlbl = Label(app)
dnlbl.place(relx=0.5,rely=0.6,anchor=CENTER)
## Password
dplbl = Label(app)
dplbl.place(relx=0.5,rely=0.7,anchor=CENTER)
## Captcha
dclbl = Label(app)
dclbl.place(relx=0.5,rely=0.8,anchor=CENTER)
# Class
class userDB():
    def __init__(self):
        self.__username = "User"
        self.__password = "User25$"
        self.__captcha = "jksha"
    def showUser(self):
        dnlbl['text'] = "Name: " + self.__username
        dplbl['text'] = "Password: " + self.__password
        dclbl['text'] = "Captcha: " + self.__captcha
objclass = userDB()
def addUser():
    global objclass
    objclass.username = ntry.get()
    objclass.password = ptry.get()
    objclass.captcha = ctry.get()
    print("Updated!: "+objclass.username+ " " +objclass.password + " " +objclass.captcha)
btn = Button(app,text="Update Login Details",command=addUser)
btn.place(relx=0.2,rely=0.5)
btn1 = Button(app,text="Show Profile",command=objclass.showUser)
btn1.place(relx=0.5,rely=0.5)
app.mainloop()