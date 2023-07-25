from tkinter import *
from aduser_rough import show_profile
import pymysql
from tkinter import messagebox
root = Tk()
root.title('User Profile')
root.geometry('500x400+500+200')
root.configure(bg="#fff")
root.resizable(False, False)

# email = aduser_rough.user()
username = show_profile()
print(username)


def user_profile():
    try:
        con = pymysql.connect(host='localhost', user='root', password='admin', database='project')
        mycursor = con.cursor()
        print("database try block executed")
    except Exception as e:
        print('Error is in: ', e)
        messagebox.showerror('Error', 'Database connectivity issue')
        return

    query = 'SELECT * FROM admin_login WHERE ngo_name=%s'
    mycursor.execute(query, username)
    user = mycursor.fetchone()
    con.commit()
    con.close()
    print('fetchone executed')
    print(user)

    if user:
        heading = Label(root, text='Admin Profile', fg='#160c17', bg="#ffffff", font=("Helvetica", 23, 'bold'))
        heading.place(x=120, y=10)

        # ngo_name = get_ngo_name(user)
        # print(ngo_name)
        name_label = Label(root,background="white", text="Name:  " + user[0])
        name_label.place(x=100, y=75)

        email_label = Label(root,background="white", text="EmailId:  " + user[1])
        email_label.place(x=100, y=105)

        address_label = Label(root,background="white",wraplength=300, text="Address:  " + user[3])
        address_label.place(x=100, y=135)


    else:
        messagebox.showerror('Error', 'User not found')




c = user_profile()

root.mainloop()