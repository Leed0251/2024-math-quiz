from tkinter import *

class QuestionFrame:
    def __init__(self, partner, root):
        root.withdraw()
        bg = "#E1D5E7"

        self.question_window = Toplevel()

        # Appearance
        self.question_window.config(
            bg=bg,
            padx=5,
            pady=5
        )

        self.question_label = Label(self.question_window)
        self.question_label.config(text=f"Question 1 / {partner.question_count.get()}",
            background=bg,
            font=("Arial", "12", "bold"),
            padx=5,
            pady=5
        )
        self.question_label.grid(row=0)

        self.question_frame = Frame(self.question_window)
        self.question_frame.config(
            highlightbackground="#000000",
            highlightthickness=2
        )
        self.question_frame.grid(row=1, padx=5, pady=5)
        self.question_display = Label(self.question_frame,
            background="#FFFFFF",
            font=("Arial", "16", "bold"),
            padx=5,
            pady=5,
            width=21
        )
        self.question_display.grid(row=0)

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

        self.answer_box = Entry(self.answer_container)
        self.answer_box.config(
            text="",
            font=("Arial", "12"),
            width=19,

            relief="solid",
            borderwidth=0,
            bg="#FFE6CC"
        )
        self.answer_box.grid(row=0, column=0, padx=5, pady=5)

        self.response_frame = Frame(self.answer_frame)
        self.response_frame.config(
            width=19,
            relief="solid",
            borderwidth=0,
            highlightthickness=2
        )

        self.response_label = Label(self.response_frame)
        self.response_label.config(
            text="",
            font=("Arial", "12"),
            width=19,
        )
        self.response_label.grid(padx=5, pady=5)

        # Submit button
        self.submit_frame = Frame(self.answer_frame)
        self.submit_frame.config(
            bg="#FFE6CC",
            highlightthickness=2,
            highlightbackground="#D79B00"
        )
        self.submit_frame.grid(row=0, column=1, padx=5, pady=5)

        self.answer_submit = Button(self.submit_frame)
        self.answer_submit.config(
            text="Enter",
            font=("Arial", "12"),
            width=8,

            relief="solid",
            borderwidth=0,
            bg="#FFE6CC",

            padx=5,
            pady=5
        )
        self.answer_submit.grid()

        # Error display
        self.quiz_error_frame = Frame(self.question_window,
            highlightthickness=2,
            highlightbackground="#B85450",
            background="#F8CECC",
            padx=5,
            pady=5
        )

        self.quiz_error_label = Label(self.quiz_error_frame,
            text="",
            font=("Arial", "10"),
            width=32,

            bg="#F8CECC",
            fg="#000000",
        )
        self.quiz_error_label.grid()

        # Row 3 buttons
        self.button_frame = Frame(self.question_window)
        self.button_frame.config(bg=bg, padx=5, pady=5)
        self.button_frame.grid(row=4, padx=5, pady=(0, 5))

        # Help button
        self.help_frame = Frame(self.button_frame)
        self.help_frame.config(
            bg="#FFF2CC",
            highlightthickness=2,
            highlightbackground="#D6B656"
        )
        self.help_frame.grid(row=0, column=0, padx=5)

        self.help_button = Button(self.help_frame)
        self.help_button.config(
            text="Help",
            font=("Arial", "12"),
            width=8,

            relief="solid",
            borderwidth=0,
            bg="#FFF2CC",
            
            padx=5,
            pady=5
        )
        self.help_button.grid()

        # Export button
        self.export_frame = Frame(self.button_frame)
        self.export_frame.config(
            bg="#DAE8FC",
            highlightthickness=2,
            highlightbackground="#6C8EBF"
        )
        self.export_frame.grid(row=0, column=1, padx=5)

        self.export_button = Button(self.export_frame)
        self.export_button.config(
            state=DISABLED,

            text="Export",
            font=("Arial", "12"),
            width=8,

            relief="solid",
            borderwidth=0,
            bg="#DAE8FC",
            
            padx=5,
            pady=5
        )
        self.export_button.grid()

        # Start over button

        self.start_over_frame = Frame(self.button_frame)
        self.start_over_frame.config(
            bg="#F5F5F5",
            highlightthickness=2,
            highlightbackground="#666666"
        )
        self.start_over_frame.grid(row=0, column=2, padx=5)

        self.start_over_button = Button(self.start_over_frame)
        self.start_over_button.config(
            text="Start Over",
            font=("Arial", "12"),
            width=8,

            relief="solid",
            borderwidth=0,
            bg="#F5F5F5",

            padx=5,
            pady=5
        )
        self.start_over_button.grid()