import tkinter
from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from aduser_rough import show_profile
 # email = aduser_rough.user()
username = show_profile()
print(username)


window = Tk()  # creating the default tkinter page

window.title("Home Page")  # title of the page

window.geometry('1200x750+50+25')  # setting the geometry of the page

window.config(bg='#fff')  # setting the background color

window.resizable(False, False)  # setting non-resizable page

frame1 = Frame(window)
frame = Frame(window)

# Create a list to hold all frames except for the main frame
frames_list = [frame1, frame]

def close_frames():
    # Destroy both frames
    frame1.destroy()
    frame.destroy()

current_frame = [frame1]

def current_close():
    frame1.destroy()


def funds():
    try:
        global frame1
        current_close()
        frame1 = LabelFrame(window, width=875, height=700, bg='black')  ### counts(cloth count)
        frame1.place(x=310, y=70)
        heading = Label(frame1, text="Fund Donation Details", fg='#57a1f8',background="white" ,font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=75, y=5)

        def get_donation_count():
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="admin",
                    database="project"
                )
                mycursor = mydb.cursor()
                ngo_name = username
                query = f"select count(*) from payment_details where ngo = '{ngo_name}'"
                mycursor.execute(query)
                count = mycursor.fetchone()[0]
                mycursor.close()
                mydb.close()
                return count
            except Exception as e:
                print('Error is in: ', e)

        count_label = Label(frame1, width=40, height=5, bg='white',text= f'{get_donation_count()} PEOPLE HAVE DONATED!!')  ### counts(cloth count)
        count_label.place(x=125, y=75)
        print("executed here")
        # Add Treeview widget
        column = (
            'Donar Name', 'Contact_No', 'Payment_mode', 'Transaction_id', 'Amount', 'Day_Time', 'NGO_Name')
        tree = ttk.Treeview(frame1,columns=column, show='headings')
        tree.heading('Donar Name', text='Donar Name')
        tree.heading('Contact_No', text='Contact_No.')
        tree.heading('Payment_mode', text='Payment_mode')
        tree.heading('Transaction_id', text='Transaction_id')
        tree.heading('Amount', text='Amount')
        tree.heading('Day_Time', text='Day_Time')
        tree.heading('NGO_Name', text='NGO_Name')

        tree.column('Donar Name', width=110)
        tree.column('Contact_No', width=105)
        tree.column('Payment_mode', width=105)
        tree.column('Transaction_id',width=110)
        tree.column('Amount', width=105)
        tree.column('Day_Time', width=125)
        tree.column('NGO_Name', width=180)
        tree.place(x=10,y=250)
        try:
            # Connect to database
            print("database block run")
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin",
                database="project"
            )
            mycursor = mydb.cursor()
            ngo_name = username
            query = 'select fullname,contact_number,payment_mode,transaction_id,amount,datetime,ngo from payment_details where ngo = %s'
            mycursor.execute(query,(ngo_name,))
            rows = mycursor.fetchall()
            # Insert data into Treeview widget
            for row in rows:
                tree.insert('', END, values=row)

            mycursor.close()
            mydb.close()

        except Exception as e:
            print('Error is in: ', e)

    except:
        messagebox.showerror("Error","Error in opening cloth donation block")

def food_donation():
    try:
        global frame1
        current_close()
        frame1 = LabelFrame(window, width=875, height=700, bg='black')  ### counts(cloth count)
        frame1.place(x=310, y=70)
        heading = Label(frame1, text="Food Donation Details", fg='#57a1f8',background='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=75, y=5)

        def get_donation_count():
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="admin",
                    database="project"
                )
                mycursor = mydb.cursor()
                ngo_name = username
                query = f"select count(*) from food_donation where ngo ='{ngo_name}'"
                mycursor.execute(query)
                count = mycursor.fetchone()[0]
                mycursor.close()
                mydb.close()
                return count
            except Exception as e:
                print('Error is in: ', e)

        count_label = Label(frame1, width=40, height=5, bg='white',text= f'{get_donation_count()} PEOPLE HAVE DONATED!!')  ### counts(cloth count)
        count_label.place(x=125, y=75)

        # Add Treeview widget
        column = (
            'Donar Name', 'Contact_No', 'Alternate No.', 'Email_id', 'Date', 'Day_Time', 'NGO_Name')
        tree = ttk.Treeview(frame1,columns=column, show='headings')
        tree.heading('Donar Name', text='Donar Name')
        tree.heading('Contact_No', text='Contact_No.')
        tree.heading('Alternate No.', text='Alternate No.')
        tree.heading('Email_id', text='Email_id')
        tree.heading('Date', text='Date')
        tree.heading('Day_Time', text='Day_Time')
        tree.heading('NGO_Name', text='NGO_Name')

        tree.column('Donar Name', width=110)
        tree.column('Contact_No', width=105)
        tree.column('Alternate No.', width=105)
        tree.column('Email_id',width=110)
        tree.column('Date', width=105)
        tree.column('Day_Time', width=125)
        tree.column('NGO_Name', width=180)
        tree.place(x=10,y=250)
        try:
            # Connect to database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin",
                database="project"
            )
            mycursor = mydb.cursor()
            ngo_name = username
            query = 'SELECT * FROM food_donation WHERE ngo=%s'
            mycursor.execute(query,(ngo_name,))
            rows = mycursor.fetchall()
            # Insert data into Treeview widget
            for row in rows:
                tree.insert('', END, values=row)

            mycursor.close()
            mydb.close()

        except Exception as e:
            print('Error is in: ', e)

    except:
        messagebox.showerror("Error","Error in opening food donation block")


def cloth_donation():
    try:
        global frame1
        current_close()
        frame1 = LabelFrame(window, width=875, height=700, bg='black')  ### counts(cloth count)
        frame1.place(x=310, y=70)
        heading = Label(frame1, text="Cloth Donation Details", fg='#57a1f8',background='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=75, y=5)

        def get_donation_count():
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="admin",
                    database="project"
                )
                mycursor = mydb.cursor()
                ngo_name = username
                query = f"select count(*) from cloth_donation where ngo ='{ngo_name}'"
                mycursor.execute(query)
                count = mycursor.fetchone()[0]
                mycursor.close()
                mydb.close()
                return count
            except Exception as e:
                print('Error is in: ', e)

        count_label = Label(frame1, width=40, height=5, bg='white',text= f'{get_donation_count()} PEOPLE HAVE DONATED!!')  ### counts(cloth count)
        count_label.place(x=125, y=75)


        # Add Treeview widget
        column = (
            'Donar Name', 'Contact_No', 'Alternate No.', 'Email_id', 'Date', 'Day_Time', 'NGO_Name')
        tree = ttk.Treeview(frame1,columns=column, show='headings')
        tree.heading('Donar Name', text='Donar Name')
        tree.heading('Contact_No', text='Contact_No.')
        tree.heading('Alternate No.', text='Alternate No.')
        tree.heading('Email_id', text='Email_id')
        tree.heading('Date', text='Date')
        tree.heading('Day_Time', text='Day_Time')
        tree.heading('NGO_Name', text='NGO_Name')

        tree.column('Donar Name', width=110)
        tree.column('Contact_No', width=105)
        tree.column('Alternate No.', width=105)
        tree.column('Email_id',width=110)
        tree.column('Date', width=105)
        tree.column('Day_Time', width=125)
        tree.column('NGO_Name', width=180)
        tree.place(x=10,y=250)
        try:
            # Connect to database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin",
                database="project"
            )
            mycursor = mydb.cursor()
            ngo_name = username
            query = 'SELECT * FROM cloth_donation WHERE ngo=%s'
            mycursor.execute(query,(ngo_name,))
            rows = mycursor.fetchall()
            # Insert data into Treeview widget
            for row in rows:
                tree.insert('', END, values=row)

            mycursor.close()
            mydb.close()

        except Exception as e:
            print('Error is in: ', e)

    except:
        messagebox.showerror("Error","Error in opening cloth donation block")


def event_organized():
    try:
        global frame1
        current_close()
        frame1 = LabelFrame(window, width=875, height=700, bg='black')
        frame1.place(x=310, y=70)
        heading = Label(frame1, text="Events Organise Details", fg='#57a1f8',background='white' ,font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=75, y=5)

        def get_donation_count():
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="admin",
                    database="project"
                )
                mycursor = mydb.cursor()
                ngo_name = username
                query = f"select count(*) from events where ngo ='{ngo_name}'"
                mycursor.execute(query)
                count = mycursor.fetchone()[0]
                mycursor.close()
                mydb.close()
                return count
            except Exception as e:
                print('Error is in: ', e)

        count_label = Label(frame1, width=40, height=5, bg='white',text= f'{get_donation_count()} PEOPLE HAVE ORGANISE THE EVENTS!!')  ### counts(cloth count)
        count_label.place(x=125, y=75)
        print("labl created")

        # Add Treeview widget
        column = (
            'EVENT_ID','Contact_no', 'Email_id', 'HEAD VOLUNTEER Name', 'Date', 'Time','Description', 'NGO_Name')
        tree = ttk.Treeview(frame1,columns=column, show='headings')
        tree.heading('EVENT_ID', text='EVENT_ID')
        tree.heading('Contact_no', text='Contact_no')
        tree.heading('Email_id', text='Email_id')
        tree.heading('HEAD VOLUNTEER Name', text='HEAD VOLUNTEER Name')
        tree.heading('Date', text='Date')
        tree.heading('Time', text='Time')
        tree.heading('Description', text='Description')
        tree.heading('NGO_Name', text='NGO_Name')
        print("heading creatd")

        tree.column('EVENT_ID', width=70)
        tree.column('Contact_no', width=100)
        tree.column('Email_id', width=100)
        tree.column('HEAD VOLUNTEER Name',width=110)
        tree.column('Date', width=70)
        tree.column('Time',width=70)
        tree.column('Description',width=195)
        tree.column('NGO_Name',width=125)
        tree.place(x=10,y=250)
        print("tree created")
        try:
            # Connect to database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin",
                database="project"
            )
            mycursor = mydb.cursor()
            ngo_name = username
            query = 'SELECT * FROM events WHERE ngo=%s'
            mycursor.execute(query,(ngo_name,))
            rows = mycursor.fetchall()
            # Insert data into Treeview widget
            for row in rows:
                tree.insert('', END, values=row)

            mycursor.close()
            mydb.close()

        except Exception as e:
            print('Error is in: ', e)

    except:
        messagebox.showerror("Error","Error in opening cloth donation block")



def admin_profile():
    import admin_usr


def index_page():
    window.destroy()
    import index_page


def show():
    global frame
    frame = Frame(window, width=300, height=700, bg='black')
    frame.place(x=0, y=70)
    fund_button = Button(frame, width=45, height=3, bg='white', fg='black', border=1,text='FUNDS',
                             cursor='hand2', font=('Microsoft YaHei UI Light', 7, 'bold'),command=funds)
    fund_button.place(x=10, y=10)

    cloth_button = Button(frame, width=45, height=3, bg='white', fg='black', border=1, text='CLOTH',
                         cursor='hand2', font=('Microsoft YaHei UI Light', 7, 'bold'),command=cloth_donation)
    cloth_button.place(x=10, y=70)

    food_button = Button(frame, width=45, height=3, bg='white', fg='black', border=1, text='FOOD',
                         cursor='hand2', font=('Microsoft YaHei UI Light', 7, 'bold'),command=food_donation)
    food_button.place(x=10, y=130)

    event_button = Button(frame, width=45, height=3, bg='white', fg='black', border=1, text='EVENTS',
                         cursor='hand2', font=('Microsoft YaHei UI Light', 7, 'bold'),command=event_organized)
    event_button.place(x=10, y=190)
    logout_button = Button(frame, width=45, height=3, bg='white', fg='black', border=1, text='LOG OUT',
                         cursor='hand2', font=('Microsoft YaHei UI Light', 7, 'bold'),command=index_page)
    logout_button.place(x=10, y=600)


    close_button = Button(frame, width=45, height=3, bg='white', fg='black', border=1, text='CLOSE',
                         cursor='hand2', font=('Microsoft YaHei UI Light', 7, 'bold'),command=close_frames)
    close_button.place(x=10, y=530)


 # creating main frame window
main = Frame(window, width=1200, height=70, bg='#ffffff')
main.place(x=0, y=0)

profile_image = Image.open("C://Users//ACER//PycharmProjects//Old_Age_Home//Image//admin_profile.png")
profile_image = profile_image.resize((80, 50))
profile_image = ImageTk.PhotoImage(profile_image)

bg_image = Image.open("C://Users//ACER//PycharmProjects//Old_Age_Home//Image//menu-bar.png")
bg_image = bg_image.resize((200, 50))
bg_image = ImageTk.PhotoImage(bg_image)

threeline_button = Button(main, width=50, height=70, pady=7,  bg='#ffffff', fg='white', border=0, image=bg_image,
                         cursor='hand2', font=('Microsoft YaHei UI Light', 7, 'bold'),command=show)
threeline_button.place(x=0, y=0)

profile_button = Button(main, width=70, height=70, pady=7,  bg='#ffffff', fg='white', border=0, image=profile_image,
                         cursor='hand2', font=('Microsoft YaHei UI Light', 7, 'bold'),command=admin_profile)
profile_button.place(x=1130, y=0)


window.mainloop()
