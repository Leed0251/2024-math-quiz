from tkinter import *
from functools import partial # To prevent unwanted windows
import re
import math
import datetime
import random
import pandas

import G01_select_questions_v1
import G02_quiz_v1
import G03_help_v1
import G04_export_v1

class QuizGame:
    def __init__(self, root):
        # Create the GUI Frame
        self.selection = G01_select_questions_v1.Gui(root)

        # Class contains these important variables
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

        self.selection.enter_button.config(
            command=lambda: self.check_input(1, 1000)
        )

    def check_input(self, min, max):
        num = self.selection.number_box.get()
        result, errMessage = self.check_num(num, min, max)

        if result:
            # User input was valid
            self.question_count = IntVar()
            self.question_count.set(int(num))
            
            self.selection.error_frame.grid_forget()
            self.selection.error_label.config(text=errMessage)
            
            self.load_quiz()
        else:
            # User input was not valid
            self.selection.error_frame.grid(row=3)
            self.selection.error_label.config(text=errMessage)

    def load_quiz(self):
         # Load main quiz
        self.quiz_window = G02_quiz_v1.QuestionFrame(self, root)
        # Class contains these important variables
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

        # If users press cross at top, closes quiz and opens first gui
        self.quiz_window.question_window.protocol('WM_DELETE_WINDOW',
            partial(self.close_quiz)
        )

        self.question_number = IntVar()
        self.question = StringVar()
        self.answer = IntVar()

        self.correct_answers = IntVar()
        self.incorrect_answers = IntVar()
        self.questions_answered = []

        # help button
        self.quiz_window.help_button.config(
            command=lambda: self.open_help()
        )

        # export button
        self.quiz_window.export_button.config(
            command=lambda: self.open_export()
        )

        # start over button
        self.quiz_window.start_over_button.config(
            command=lambda: self.close_quiz()
        )

        self.next_question()

    def next_question(self):
        if self.question_number.get() == self.question_count.get():
            self.show_response("Complete", "#FFFFFF", "#000000")
            self.quiz_window.submit_frame.grid_forget()
            return
        
        self.show_response("", "#FFE6CC", "#D79B00")
        
        self.quiz_window.answer_submit.config(
            command=lambda: self.check_answer(),
            text="Enter"
        )
        self.quiz_window.response_frame.grid_forget()
        self.quiz_window.answer_container.grid(padx=5, pady=5, row=0)
        
        self.quiz_window.answer_box.delete(0, "end")
        self.question_number.set(self.question_number.get() + 1)
        self.quiz_window.question_label.config(text=f"Question {self.question_number.get()}/{self.question_count.get()}")
        # Generate new question for user to solve
        GenerateQuestion(self, 1, 15, 3)

        self.quiz_window.question_display.config(
            text=self.question.get()
        )

    def check_answer(self):
        user_answer = self.quiz_window.answer_box.get()
        result, returned_value = self.check_num(user_answer, -math.inf, math.inf)
        
        # Abort function if input was not valid
        if not result:
            self.quiz_window.quiz_error_frame.grid(row=3)
            self.quiz_window.quiz_error_label.config(
                text=returned_value
            )
            return
        
        # Hide error message
        self.quiz_window.quiz_error_frame.grid_forget()
        
        self.quiz_window.answer_container.grid_forget()
        self.quiz_window.response_frame.grid(padx=5, pady=5, row=0)

        # Record the question and answer
        self.questions_answered.append([self.question.get(), str(self.answer.get()), user_answer])

        # Check users answer
        if returned_value == self.answer.get():
            self.correct_answers.set(self.correct_answers.get() + 1)
            self.show_response("Correct", "#D5E8D4", "#82B366")
        else:
            self.incorrect_answers.set(self.incorrect_answers.get() + 1)
            self.show_response("Incorrect", "#F8CECC", "#B85450")
        
        if self.question_number.get() == self.question_count.get():
            self.quiz_window.answer_submit.config(text="Finish")

        # Activate export button
        self.quiz_window.export_button.config(
            state=NORMAL
        )

        self.quiz_window.answer_submit.config(
            command=lambda: self.next_question()
        )

    def show_response(self, text, background, highlight):
        self.quiz_window.response_frame.config(
            bg=background,
            highlightbackground=highlight
        )
        self.quiz_window.response_label.config(
            bg=background,
            text=text
        )
        self.quiz_window.submit_frame.config(
            bg=background,
            highlightbackground=highlight
        )
        self.quiz_window.answer_submit.config(
            bg=background,
            text="Next"
        )

    def close_quiz(self):
        self.quiz_window.question_window.destroy()
        root.deiconify()

    def open_help(self):
        self.help_window = G03_help_v1.HelpGui(self)
        # Class contains these important variables
        """
        self.help_window
        Root window of help

        self.help_dismiss_button
        The dismiss button
        """

        def close():
            self.help_window.help_window.destroy()
            self.quiz_window.help_button.config(
                state=NORMAL
            )

        self.help_window.help_window.protocol('WM_DELETE_WINDOW', close)

        self.help_window.dismiss_button.config(
            command=close
        )

    def open_export(self):
        self.export_window = G04_export_v1.ExportGui(self)
        # Class contains these important variables
        """
        self.export_window
        The root window

        self.content_label
        Displays the user what they are exporting

        self.filename_box
        Where the user inputs their file name

        self.export_dismiss_button
        Button the user clicks to close the window

        self.export_success_button
        Button the user clicks to export their results

        self.error_label
        Displays to the user when there is invalid input
        """

        def close():
            self.export_window.export_window.destroy()
            self.quiz_window.export_button.config(
                state=NORMAL
            )

        self.export_window.export_window.protocol('WM_DELETE_WINDOW', close)

        self.export_window.export_dismiss_button.config(
            command=close
        )

        display = self.format_results([self.questions_answered[-1]])

        # Display stats
        displaying = ""
        for index, value in enumerate(display):
            if index > 0:
                displaying = displaying + "\n"
            displaying = displaying + f"{value[0]:22s} {value[1]:18s} {value[2]:18s}"

        self.export_window.content_label.config(
            text=displaying
        )

        self.export_window.export_success_button.config(command=lambda: self.export_results())

    def format_results(self, displaying):
        correct = self.correct_answers.get()
        incorrect = self.incorrect_answers.get()

        exporting = [["Question", "Correct answer", "User answer"]]
        exporting.extend(displaying) # Questions answered
        exporting.append(["","",""]) # This creates a gap
        exporting.append(["Total correct:", str(correct), ""])
        exporting.append(["Total incorrect:", str(incorrect), ""])
        exporting.append(["Score:", f"{round(correct / (correct + incorrect) * 100)} / 100", ""])

        return exporting

    def export_results(self):
        # Check file name input
        date = datetime.datetime.today().strftime('%Y_%m_%d')
        success, file_name = self.string_checker(self.export_window.filename_box.get(), f"{date}_Results")
        self.export_window.export_success_button.config(text="Export")

        if success:
            # Hide error message
            self.export_window.error_label.grid_forget()
            # Export results
            data = self.format_results(self.questions_answered)
            df = pandas.DataFrame(data)

            df.to_csv(f"{file_name}.csv", header=False, index=False)

            self.export_window.export_success_button.config(text="Success")
        else:
            self.export_window.error_label.config(
                text=file_name # In this case, file_name is an error message
            )
            self.export_window.error_label.grid(row=5, sticky="we", padx=5, pady=5)
        
        
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
    
    @staticmethod
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
        # List of functions
        self.generators = [
            self.simple_question,
            self.solve_x,
        ]

        possible_operations = [
            "+",
            "-",
            "*",
            "/"
        ]

        numbers = []
        operations = []

        # Adds random numbers into the numbers list
        for _ in range(0, number_count):
            numbers.append(random.randint(low,high))

        # Adds random operations to the operations list
        for i in range(0, number_count - 1):
            chosen_operation = random.choice(possible_operations)
            try:
                while chosen_operation == operations[-1]:
                    chosen_operation = random.choice(possible_operations)
            except:
                chosen_operation = random.choice(possible_operations)
            
            # Multiples the number to the left of any "/" by the value to the right
            if chosen_operation == "/":
                numbers[i] *= numbers[i+1]
            operations.append(chosen_operation)

        # Runs numbers and operations through a random generator function
        # Either solve x or basic
        chosen_function = random.choice(self.generators)

        question, answer = chosen_function(numbers, operations)

        partner.question.set(question)
        partner.answer.set(answer)

    # Solves questions from the numbers and operations lists
    def solve(self, numbers, operations):
        question = self.form_question(numbers, operations)

        answer = int(eval(question))
        return answer

    # Takes numbers and operations, output a readable equation
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
        
    # Gives basic questions
    def simple_question(self, numbers, operations):
        question = self.form_question(numbers, operations)
        answer = self.solve(numbers, operations)

        return question, answer

    # Gives solve x questions
    def solve_x(self, numbers, operations):
        # Solve original question
        new_numbers = numbers.copy()
        answer = self.solve(numbers, operations)

        # Replace random number with x
        index = random.randint(1, len(numbers))
        new_numbers[index-1] = "x"

        # Form a new question
        question = self.form_question(new_numbers, operations)
        question += f"={answer}"
        answer = numbers[index-1]

        # Return the new question and the original value of now "x"
        return question, answer

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    QuizGame(root)
    root.mainloop()