from tkinter import *
import G01_select_questions_v1

class QuizGame:
    def __init__(self, root):
        # Create the GUI Frame
        G01_select_questions_v1.Gui(self, root)

        # Function gives the following variables
        """
            self.number_box : Entry
            The entry box a user puts their round number in

            self.enter_button : Button
            The next button that starts the game

            self.error_frame : Frame
            The frame the contains error_label

            self.error_label : Label
            Label that gives user feedback when a mistake is made in the entry box
        """

        self.enter_button.config(
            command=lambda: self.check_input(1, 1000)
        )

    def check_input(self, min, max):
        num = self.number_box.get()
        result, errMessage = self.check_num(num, min, max)

        if result:
            # User input was valid
            self.round_count = IntVar()
            self.round_count.set(int(num))
            
            self.error_frame.grid_forget()
            self.error_label.config(text=errMessage)
        else:
            # User input was not valid
            self.error_frame.grid(row=3)
            self.error_label.config(text=errMessage)
            
    @staticmethod
    def check_num(num, min, max):
        boundary_error = f"Number must be between {min} and {max}"
        num_error = "Input must be a whole number"
        blank_error = "Input can not be blank"

        # Check that input is an integer
        if num == "":
            return False, blank_error

        try:
            user_input = int(num)

            if min <= user_input <= max:
                return True, num
            else:
                return False, boundary_error
        except:
            return False, num_error

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    QuizGame(root)
    root.mainloop()