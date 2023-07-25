from tkinter import *
import tkinter.messagebox
import mysql.connector

root = Tk()
root.title('Event')
root.geometry('925x500+300+200')
root.configure(bg="#e59ff0")
root.resizable(False, False)


frame = Frame(root, width=600, height=550, bg="#e59ff0")
frame.place(x=250, y=1)
heading = Label(frame, text='Organized Events', fg='#160c17', bg='#e59ff0', font=("Helvetica", 23, 'bold'))
heading.place(x=50, y=5)

# contact
entry_1 = Entry(frame, width=35, border=3)
entry_1.place(x=120, y=130)

labl_1 = Label(frame, text="Email", width=10, font=("bold", 10))
labl_1.place(x=30, y=170)

# email
entry_2 = Entry(frame, width=35, border=3)
entry_2.place(x=120, y=170)

labl_2 = Label(frame, text="Contact", width=10, font=("bold", 10))
labl_2.place(x=30, y=130)

# head volunteer name
entry_3 = Entry(frame, width=35, border=3)
entry_3.place(x=200, y=210)

labl_3 = Label(frame, text="Head volunteer name", width=20, font=("bold", 10))
labl_3.place(x=30, y=210)


# event date
labl_date = Label(frame, text="Event date (YYYY-MM-DD)", width=20, font=("bold", 10))
labl_date.place(x=30, y=250)

entry_date = Entry(frame, width=25, border=3)
entry_date.place(x=200, y=250)


options_NGO = ["LITTLE SISTERS OF THE POOR", "AAIJIDEVI CARE FOUNDATION", "ST. ANTHONYS HOME FOR THE AGED"]
selected_option = StringVar(root)
selected_option.set("SELECT THE NGO")
drop_NGO = OptionMenu(frame, selected_option, *options_NGO)
drop_NGO.place(x=30, y=300)

# slot
options_slot = [ "10:00:00", "15:00:00", "19:00:00"]
menu = StringVar(root)
menu.set("Select the slot")
# Create a dropdown Menu
drop = OptionMenu(frame, menu,*options_slot)
drop.place(x=290,y=300)

# description
entryw = Text(frame,width=35,height=2)
entryw.place(x=210, y=350)

labl_4 = Label(frame, text="Describe event in short", width=20,  font=("bold", 10))
labl_4.place(x=30, y=350)

def onClick():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="project",
        sql_mode = "STRICT_TRANS_TABLES"
    )

    ngo_name = selected_option.get()
    contact = entry_1.get()
    email = entry_2.get()
    head_volunteer = entry_3.get()
    event_date = entry_date.get()
    event_slot = menu.get().replace('-', ':')
    event_desc = entryw.get("1.0", "end-1c")

    cursor = mydb.cursor()
    sql = "INSERT INTO events (contact, email, head_volunteer, event_date, event_slot, event_desc,ngo) VALUES (%s, %s, %s, %s, %s, %s,%s)"
    val = (contact, email, head_volunteer, event_date, event_slot, event_desc,ngo_name)
    cursor.execute(sql, val)
    mydb.commit()
    tkinter.messagebox.showinfo("Success", "Form Submitted")


sign_up = Button(frame, width=15, text='Confirm', border=8, bg="white", cursor="hand2", fg="#57a1f8", command=onClick)
sign_up.place(x=100,y=400)
root.mainloop()