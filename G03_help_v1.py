from tkinter import *
from functools import partial

class HelpGui:
    def __init__(self, partner):
        bg = "#FFF2CC"

        self.help_text = " huireg huighiuweegh iuwegguyegfjoighuidbh ub husghiugguyg hiegh uieghiusghiueggyug g iughyusgiuesg hiuseh iuseghsiufuyf fhrherhgwehah thth rththrhtrfh"

        partner.help_window = Toplevel()
        partner.help_window.config(
            bg=bg,
            padx=5,
            pady=5
        )
        # Disable help button
        partner.help_button.config(
            state=DISABLED
        )
        partner.help_window.protocol('WM_DELETE_WINDOW',
            partial(self.close_help_window, partner)
        )

        self.help_heading = Label(partner.help_window)
        self.help_heading.config(
            padx=5,
            pady=5,
            font=("Arial","18","bold"),
            text="Help",
            bg=bg
        )
        self.help_heading.grid(padx=5, pady=5)

        self.help_label = Label(partner.help_window)
        self.help_label.config(
            padx=5,
            pady=5,
            bg=bg,
            text=self.help_text,
            wraplength=260
        )
        self.help_label.grid(padx=5, pady=5)

        self.dismiss_button_frame = Frame(partner.help_window)
        self.dismiss_button_frame.config(
            bg="#F5F5F5",

            highlightthickness=2,
            highlightbackground="#666666"
        )
        self.dismiss_button_frame.grid(padx=5, pady=5)

        partner.help_dismiss_button = Button(self.dismiss_button_frame)
        partner.help_dismiss_button.config(
            padx=5,
            pady=5,

            relief="solid",
            borderwidth=0,
            
            text="Dismiss",
            bg="#F5F5F5",
            font=("Arial","12")
        )
        partner.help_dismiss_button.grid()


    def close_help_window(self, partner):
        # Re-enable help button when closed
        partner.help_window.destroy()
        partner.help_button.config(
            state=NORMAL
        )