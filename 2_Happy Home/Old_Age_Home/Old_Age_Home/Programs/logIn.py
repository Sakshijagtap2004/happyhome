from tkinter import *
from tkinter import messagebox
import pymysql
import re

# from PIL import ImageTk

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)


def user_email():
    return user.get()


def database_connectivity(emailId, passWord):
    try:
        con = pymysql.connect(host='localhost', user='root', password='admin', database='project')
        mycursor = con.cursor()
    except:
        messagebox.showerror('Error', 'Database connectivity issue')
        return

    query = 'SELECT * FROM signup WHERE email=%s AND password=%s'
    mycursor.execute(query, (emailId, passWord))
    user = mycursor.fetchone()
    con.commit()
    con.close()

    if user:
        messagebox.showinfo('Success', 'Login is successful')
        try:
            root.destroy()
            import home_page

        except Exception as e:
            print("Error ", e)
            messagebox.showerror("Error", "Error in opening home page")
    else:
        messagebox.showerror('Error', 'Invalid email or password')



def forget_password():
    import forget_password


def hide():
    openeye.config(file='C://Users//ACER/PycharmProjects//Old_Age_Home//Image//closeeye.png')
    password.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='C://Users//ACER//PycharmProjects//Old_Age_Home//Image//openeye.png')
    password.config(show='')
    eyeButton.config(command=hide)


def signin():
    emailId = userName.get()
    passWord = password.get()

    if emailId == '' or passWord == '':
        messagebox.showerror("Error","All field are requried")
        return
    pattern1 = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if not pattern1.match(emailId):
        messagebox.showerror("Error", "Enter correct emailid")
        return
    pattern2 = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+~\-={}[\]:;"\'<>,.?\\/]).{8,}$')
    if not pattern2.match(passWord):
        messagebox.showerror("Error",
                             "Enter Minimum 8 characters Password, Password Must be Alphanumeric, Password Must contain special characters")
        return
    else:
        database_connectivity(emailId, passWord)


img = PhotoImage(file='C://Users//ACER//PycharmProjects//Old_Age_Home//Image//login_img.png')
Label(root, image=img, bg='white').place(x=0,y=0)


frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=260, y=70)
heading = Label(frame, text='LOGIN', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=120, y=30)


def on_enter(e):
    userName.delete(0, 'end')


def on_leave(e):
    name = userName.get()
    if name == '':
        userName.insert(0, 'EmailID')

user = StringVar()
userName = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11),textvariable=user)
userName.place(x=30, y=80)
userName.insert(0, 'EmailID')
userName.bind('<FocusIn>', on_enter)
userName.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)


def on_enter(e):
    password.delete(0, 'end')


def on_leave(e):
    name = password.get()
    if name == '':
        password.insert(0, 'Password')


password = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
password.place(x=30, y=150)
password.insert(0, 'Password')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

openeye = PhotoImage(file='C://Users//ACER//PycharmProjects//Old_Age_Home//Image//openeye.png')
eyeButton = Button(frame, image=openeye, bd=0, bg='White', activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=275, y=145)

forgetPassword = Button(frame, text="Forgot Password?", fg="#57a1f8", bg='white', font=('Microsoft YaHei UI Light', 9),
                        bd=0, cursor='hand2', command=forget_password)
forgetPassword.place(x=35, y=245)

remember_me = Checkbutton(frame, text="Remember Me", fg="#57a1f8", bg='white', font=('Microsoft YaHei UI Light', 9),
                     bd=0, cursor='hand2')
remember_me.place(x=210, y=245)


# signin button
signIn = Button(frame, width=39, pady=7, text='Sign in', bg="#57a1f8", fg='white', border=0, command=signin)
signIn.place(x=35, y=204)


root.mainloop()

