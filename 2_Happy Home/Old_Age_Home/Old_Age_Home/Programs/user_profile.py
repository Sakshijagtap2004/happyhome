from tkinter import *
from tkinter import messagebox
import pymysql
# from userprofile_rough import show_profile
root = Tk()
root.title('User Profile')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

user_email = show_profile()


def user_profile():
    try:
        con = pymysql.connect(host='localhost', user='root', password='admin', database='project')
        mycursor = con.cursor()
        print("database try block executed")
    except Exception as e:
        print('Error is in: ', e)
        messagebox.showerror('Error', 'Database connectivity issue')
        return

    query = 'SELECT * FROM signup WHERE email=%s'
    mycursor.execute(query, user_email)
    user = mycursor.fetchone()
    con.commit()
    con.close()
    print('fetchone executed')
    print(user)

    if user:
        name_label = Label(root, text="Name:" + user[0])
        name_label.place(x=200, y=225)

        email_label = Label(root, text="EmailId:" + user[1])
        email_label.place(x=200, y=275)

        phone_label = Label(root, text="Phone Number: " + user[2])
        phone_label.place(x=200, y=320)
        contact_no = user[2]
        print('contact_no:', contact_no)

    #     try:
    #         con = pymysql.connect(host='localhost', user='root', password='admin', database='project')
    #         mycursor = con.cursor()
    #         print("database try block executed")
    #     except Exception as e:
    #         print('Error is in: ', e)
    #         messagebox.showerror('Error', 'Database connectivity issue')
    #         return
    #
    #     query = 'SELECT * FROM food_donation WHERE contact=%s'
    #     mycursor.execute(query, contact_no)
    #     user1 = mycursor.fetchone()
    #     con.commit()
    #     con.close()
    #     print('fetchone executed')
    #     print(user1)
    #
    #     if user1:
    #         label = Label(text="Food Donation").place(x=200, y=350)
    # else:
    #     messagebox.showerror('Error', 'User not found')

#
# def logout():
#     # hide profile page and show login page
#     root.destroy()
#     import index_page
#
#
# logout_button = Button(root, text="Logout",command=logout)
# logout_button.place(x=150,y=215)

# name_label = Label(root, text="Name:" + user[0])
# name_label.place(x=200, y=225)
# email_label = Label(root, text="EmailId:" + user[1])
# email_label.place(x=200, y=275)
# phone_label = Label(root, text="Phone Number: " + user[2])
# phone_label.place(x=200, y=320)
#


root.mainloop()
