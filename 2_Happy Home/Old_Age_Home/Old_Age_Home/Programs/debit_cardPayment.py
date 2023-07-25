from tkinter import *
from tkinter import messagebox          ######## database1(credit card,payment_date,phone_no,card_no,amount,transac_id)
import random                           ######## database2(name,phone_no,city,zipcode,ngo_name)
import requests
import json
import re
import mysql.connector
from datetime import datetime

root = Tk()
root.title('Payment Gateway')
root.geometry('975x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)


mode = 'debit'
selected_option = ''
def insert_payment_details(name, contact_no, city, zipcode, ngo, mode,amount, card_number, expiry_date, cvv,transaction_id):
    # establish connection
    conn = mysql.connector.connect(
        host='localhost', user='root', password='admin', database='project'
    )

    # create a cursor
    cursor = conn.cursor()

    # insert payment details
    sql = "INSERT INTO payment_details (fullname,contact_number,city,zipcode,ngo,payment_mode,amount, card_number, expiry_date, cvv,transaction_id,datetime) VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s)"
    val = (name,contact_no,city,zipcode,ngo,mode,amount, card_number, expiry_date, cvv, transaction_id,datetime.now())
    cursor.execute(sql, val)

    # commit the transaction
    conn.commit()

    # close the cursor and connection
    cursor.close()
    conn.close()

    print(cursor.rowcount, "record inserted.")



def pay_now():
    payment_amount = pay_amount_entry.get()
    card_no = card_number_entry.get()
    expiry = expiry_date_entry.get()
    cvv_label = cvv_entry.get()

    contact_no = phone_no_entry.get()
    name = name_entry.get()
    city = city_entry.get()
    zipcode = zipcode_entry.get()
    ngo = selected_option.get()

    entered_otp = otp_entry.get()
    transId = ''
    for i in range(6):
        transId += str(random.randint(0, 9))

    transaction_message = f"Transaction number is:{transId}"

    if entered_otp == otp_generated:
        messagebox.showinfo("Message","Payment Successful! "+transaction_message)
        insert_payment_details(name, contact_no, city, zipcode, ngo, mode,payment_amount, card_no, expiry, cvv_label, transId)


    else:
        messagebox.showerror("error","Invalid OTP")



def send_sms(otpgenerated):
    contact_no = phone_no_entry.get()

    url = "https://api.d7networks.com/messages/v1/send"

    payload = json.dumps({
        "messages": [
            {
                "channel": "sms",
                "recipients": [contact_no],
                "content": "Hello, your OTP Code: "+otpgenerated,
                "msg_type": "text",
                "data_coding": "text"
            }
        ],
        "message_globals": {
            "originator": "SignOTP",
            "report_url": "https://the_url_to_recieve_delivery_report.com"
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhdXRoLWJhY2tlbmQ6YXBwIiwic3ViIjoiZjE4MzcwYTEtMzFjMi00Njg0LWFkYTMtOWNlMmJlMDI3YTNmIn0.HzVZgNTBY7xwFCGmlQFlznfXjFoUjrnLBs_5fjVVnL0'}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    # Check the response status code and show a message to the user
    if response.status_code == 200:
        messagebox.showinfo("Success",'OTP sent successfully!')
    else:
        messagebox.showinfo("Success",'Error sending OTP. Please try again.')


def submit_details(msg="Data saved successfully."):
    # get user details
    name = name_entry.get()
    contact_no = phone_no_entry.get()
    city = city_entry.get()
    zipcode = zipcode_entry.get()
    ngo = selected_option.get()

    if not name.isprintable():
        messagebox.showerror("Error", "Invalid Name Entry")
        return
    pattern = re.compile(r'^\+(?:[0-9]){1,3}(?:[\s\-\.])?(?:[(]{1}[0-9]{1,6}[)])?[\s\-\.]?[0-9]{3,12}$')
    if not pattern.match(contact_no):
        messagebox.showerror("Error", "Invalid, Contact Number must be with country code or must be numeric only")
        return
    if not city.isalpha():
        messagebox.showerror("Error","Invalid City Name, \nProvide Correct City Name")
        return
    if not zipcode.isnumeric() or len(zipcode) != 6:
        messagebox.showerror("Error","Invalid Zipcode, \nEnter 6 digit zipcode")
        return
    if msg == "Data saved successfully.":
        # msg = "Data saved successfully."
        messagebox.showinfo("Message", msg)

    else:
        # here if the string is not equal to the msg it will come in this block
        otp = ''
        for i in range(4):
            otp += str(random.randint(0, 9))
        # here an otp is generated
        # declaring otp_generated as global variable because will have to use this variable in different function
        # or in different block
        global otp_generated
        otp_generated = otp  # store the generated otp in global variable
        message = f"OTP is sent to {contact_no}"
        messagebox.showinfo("Message", message)
        send_sms(otp_generated)


def generate_otp():
    # get payment details
    payment_amount = pay_amount_entry.get()
    card_no = card_number_entry.get()
    expiry = expiry_date_entry.get()
    cvv_label = cvv_entry.get()


    if not payment_amount.isdigit() or int(payment_amount) <= 0:
        messagebox.showerror("Error", "Invalid payment amount.")
        return
    if not card_no.isdigit() or len(card_no) != 16:
        messagebox.showerror("Error", "Invalid card number.")
        return
    if not expiry.isdigit() or len(expiry) != 4:
        messagebox.showerror("Error", "Invalid expiry date.")
        return
    if not cvv_label.isdigit() or len(cvv_label) != 3:
        messagebox.showerror("Error", "Invalid CVV.")
        return

    # after accepting all the details pop up the following message and send message to submit_details function
    response = "OTP SENDED SUCCESSFULLY"
    submit_details(response)

heading = Label(root, text='Payment Gateway', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=350, y=30)
heading = Label(root, text='Debit Card', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=390, y=90)

# left side frame(some personal details)
frame = Frame(root, width=295, height=375, bg='#57a1f8')
frame.place(x=75, y=100)

name_label = Label(frame, height=2, width=15, background="black", text="Full Name", foreground="white")
name_label.place(x=5, y=5)
name_entry = Entry(frame, width=20, background="white", border=1, font=('Microsoft YaHei UI Light', 11))
name_entry.place(x=5, y=45)

phone_no = Label(frame, height=2, width=15, background="black", text="Contact Number", foreground="white")
phone_no.place(x=5, y=75)
phone_no_entry = Entry(frame, width=20, background="white", border=1, font=('Microsoft YaHei UI Light', 11))
phone_no_entry.place(x=5, y=115)

city_label = Label(frame, height=2, width=15, background="black", text="City", foreground="white")
city_label.place(x=5, y=145)
city_entry = Entry(frame, width=13, background="white", border=1, font=('Microsoft YaHei UI Light', 11))
city_entry.place(x=5, y=185)

zipcode_label = Label(frame, height=2, width=15, background="black", text="ZIP Code", foreground="white")
zipcode_label.place(x=180, y=145)
zipcode_entry = Entry(frame, width=13, background="white", border=1, font=('Microsoft YaHei UI Light', 11))
zipcode_entry.place(x=180, y=185)

ngoSelect_label = Label(frame, height=2, width=20, background="black", text="Choose Any one NGO", foreground="white")
ngoSelect_label.place(x=5, y=225)

options = ["LITTLE SISTERS OF THE POOR", "AAIJIDEVI CARE FOUNDATION","ST. ANTHONYS HOME FOR THE AGED"]
selected_option = StringVar(frame)
selected_option.set(options[0])
ngoSelect_menu = OptionMenu(frame,selected_option, *options)
ngoSelect_menu.config(bg='white',fg='black')
ngoSelect_menu.place(x=5, y=265)

# button for submit now
submit_button = Button(frame, width=25, pady=7, text="SUBMIT DETAILS", bg='black', fg='white', border=1,
                       cursor='hand2', command=submit_details)
submit_button.place(x=50, y=325)

# right side frame(card details)
frame_rgt = Frame(root, width=295, height=375, bg='#57a1f8')
frame_rgt.place(x=595, y=100)

pay_amount = Label(frame_rgt, height=2, width=15, background="black", text="Payment Amount", foreground="white")
pay_amount.place(x=5, y=5)
pay_amount_entry = Entry(frame_rgt, width=13, background="white", border=1, font=('Microsoft YaHei UI Light', 11))
pay_amount_entry.place(x=145, y=10)

card_number = Label(frame_rgt, height=2, width=15, background="black", text="Card Number", foreground="white")
card_number.place(x=5, y=65)
card_number_entry = Entry(frame_rgt, width=30, background="white", border=1, font=('Microsoft YaHei UI Light', 11))
card_number_entry.place(x=5, y=110)

expiry_date = Label(frame_rgt, height=2, width=15, background="black", text="Expiry Date", foreground="white")
expiry_date.place(x=5, y=155)
expiry_date_entry = Entry(frame_rgt, width=13, background="white", border=1, font=('Microsoft YaHei UI Light', 11))
expiry_date_entry.place(x=145, y=165)

cvv_label = Label(frame_rgt, height=2, width=15, background="black", text="CVV", foreground="white")
cvv_label.place(x=5, y=210)
cvv_entry = Entry(frame_rgt, width=13, background="white", border=1, font=('Microsoft YaHei UI Light', 11), show="*")
cvv_entry.place(x=145, y=220)

# if verify the above details then generate otp
get_otp_label = Label(frame_rgt, height=2, width=15, text="Submit OTP Here", bg='black', fg='white')
get_otp_label.place(x=5, y=265)
otp_entry = Entry(frame_rgt, width=13, background="white", border=1, foreground="black",
                  font=('Microsoft YaHei UI Light', 11))
otp_entry.place(x=145, y=275)

submit_otp_button = Button(frame_rgt, width=15, pady=7, background="black", text="Generate OTP", foreground="white",
                           border=1,
                           cursor='hand2', command=generate_otp)
submit_otp_button.place(x=25, y=325)

# button for pay now(if otp verification is successful)
pay_now_button = Button(frame_rgt, width=15, pady=7, text="PAY NOW!!", bg='black', fg='white', border=1,
                        cursor='hand2',command=pay_now)
pay_now_button.place(x=155, y=325)

root.mainloop()
