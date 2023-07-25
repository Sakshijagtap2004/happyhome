from tkinter import *
import requests


class Places:
    def __init__(self):
        # create the main window
        self.root = Tk()
        self.root.geometry("1600x3000")
        # set the title of the main window
        self.root.title('Nearby Restaurants')

        # create a label and an entry field for the location

        my_labelframe = LabelFrame(self.root, text="Enter any place between goa and mumbai")
        my_labelframe.pack(side=TOP, anchor='nw', padx=10)

        location_entry = Entry(my_labelframe, font=("Helvetica", 15))
        location_entry.grid(row=0, column=0, padx=10, pady=10)

        # create a button to submit the location
        submit_button = Button(my_labelframe, text='Submit', width="10", command=self.submit_location)
        submit_button.grid(row=0, column=1, padx=10)

        my_text = Text(self.root, height=30, width=65, wrap=WORD)
        my_text.pack(padx=10, pady=10, anchor="nw")

        back = Button(self.root, text="Back", width="15",height="2", command=self.go_to_main)
        back.pack(padx=200, pady=10, anchor="w")

        # start the main loop
        self.root.mainloop()

    # create a function to get the list of nearby areas

    def submit_location(self):
        loc = self.location_entry.get()

        # get the list of nearby areas
        self.get_nearby_areas(loc)
        # create a label to display the list of nearby areas

    def go_to_main(self):
        self.root.destroy()

Places()