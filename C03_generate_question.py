import random

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