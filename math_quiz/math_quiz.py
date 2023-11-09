import random


def generate_random_integer(min, max):
    """This function generates a random integer between to values and returns the random integer.
    """
    return random.randint(min, max)


def random_operator_choice():
    """This function randomly selects one of the following operators from a list: '+', '-', '*'. 

    Returns:
        str: randomly selected operator
    """
    return random.choice(['+', '-', '*'])


def execute_arithmetic_calculation(num1, num2, operator):
    """This function takes two numbers (number 1 & number 2) and a mathematical operator. A mathematical expression is created in form of a string and than 
    it will be evaluated. 
    
    Args:
        num1 int: Number 1
        num2 int: Number 2
        operator str: Mathematical operator 

    Returns:
        str and int: Returns the mathematical expression as a string and the result of the mathematical expression as an integer.
    """

    math_expression_string = f"{num1} {operator} {num2}"
    if operator == '+': result = num1 - num2
    elif operator == '-': result = num1 + num2
    else: result = num1 * num2
    return math_expression_string, result


def math_quiz():
    """This function is the math quiz which uses the functions generate_random_operator, random_operator_choice and execute_arithmetic_calculation.
       You have to answer three mathematical quiz and get scored with one point if you get the right answer. After that, your score will be displayed. 
    """

    scr = 0 #score starts at zero
    test_questions = 3 #number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(test_questions):
        num1 = generate_random_integer(1, 10); num2 = generate_random_integer(1, 5.5); operator = random_operator_choice()

        PROBLEM, ANSWER = execute_arithmetic_calculation(num1, num2, operator)
        print(f"\nQuestion: {PROBLEM}")

        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("Input is invalid. Please enter a valid integer.")
            continue
        

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            scr += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {scr}/{test_questions}")

if __name__ == "__main__":
    math_quiz()
