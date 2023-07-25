import tkinter
from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox


window = Tk()  # creating the default tkinter page

window.title("Home Page")  # title of the page

window.geometry('1500x750+5+10')  # setting the geometry of the page

window.config(bg='#fff')  # setting the background color

window.resizable(False, False)  # setting non-resizable page
# gui connective


def donatepage():
    try:
        import fund_donate
    except Exception as e:
        print("Error is in: ", e)
        messagebox.showerror("Error", "Error in opening donation page")


def user_profile():
    try:
        import user
    except:
        messagebox.showerror("Error","Error in opening user profile")

def organise():
    try:
        import organise_events
    except:
        messagebox.showerror("Error","Error in opening organize events page")


def welfare_page():
    try:
        import welfaredonation
    except:
        messagebox.showerror("Error","Error in opening welfare page")


def about_us():
    root = Tk()
    root.geometry('500x500')
    root.title("About Us Page")
    info = Label(root, text="A Mini Project based on Donation for Specific OLD AGE HOME's")
    info.place(x=10,y=10)

    root.mainloop()


def logout():
    # hide profile page and show login page
    window.destroy()
    import index_page

# creating main frame window
frame = Frame(window, width=1500, height=750, bg='#fff')
frame.place(x=0, y=0)

# background image
bg_image = PhotoImage(file="C://Users//ACER//PycharmProjects//Old_Age_Home//Image//image.png")
bg_label = Label(frame, image=bg_image)
bg_label.place(x=0, y=0)



# creating a user profile icon
profile = PhotoImage(file='C://Users//ACER//PycharmProjects//Old_Age_Home//Image//profile.png')
Button(window, image=profile, border=0, bg='white', cursor='hand2', command=user_profile).place(x=1425, y=0)


logout_button = Button(window, text="Logout", command=logout,border=4,bg='#57a1f8', fg='white', cursor='hand2',width=10)
logout_button.place(x=1290, y=35)

# creating system heading
heading = Label(frame, text="HAPPY HOME", fg='#57a1f8', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=675, y=5)

# creating a donation button
donate_button = Button(frame, width=39, pady=7, text="Fund Donation", bg='#57a1f8', fg='white', border=0, cursor='hand2',
                       command=donatepage)
donate_button.place(x=50, y=400)

# creating welfare donation button
welfare_button = Button(frame, width=39, pady=7, text="Welfare Donation", bg='#57a1f8', fg='white', border=0,
                        cursor='hand2', command=welfare_page)
welfare_button.place(x=50, y=470)

# event organisation button
event_button = Button(frame, width=39, pady=7, text='Organize Events', bg='#57a1f8', fg='white', border=0,
                      cursor='hand2', command=organise)
event_button.place(x=50, y=540)


# about us
about_us = Button(frame, text='About Us', bg='#57a1f8', fg='white', cursor='hand2', bd=0, command=about_us)
about_us.place(x=1435, y=725)

window.mainloop()
