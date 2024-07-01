from tkinter import *
import re
import math
import random
import G01_select_questions_v1
import G02_quiz_v1
import G03_help_v1
import G04_export_v1

class QuizGame:
    def __init__(self, root):
        # Create the GUI Frame
        G01_select_questions_v1.Gui(self, root)

        # Function gives the following variables
        """
            self.number_box : Entry
            The entry box a user enters the amount of questions they would like to answer

            self.enter_button : Button
            The next button that starts the quiz

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
            self.question_count = IntVar()
            self.question_count.set(int(num))
            
            self.error_frame.grid_forget()
            self.error_label.config(text=errMessage)

            # Load main quiz
            G02_quiz_v1.QuestionFrame(self, root)
            # Function gives the following variables
            """
                self.question_window
                Root window

                self.question_label
                Label that displays the users progress through the questions

                self.question_display
                Displays the current question the user is answering

                self.answer_box
                Where the user enters their input

                self.response_frame
                Frame that contains the label used to communicate to the user

                self.response_label
                Label that communicates to the user whether they are right or wrong

                self.submit_frame
                Frame that contains the submit button (for the appearance)
                
                self.answer_submit
                Button that the user clicks to submit their answer

                self.help_button
                Displays frame showing instructions

                self.export_button
                Displays frame that allows user to export their report

                self.start_over_button
                Sends the user back to the home page
            """
            self.question_number = IntVar()
            self.question = StringVar()
            self.answer = IntVar()

            # help button
            self.help_button.config(
                command=lambda: self.open_help()
            )

            # start over button
            self.start_over_button.config(
                command=lambda: self.close_quiz()
            )

            self.next_question()
        else:
            # User input was not valid
            self.error_frame.grid(row=3)
            self.error_label.config(text=errMessage)

    def next_question(self):
        if self.question_number.get() == self.question_count.get():
            self.show_response("Complete", "#FFFFFF", "#000000")
            self.submit_frame.grid_forget()
            return
        
        self.show_response("", "#FFE6CC", "#D79B00")
        
        self.answer_submit.config(
            command=lambda: self.check_answer(),
            text="Enter"
        )
        self.response_frame.grid_forget()
        self.answer_container.grid(padx=5, pady=5, row=0)
        
        self.answer_box.delete(0, "end")
        self.question_number.set(self.question_number.get() + 1)
        self.question_label.config(text=f"Question {self.question_number.get()}/{self.question_count.get()}")
        # Generate new question for user to solve
        GenerateQuestion(self, 1, 15, 3)

        self.question_display.config(
            text=self.question.get()
        )

    def check_answer(self):
        user_answer = self.answer_box.get()
        result, returned_value = self.check_num(user_answer, -math.inf, math.inf)
        
        if not result:
            self.quiz_error_frame.grid(row=3)
            self.quiz_error_label.config(
                text=returned_value
            )
            return
        
        self.quiz_error_frame.grid_forget()
        
        self.answer_container.grid_forget()
        self.response_frame.grid(padx=5, pady=5, row=0)

        if returned_value == self.answer.get():
            self.show_response("Correct", "#D5E8D4", "#82B366")
        else:
            self.show_response("Incorrect", "#F8CECC", "#B85450")
            print(f"Correct answer was {self.answer.get()}")
        
        if self.question_number.get() == self.question_count.get():
            self.answer_submit.config(text="Finish")

        self.answer_submit.config(
            command=lambda: self.next_question()
        )

    def show_response(self, text, background, highlight):
        self.response_frame.config(
            bg=background,
            highlightbackground=highlight
        )
        self.response_label.config(
            bg=background,
            text=text
        )
        self.submit_frame.config(
            bg=background,
            highlightbackground=highlight
        )
        self.answer_submit.config(
            bg=background,
            text="Next"
        )

    def close_quiz(self):
        self.question_window.destroy()
        root.deiconify()

    def open_help(self):
        G03_help_v1.HelpGui(self)
        # Function gives the following variables
        """
        self.help_window
        Root window of help

        self.help_dismiss_button
        The dismiss button
        """

        def close():
            self.help_window.destroy()
            self.help_button.config(
                state=NORMAL
            )

        self.help_dismiss_button.config(
            command=lambda: close()
        )

    def open_export(self):
        G04_export_v1.ExportGui(self)

        def close():
            self.export_window.destroy()
            self.export_button.config(
                state=NORMAL
            )
        
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
                return True, user_input
            else:
                return False, boundary_error
        except:
            return False, num_error
        
    import re
        
    def string_checker(string, default):
        problem = False
        error = ""

        # Regular expression to check filename is valid
        valid_char = "[A-Za-z0-9_]"

        if string == "":
            return True, default

        # iterates through filename and checks each letter.
        for letter in string:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                error = "Sorry, no spaces allowed"
            else:
                error = "Sorry, no {}'s allowed".format(letter)

            problem = True
            break

        if problem:
            error = "{}. Use letters / numbers / underscores only".format(error)

        return not problem, error or string
    
class GenerateQuestion:
    def __init__(self, partner, low, high, number_count):
        self.generators = [
            self.simple_question,
            self.solve_x,
        ]

        possible_operations = [
            "+",
            "-",
            "*",
            "/",
        ]

        numbers = []
        operations = []

        for _ in range(0, number_count):
            numbers.append(random.randint(low,high))

        for i in range(0, number_count - 1):
            chosen_operation = random.choice(possible_operations)
            try:
                while chosen_operation == operations[-1]:
                    chosen_operation = random.choice(possible_operations)
            except:
                chosen_operation = random.choice(possible_operations)
            
            if chosen_operation == "/":
                numbers[i] *= numbers[i+1]
            elif chosen_operation == "^":
                numbers[i+1] = 2 # This avoids any overly complicated powers
            operations.append(chosen_operation)

        chosen_function = random.choice(self.generators)

        question, answer = chosen_function(numbers, operations)

        partner.question.set(question)
        partner.answer.set(answer)


    def solve(self, numbers, operations):
        question = self.form_question(numbers, operations)

        answer = int(eval(question))
        return answer

    def form_question(self, numbers, operations):
        question = ""

        for i in range(0, len(numbers)):
            number = 0
            operation = ""

            number = numbers[i]
            if i != len(numbers) - 1:
                operation = operations[i]

            question = f"{question}{number}{operation}"

        return question
        

    def simple_question(self, numbers, operations):
        question = self.form_question(numbers, operations)
        answer = self.solve(numbers, operations)

        return question, answer

    def solve_x(self, numbers, operations):
        # Solve original question
        new_numbers = numbers.copy()
        answer = self.solve(numbers, operations)

        index = random.randint(1, len(numbers))
        new_numbers[index-1] = "x"

        question = self.form_question(new_numbers, operations)
        question += f"={answer}"
        answer = numbers[index-1]

        return question, answer

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    QuizGame(root)
    root.mainloop()