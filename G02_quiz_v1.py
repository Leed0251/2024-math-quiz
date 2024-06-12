from tkinter import *
from functools import partial # To prevent unwanted windows

class QuestionFrame:
    def __init__(self, partner, root):
        root.withdraw()
        bg = "#E1D5E7"

        self.question_window = Toplevel()

        # If users press cross at top, closes help and releases help button
        self.question_window.protocol('WM_DELETE_WINDOW',
            partial(self.close_window, root)
        )

        # Appearance
        self.question_window.config(
            bg=bg,
            padx=5,
            pady=5
        )

        partner.question_label = Label(self.question_window)
        partner.question_label.config(text=f"Question 1 / {partner.round_count.get()}",
            background=bg,
            font=("Arial", "12", "bold"),
            padx=5,
            pady=5
        )
        partner.question_label.grid(row=0)

        self.question_frame = Frame(self.question_window)
        self.question_frame.config(
            highlightbackground="#000000",
            highlightthickness=2
        )
        self.question_frame.grid(row=1, padx=5, pady=5)
        partner.question_display = Label(self.question_frame,
            background="#FFFFFF",
            font=("Arial", "16", "bold"),
            padx=5,
            pady=5,
            width=21
        )
        partner.question_display.grid(row=0)

        # User answer input
        self.answer_frame = Frame(self.question_window)
        self.answer_frame.config(bg=bg)
        self.answer_frame.grid(row=2, padx=5, pady=5)
        
        self.answer_container = Frame(self.answer_frame)
        self.answer_container.config(
            highlightbackground="#D79B00",
            highlightthickness=2,

            bg="#FFE6CC",

            padx=2,
            pady=2
        )
        self.answer_container.grid(padx=5, pady=5)

        partner.answer_box = Entry(self.answer_container)
        partner.answer_box.config(
            text="",
            font=("Arial", "12"),
            width=19,

            relief="solid",
            borderwidth=0,
            bg="#FFE6CC"
        )
        partner.answer_box.grid(row=0, column=0, padx=5, pady=5)

        # Submit button
        partner.submit_frame = Frame(self.answer_frame)
        partner.submit_frame.config(
            bg="#FFE6CC",
            highlightthickness=2,
            highlightbackground="#D79B00"
        )
        partner.submit_frame.grid(row=0, column=1, padx=5, pady=5)

        partner.answer_submit = Button(partner.submit_frame)
        partner.answer_submit.config(
            text="Enter",
            font=("Arial", "12"),
            width=8,

            relief="solid",
            borderwidth=0,
            bg="#FFE6CC",

            padx=5,
            pady=5
        )
        partner.answer_submit.grid()

        # Row 3 buttons
        self.button_frame = Frame(self.question_window)
        self.button_frame.config(bg=bg, padx=5, pady=5)
        self.button_frame.grid(row=3, padx=5, pady=5)

        # Help button
        self.help_frame = Frame(self.button_frame)
        self.help_frame.config(
            bg="#FFF2CC",
            highlightthickness=2,
            highlightbackground="#D6B656"
        )
        self.help_frame.grid(row=0, column=0, padx=5)

        partner.help_button = Button(self.help_frame)
        partner.help_button.config(
            text="Help",
            font=("Arial", "12"),
            width=8,

            relief="solid",
            borderwidth=0,
            bg="#FFF2CC",
            
            padx=5,
            pady=5
        )
        partner.help_button.grid()

        # Export button
        self.export_frame = Frame(self.button_frame)
        self.export_frame.config(
            bg="#DAE8FC",
            highlightthickness=2,
            highlightbackground="#6C8EBF"
        )
        self.export_frame.grid(row=0, column=1, padx=5)

        partner.export_button = Button(self.export_frame)
        partner.export_button.config(
            text="Export",
            font=("Arial", "12"),
            width=8,

            relief="solid",
            borderwidth=0,
            bg="#DAE8FC",
            
            padx=5,
            pady=5
        )
        partner.export_button.grid()

        # Start over button
        self.start_over_frame = Frame(self.button_frame)
        self.start_over_frame.config(
            bg="#F5F5F5",
            highlightthickness=2,
            highlightbackground="#666666"
        )
        self.start_over_frame.grid(row=0, column=2, padx=5)

        partner.start_over_button = Button(self.start_over_frame)
        partner.start_over_button.config(
            text="Start Over",
            font=("Arial", "12"),
            width=8,

            relief="solid",
            borderwidth=0,
            bg="#F5F5F5",

            padx=5,
            pady=5
        )
        partner.start_over_button.grid()

    def close_window(self, root):
        root.deiconify()
        self.question_window.destroy()