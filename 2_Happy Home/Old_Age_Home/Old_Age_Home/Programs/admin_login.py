from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
import re

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

def name():
    return new.get()


def database_connectivity(name,email,password):
    # Connect to database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="project"
    )
    cursor = db.cursor()
    sql = 'SELECT * FROM admin_login WHERE email=%s AND pass_word=%s AND ngo_name=%s'
    cursor.execute(sql, (email, password, name))
    result = cursor.fetchone()  # fetch the result set
    db.commit()
    db.close()
    if result is not None:
        messagebox.showinfo("Success", "Admin Login Successful!")
        root.destroy()
        import admin_dahboard
    else:
        messagebox.showerror("Error", "Invalid email or password")
    return name



def submit_data():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if email == '' or password == '' or name == '':
        messagebox.showerror("Error","All field are requried")
        return
    if not name.isprintable():
        messagebox.showerror("Error", "Invalid Name Entry")
        return
    pattern1 = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if not pattern1.match(email):
        messagebox.showerror("Error", "Enter correct emailid")
        return
    pattern2 = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+~\-={}[\]:;"\'<>,.?\\/]).{8,}$')
    if not pattern2.match(password):
        messagebox.showerror("Error",
                             "Enter Minimum 8 characters Password, Password Must be Alphanumeric, Password Must contain special characters")
        return
    database_connectivity(name,email,password)


bg_image = Image.open("C://Users//ACER//PycharmProjects//Old_Age_Home//Image//admin_login.png")
bg_image = bg_image.resize((925, 500))
bg_image = ImageTk.PhotoImage(bg_image)

bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

heading = Label(root, text='ADMIN LOGIN', fg='#c515d0', bg='#36136f', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=120, y=30)

name_label =  Label(root, text="Ngo Name: ",fg = '#dc73e3',bg = '#501aa4',font=("Helvetica", 15))
name_label.place(x=100, y=150)


email_label = Label(root, fg='#dc73e3',bg='#501aa4',font=("Helvetica", 15),text='NGO EMAILId: ')
email_label.place(x=100, y=200)

password_label = Label(root, text="Password: ", fg ='#dc73e3',bg = '#501aa4',font=("Helvetica", 15))
password_label.place(x=100, y=250)

new = StringVar()
name_entry = Entry(root, width=40,textvariable=new)
name_entry.place(x=250, y=155)

email_entry = Entry(root, width=40)
email_entry.place(x=250, y=205)

password_entry = Entry(root, show="*", width=25)
password_entry.place(x=250, y=255)

submit_button = Button(root, text="Submit", command=submit_data, width=20, height=2,bg='#27042a',fg='#c515d0')
submit_button.place(x=200, y=380)

root.mainloop()