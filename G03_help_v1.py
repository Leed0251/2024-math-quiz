from tkinter import *

class HelpGui:
    def __init__(self, partner):
        bg = "#FFF2CC"

        self.help_text = "To answer questions in the quiz you must enter into the white box the answer of the question above, if an x is present then you are solving x. You can export at any time where you will be given a list of all questions and their answers that you have entered in so far in the quiz."

        self.help_window = Toplevel()
        self.help_window.config(
            bg=bg,
            padx=5,
            pady=5
        )
        # Disable help button
        partner.quiz_window.help_button.config(
            state=DISABLED
        )

        # Heading text
        self.heading = Label(self.help_window)
        self.heading.config(
            padx=5,
            pady=5,
            font=("Arial","18","bold"),
            text="Help",
            bg=bg
        )
        self.heading.grid(padx=5, pady=5)

        # Help text
        self.label = Label(self.help_window)
        self.label.config(
            padx=5,
            pady=5,
            bg=bg,
            text=self.help_text,
            justify=LEFT,
            wraplength=260
        )
        self.label.grid(padx=5, pady=5)
        
        # Dismiss button
        self.dismiss_button_frame = Frame(self.help_window)
        self.dismiss_button_frame.config(
            bg="#F5F5F5",

            highlightthickness=2,
            highlightbackground="#666666"
        )
        self.dismiss_button_frame.grid(padx=5, pady=5)

        self.dismiss_button = Button(self.dismiss_button_frame)
        self.dismiss_button.config(
            padx=5,
            pady=5,

            relief="solid",
            borderwidth=0,
            
            text="Dismiss",
            bg="#F5F5F5",
            font=("Arial","12")
        )
        self.dismiss_button.grid()