from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class IndexPage:
    def __init__(self):
        self.root = Tk()
        self.root.title('Index Page')
        self.root.geometry('925x500+300+200')
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        # load and resize background image
        img = Image.open("C://Users//ACER//PycharmProjects//Old_Age_Home//Image//index_bg.jpg")
        img = img.resize((925,500))
        img = ImageTk.PhotoImage(img)

        # create background label
        bg_label=Label(self.root, image=img)
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        # create heading label
        heading = Label(self.root, text='LOGINS', fg='#27003a',bg='#76028d', font=("Helvetica", 23, 'bold'))
        heading.place(x=380, y=10)

        # create admin login button
        Admin_login = Button(self.root, width=25, text='Admin', border=30, bg="white",
                             font=('Microsoft YaHei UI Light', 15), cursor="hand2", fg="#57a1f8", command=self.admin_login)
        Admin_login.place(x=275, y=120)

        # create user login button
        User_login = Button(self.root, width=25, text='User', font=('Microsoft YaHei UI Light', 15), border=30, bg="white",
                            cursor="hand2", fg="#57a1f8", command=self.user_login)
        User_login.place(x=275, y=290)

        self.root.mainloop()

    def admin_login(self):
        self.root.destroy()
        import admin_login

    def user_login(self):
        self.root.destroy()
        import signup_db


index_page = IndexPage()
