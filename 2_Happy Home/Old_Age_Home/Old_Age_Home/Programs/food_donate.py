from tkinter import *
import tkinter.messagebox
import mysql.connector

# Connect to database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="project"
)

root = Tk()
root.title('food donation')
root.geometry('925x500+300+200')
root.configure(bg="#78b3d0")
root.resizable(False, False)


# Function to handle form submission
def onClick():
    # Get form data
    name = entry.get()
    contact = entry_2.get()
    alt_contact = entry_3.get()
    email = entry_1.get()
    date = date_menu.get() + '-' + month_menu.get() + '-' + entry_4.get()
    time_slot = time_menu.get()
    ngo = selected_option.get()

    # Insert data into database
    mycursor = mydb.cursor()
    sql = "INSERT INTO food_donation (name, contact, alt_contact, email, slot_date, time_slot, ngo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (name, contact, alt_contact, email, date, time_slot, ngo)
    mycursor.execute(sql, val)
    mydb.commit()

    tkinter.messagebox.showinfo("SUCCESS","Successfully form submitted!")


frame = Frame(root, width=600, height=400, bg="#78b3d0")
frame.place(x=300, y=70)
heading = Label(frame, text='FOOD DONATION', fg='#160c17', bg='#78b3d0', font=("Helvetica", 23, 'bold'))
heading.place(x=50, y=5)
#name

entry = Entry(frame,width=35,border=3)
entry.place(x=120, y=90)
labl_2 = Label(frame, text="NAME", width=10, font=("bold", 10))
labl_2.place(x=30, y=90)
#contact
entry_2 = Entry(frame,width=15,border=3)
entry_2.place(x=200, y=130)

labl_2= Label(frame, text="CONTACT NUMBER", width=20, font=("bold", 10))
labl_2.place(x=30, y=130)
#alternate contact
entry_3 = Entry(frame,width=15,border=3)
entry_3.place(x=200, y=170)
labl_2 = Label(frame, text="ALTERNATE NUMBER", width=20, font=("bold", 10))
labl_2.place(x=30, y=170)
#enail
entry_1 = Entry(frame,width=35,border=3)
entry_1.place(x=120, y=210)
labl_2 = Label(frame, text="EMAIL", width=10, font=("bold", 10))
labl_2.place(x=30, y=210)
#date
entry_4 = Entry(frame,width=10,border=5)
entry_4.place(x=305, y=247)
date_menu= StringVar(root)
date_menu.set("DAY")
date_opotions = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
month_menu= StringVar(root)
month_menu.set("MONTH")
month_options = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
#Create a dropdown Menu
date_drop= OptionMenu(root,date_menu,*date_opotions)
date_drop.place(x=430,y=315)

month_drop= OptionMenu(root,month_menu,*month_options)
month_drop.place(x=510,y=315)

labl_2 = Label(frame, text="DATE", width=10, font=("bold", 10))
labl_2.place(x=30, y=250)

#sloat
time_menu= StringVar(root)
time_menu.set("SELECT TIME SLOT")
time_options = ["MONDAY: 10-12am", "WEDNESDAY: 3-5pm","FRIDAY: 7-9pm"]
#Create a dropdown Menu

drop= OptionMenu(root,time_menu,*time_options)
drop.place(x=330,y=350)

#select ngo
# menu_NGO= StringVar()
# menu_NGO.set("SELECT THE NGO")

#Create a dropdown Menu
# drop_NGO= OptionMenu(root ,menu_NGO,"LITTLE SISTERS OF THE POOR", "AAIJIDEVI CARE FOUNDATION","ST. ANTHONYS HOME FOR THE AGED")
# drop_NGO.place(x=500,y=350)
options_NGO = ["LITTLE SISTERS OF THE POOR", "AAIJIDEVI CARE FOUNDATION","ST. ANTHONYS HOME FOR THE AGED"]
selected_option = StringVar(root)
selected_option.set("SELECT THE NGO")
drop_NGO= OptionMenu(root,selected_option, *options_NGO)
drop_NGO.place(x=500,y=350)

sign_up = Button(frame, width=10, text='BOOK', border=8, bg="white", cursor="hand2", fg="#57a1f8",command=onClick)
sign_up.place(x=150, y=320)
root.mainloop()