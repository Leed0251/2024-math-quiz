from tkinter import *
import datetime

class ExportGui():
    def __init__(self, partner):
        instructions = f"Below is a list of the content that you are exporting, if you do not enter in a file name it will be named {datetime.datetime.today().strftime('%Y_%m_%d')}_Results.csv, This file includes all questions you have answered along with a score from 0 to 100 based on how well you have done. Then just click the green export button to make your file."
        bg="#DAE8FC"

        partner.quiz_window.export_button.config(state=DISABLED)

        self.export_window = Toplevel()
        self.export_window.config(
            bg=bg,
            padx=5,
            pady=5
        )

        self.heading = Label(self.export_window)
        self.heading.config(
            bg=bg,
            text="Export",
            font=("Arial","16","bold")
        )
        self.heading.grid(row=0, sticky="we")

        self.export_instructions = Label(self.export_window)
        self.export_instructions.config(
            bg=bg,
            text=instructions,
            wraplength=400,
            justify=LEFT,
            font=("Arial", "12"),
            padx=5,
            pady=5
        )
        self.export_instructions.grid(row=1, sticky="we")

        self.content_frame = Frame(self.export_window)
        self.content_frame.config(
            bg="#FFF2CC",
            highlightbackground="#D6B656",
            highlightthickness=2
        )
        self.content_frame.grid(
            row=2, 
            padx=5,
            pady=5,
            sticky="we"
        )

        self.content_label = Label(self.content_frame)
        self.content_label.config(
            bg="#FFF2CC",
            justify=LEFT,
            font=("Consolas", "10"),
            padx=5,
            pady=5,
            height=6
        )
        self.content_label.grid()

        self.filename_box = Entry(self.export_window)
        self.filename_box.config(
            bg="#FFFFFF",
            highlightbackground="#000000",
            highlightthickness=2,
            borderwidth=0,
            relief="solid",
            font=("Arial", 14),
            
        )
        self.filename_box.grid(row=3, padx=5, pady=5, sticky="we")

        self.buttons_frame = Frame(self.export_window)
        self.buttons_frame.config(
            bg=bg
        )
        self.buttons_frame.grid(row=4, sticky="we")

        self.export_dismiss_frame = Frame(self.buttons_frame)
        self.export_dismiss_frame.config(
            bg="#F5F5F5",
            highlightbackground="#666666",
            highlightthickness=2
        )
        self.export_dismiss_frame.grid(row=0, column=0, padx=5, pady=5, sticky="we")

        self.export_dismiss_button = Button(self.export_dismiss_frame)
        self.export_dismiss_button.config(
            text="Dismiss",
            bg="#F5F5F5",
            font=("Arial", "15", "bold"),
            relief="solid",
            borderwidth=0,
        )
        self.export_dismiss_button.grid(sticky="nesw")

        self.export_frame = Frame(self.buttons_frame)
        self.export_frame.config(
            bg="#D5E8D4",
            highlightbackground="#82B366",
            highlightthickness=2
        )
        self.export_frame.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        self.export_success_button = Button(self.export_frame)
        self.export_success_button.config(
            text="Export",
            bg="#D5E8D4",
            font=("Arial", "15", "bold"),
            relief="solid",
            borderwidth=0,
        )
        self.export_success_button.grid(sticky="nesw")

        self.error_label = Label(self.export_window)
        self.error_label.config(
            bg="#F8CECC",
            highlightbackground="#B85450",
            highlightthickness=2,
            text="Error message",
            padx=5,
            pady=5,
            font=("Arial", "12")
        )

        # GUI Scaling
        self.export_window.grid_columnconfigure(0, weight=1)
        self.export_window.grid_columnconfigure(1, weight=1)
        self.export_window.grid_columnconfigure(2, weight=1)
        self.export_window.grid_columnconfigure(3, weight=1)
        self.export_window.grid_columnconfigure(4, weight=1)
        self.export_window.grid_columnconfigure(5, weight=1)

        self.buttons_frame.grid_columnconfigure(0, weight=1)
        self.buttons_frame.grid_columnconfigure(1, weight=1)

        self.export_dismiss_frame.grid_columnconfigure(0, weight=1)
        self.export_frame.grid_columnconfigure(0, weight=1)