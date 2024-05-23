import random

class GenerateQuestion:
    def __init__(self, low, high, number_count):
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