import requests
import json

url = "https://api.d7networks.com/messages/v1/send"

payload = json.dumps({
  "messages": [
    {
      "channel": "sms",
      "recipients": ["+919833799878"],
      "content": "Hello Karan Jain. Rs.1600 debited from your account(06-04-2023 15:04:12)",
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
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdJhdXRoLWJhY2tlbmQ6YXBwIiwic3ViIjoiYzFjMmUxMmMtNWRmMS00NGViLWFjNmUtM2NhMzE3NWQ2ZDViIn0.Q68Gezjn5wcNrAtN2fbLFneIqbTBnBBLejrC3EqSBkQ'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)




### validation
# import re
# import tkinter as tk
#
# def validate_email(email):
#     """Validate email address format using regular expression"""
#     email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
#     return email_pattern.match(email)
#
# def validate_fullname(fullname):
#     """Validate full name format using regular expression"""
#     fullname_pattern = re.compile(r"^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$")
#     return fullname_pattern.match(fullname)
#
# def validate_contact(contact):
#     """Validate contact number format using regular expression"""
#     contact_pattern = re.compile(r"^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$")
#     return contact_pattern.match(contact)
#
# def validate_password(password):
#     """Validate password format using regular expression"""
#     password_pattern = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).{8,}$")
#     return password_pattern.match(password)
#
# def submit_form():
#     """Function to validate and submit form data"""
#     email = email_entry.get()
#     fullname = fullname_entry.get()
#     contact = contact_entry.get()
#     password = password_entry.get()
#
#     if not validate_email(email):
#         error_label.config(text="Invalid Email")
#     elif not validate_fullname(fullname):
#         error_label.config(text="Invalid Full Name")
#     elif not validate_contact(contact):
#         error_label.config(text="Invalid Contact Number")
#     elif not validate_password(password):
#         error_label.config(text="Invalid Password")
#     else:
#         error_label.config(text="")
#         # Submit form data here
#
# # Create Tkinter window and form fields
# window = tk.Tk()
# window.title("Form Validation")
#
# email_label = tk.Label(window, text="Email")
# email_entry = tk.Entry(window)
# email_label.grid(row=0, column=0)
# email_entry.grid(row=0, column=1)
#
# fullname_label = tk.Label(window, text="Full Name")
# fullname_entry = tk.Entry(window)
# fullname_label.grid(row=1, column=0)
# fullname_entry.grid(row=1, column=1)
#
# contact_label = tk.Label(window, text="Contact Number")
# contact_entry = tk.Entry(window)
# contact_label.grid(row=2, column=0)
# contact_entry.grid(row=2, column=1)
#
# password_label = tk.Label(window, text="Password")
# password_entry = tk.Entry(window, show="*")
# password_label.grid(row=3, column=0)
# password_entry.grid(row=3, column=1)
#
# submit_button = tk.Button(window, text="Submit", command=submit_form)
# submit_button.grid(row=4, column=1)
#
# error_label = tk.Label(window, fg="red")
# error_label.grid(row=5, column=1)
#
# window.mainloop()
