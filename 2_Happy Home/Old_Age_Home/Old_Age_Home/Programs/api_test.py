import re
import tkinter as tk

def validate_phone_number():
    phone_number = phone_entry.get()
    pattern = re.compile(r'^\+(?:[0-9]){1,3}(?:[\s\-\.])?(?:[(]{1}[0-9]{1,6}[)])?[\s\-\.]?[0-9]{3,12}$')
    if pattern.match(phone_number):
        status_label.config(text="Phone number is valid.", fg="green")
    else:
        status_label.config(text="Phone number is invalid.", fg="red")

# create a tkinter window
window = tk.Tk()

# create a phone number entry widget
phone_entry = tk.Entry(window)
phone_entry.pack()

# create a validate button
validate_button = tk.Button(window, text="Validate", command=validate_phone_number)
validate_button.pack()

# create a status label to display validation status
status_label = tk.Label(window, text="")
status_label.pack()

# start the tkinter mainloop
window.mainloop()