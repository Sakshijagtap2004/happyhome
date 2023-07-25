import decimal
from tkinter import *
from userprofile_rough import show_profile
from tkinter import messagebox
import pymysql
from datetime import datetime
root = Tk()
root.title('User Profile')
root.geometry('700x400+500+200')
root.configure(bg="#fff")
root.resizable(False, False)

username = show_profile()
# Label(root, text=username,font=('Microsoft YaHei UI Light', 20, 'bold')).place(x=200,y=200)


def user_profile():
    try:
        try:
            con = pymysql.connect(host='localhost', user='root', password='admin', database='project')
            mycursor = con.cursor()
            print("database try block executed")
        except Exception as e:
            print('Error is in: ', e)
            messagebox.showerror('Error', 'Database connectivity issue')
            return
        query = 'SELECT * FROM signup WHERE email=%s'
        mycursor.execute(query, username)
        user = mycursor.fetchone()
        con.commit()
        con.close()
        print('fetchone executed')
        print(user)
        if user:
            heading = Label(root, text='User Profile', fg='#160c17', bg="#ffffff", font=("Helvetica", 18, 'bold'))
            heading.place(x=300, y=0)
            label = Label(root, background="white", text="Personal Details")
            label.place(x=40, y=25)
            name_label = Label(root,background="white", text="Name:  " + user[0])
            name_label.place(x=40, y=50)
            email_label = Label(root,background="white", text="EmailId:  " + user[1])
            email_label.place(x=40, y=75)
            contact_no = user[2]
            phone_label = Label(root,background="white", text="Phone Number:  " + contact_no)
            phone_label.place(x=40, y=90)
            print(contact_no)

            try:
                con = pymysql.connect(host='localhost', user='root', password='admin', database='project')
                mycursor = con.cursor()
                print("database try block executed")
            except Exception as e:
                print('Error is in: ', e)
                messagebox.showerror('Error', 'Database connectivity issue')
                return

            query = 'SELECT * FROM food_donation WHERE contact=%s'
            mycursor.execute(query, contact_no)
            user1 = mycursor.fetchone()
            con.commit()
            con.close()
            print('fetchone executed')
            print(user1)
            if user1:
                heading_label = Label(root, text='Food Donation', fg='#160c17', bg="#ffffff", font=("Helvetica", 10, 'bold'))
                heading_label.place(x=350, y=35)
                name_label = Label(root, background="white", text="Name:  " + user1[0])
                name_label.place(x=350, y=60)
                contact_label = Label(root, background="white", text="Contact Number:  " + user1[1])
                contact_label.place(x=350, y=85)
                alternate_label = Label(root, background="white", text="Alternate Number:  " + user1[2])
                alternate_label.place(x=350, y=110)
                email_label = Label(root, background="white", text="Email Id:  " + user1[3])
                email_label.place(x=350, y=135)
                date_time = Label(root, background="white", text="Date:  " + user1[4] + "Time: " + user1[5])
                date_time.place(x=350, y=160)
                ngo_label = Label(root, background="white", text="NGO Selected: " + user1[6])
                ngo_label.place(x=350,y=185)
            else:
                Label(root, text="User has not donated food yet!!").place(x=350, y=250)


            try:
                con = pymysql.connect(host='localhost', user='root', password='admin', database='project')
                mycursor = con.cursor()
                print("database try block executed")
            except Exception as e:
                print('Error is in: ', e)
                messagebox.showerror('Error', 'Database connectivity issue')
                return

            query = 'select fullname,contact_number,payment_mode,transaction_id,amount,datetime,ngo from payment_details where contact_number = %s'
            mycursor.execute(query, contact_no)
            user2 = mycursor.fetchone()
            con.commit()
            con.close()
            print('fetchone executed')
            print(user2)

            if user2:
                heading_label = Label(root, text='Fund Donated', fg='#160c17', bg="#ffffff",
                                      font=("Helvetica", 10, 'bold'))
                heading_label.place(x=50, y=175)
                name_label = Label(root, background="white", text="Name:  " + user2[0])
                name_label.place(x=40, y=200)
                contact_label = Label(root, background="white", text="Contact Number:  " + user2[1])
                contact_label.place(x=40, y=225)
                alternate_label = Label(root, background="white", text="Payment Mode:  " + user2[2])
                alternate_label.place(x=40, y=250)
                email_label = Label(root, background="white", text="Transaction Id:  " + user2[3])
                email_label.place(x=40, y=275)
                ngo_label = Label(root, background="white", text="Transaction Id:  " + user2[6])
                ngo_label.place(x=40,y=300)

                date_time = Label(root, background="white", text="Amount:  " + str(user2[4]))
                date_time.place(x=40, y=325)

                date = user2[5].strftime('%Y-%m-%d %H:%M:%S')
                time_label = Label(root, background="white", text="Date and Time: " + date)
                time_label.place(x=40, y=350)

            else:
                Label(root, text="User has not donated fund yet!!").place(x=350, y=250)


            try:
                con = pymysql.connect(host='localhost', user='root', password='admin', database='project')
                mycursor = con.cursor()
                print("database try block executed")
            except Exception as e:
                print('Error is in: ', e)
                messagebox.showerror('Error', 'Database connectivity issue')
                return

            query = 'SELECT * FROM cloth_donation WHERE contact=%s'
            mycursor.execute(query, contact_no)
            user1 = mycursor.fetchone()
            con.commit()
            con.close()
            print('fetchone executed')
            print(user1)
            if user1:
                heading_label = Label(root, text='Cloth Donation', fg='#160c17', bg="#ffffff", font=("Helvetica", 10, 'bold'))
                heading_label.place(x=350, y=210)
                name_label = Label(root, background="white", text="Name:  " + user1[0])
                name_label.place(x=350, y=235)
                contact_label = Label(root, background="white", text="Contact Number:  " + user1[1])
                contact_label.place(x=350, y=260)
                alternate_label = Label(root, background="white", text="Alternate Number:  " + user1[2])
                alternate_label.place(x=350, y=285)
                email_label = Label(root, background="white", text="Email Id:  " + user1[3])
                email_label.place(x=350, y=310)
                date_time = Label(root, background="white", text="Date:  " + user1[4] + "Time: " + user1[5])
                date_time.place(x=350, y=335)
                ngo_label = Label(root, background="white", text="NGO Selected: " + user1[6])
                ngo_label.place(x=350,y=360)
            else:
                Label(root,text="User has not donated clothes yet!!").place(x=350,y=250)
        else:
            messagebox.showerror('Error', 'User not found')
    except:
        messagebox.showerror("Error","User not found")


user_profile()
root.mainloop()