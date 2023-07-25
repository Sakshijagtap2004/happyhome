import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import re
root = Tk()
root.geometry("925x500+300+200")
root.title("Registration Form")
root.configure(bg="#fff")
root.resizable(False, False)

def login():
    root.destroy()
    import logIn

def submit_data():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    contact = contact_entry.get()

    if email == '' or password == '' or contact == 0 or name == '':
        messagebox.showerror("Error","All field are requried")
        return
    if not name.isprintable():
        messagebox.showerror("Error", "Invalid Name Entry")
        return
    pattern = re.compile(r'^\+(?:[0-9]){1,3}(?:[\s\-\.])?(?:[(]{1}[0-9]{1,6}[)])?[\s\-\.]?[0-9]{3,12}$')
    if not pattern.match(contact):
        messagebox.showerror("Error", "Invalid, Contact Number must be with country code or must be numeric only")
        return
    pattern1= re.compile (r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if not pattern1.match(email):
        messagebox.showerror("Error","Enter correct emailid")
        return
    pattern2 = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+~\-={}[\]:;"\'<>,.?\\/]).{8,}$')
    if not pattern2.match(password):
        messagebox.showerror("Error","Enter Minimum 8 characters Password, Password Must be Alphanumeric, Password Must contain special characters")
        return
    database_connectivity(name, email, contact, password)


def database_connectivity(name,email,contact,password):
    # Connect to database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="project"
    )
    cursor = db.cursor()
    sql = "INSERT INTO signup (username, email, contact_no, password) VALUES (%s, %s, %s, %s)"
    val = (name, email, contact, password)
    cursor.execute(sql, val)
    db.commit()
    db.close()
    messagebox.showinfo("Success", "Your data has been registered successfully!")
    try:
        root.destroy()
        import logIn
    except:
        messagebox.showerror("Error","Error")

bg_image = Image.open("C://Users//ACER//PycharmProjects//Old_Age_Home//Image//signup_bg.png")
bg_image = bg_image.resize((925, 500))
bg_image = ImageTk.PhotoImage(bg_image)


bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


name_label =  Label(root, text="Name:", font=("Helvetica", 20))
name_label.place(x=100, y=150)

email_label = Label(root, text="Email" ,font=("Helvetica", 20))
email_label.place(x=100, y=200)

password_label = Label(root, text="Password", font=("Helvetica", 20))
password_label.place(x=100, y=250)

contact_label = Label(root, text="Contact", font=("Helvetica", 20))
contact_label.place(x=100, y=300)

name_entry = Entry(root, width=25)
name_entry.place(x=250, y=155)

email_entry = Entry(root, width=25)
email_entry.place(x=250, y=205)

password_entry = Entry(root, show="*", width=25)
password_entry.place(x=250, y=255)

contact_entry = Entry(root, width=25)
contact_entry.place(x=250, y=305)


submit_button = Button(root, text="Register", command=submit_data, width=20, height=2)
submit_button.place(x=200, y=380)

login_button = Button(root, text="Already Have An Account? Login Now!!", command=login, width=35, height=2)
login_button.place(x=150, y=430)


root.mainloop()