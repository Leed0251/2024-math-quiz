from tkinter import *

class Gui:
    def __init__(self, partner, root):
        background_color = "#DAE8FC"

        root.config(
            bg=background_color
        )

        self.select_frame = Frame(root, bg=background_color)
        self.select_frame.grid(padx=15, pady=10)

        self.heading = Label(self.select_frame,
            text="Math Quiz",
            font=("Arial", "24", "bold"),

            bg=background_color
        )
        self.heading.grid(row=0)

        self.sub_heading = Label(self.select_frame,
            text="How many questions would you like to answer?",
            font=("Arial", "14"),

            wraplength=250,
            bg=background_color,
            fg="#333333",
        )
        self.sub_heading.grid(row=1)

        self.input_frame = Frame(self.select_frame, bg=background_color)
        self.input_frame.grid(row=2)

        self.entry_frame = Frame(self.input_frame,
            highlightthickness=2,
            highlightbackground="#82B366",
        )
        self.entry_frame.grid(row = 0, column=0, padx=10, pady=10)

        partner.number_box = Entry(self.entry_frame,
            text="1",
            font=("Arial", "14"),
            width=12,

            relief="solid",
            borderwidth=0,
            bg="#D5E8D4"
        )
        partner.number_box.grid()

        self.enter_frame = Frame(self.input_frame,
            highlightthickness=2,
            highlightbackground="#82B366",
        )
        self.enter_frame.grid(row=0, column=1)

        partner.enter_button = Button(self.enter_frame,
            text=">",
            font=("Arial", "10", "bold"),
            width=3,

            relief="solid",
            borderwidth=0,
            bg="#D5E8D4"
        )
        partner.enter_button.grid()

        partner.error_frame = Frame(self.select_frame,
            highlightthickness=2,
            highlightbackground="#B85450",
            background="#F8CECC",
            padx=5,
            pady=5
        )

        partner.error_label = Label(partner.error_frame,
            text="",
            font=("Arial", "10"),

            bg="#F8CECC",
            fg="#000000",
        )
        partner.error_label.grid()