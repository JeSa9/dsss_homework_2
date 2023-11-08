import unittest
from math_quiz import generate_random_integer, random_operator_choice, execute_arithmetic_calculation


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator_choice(self):
        # Test if an operator is seleced randomly
        for _ in range(1000):  # Test a large number of random values
             operator = random_operator_choice()
             self.assertIn(operator, ['+', '-', '*'])
        

    def test_execute_arithmetic_calculation(self):
        # Test the calculation of the cases 
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (2, 3, '*', '2 * 3', 6),
                (68, 10, '-', '68 - 10', 58),
                (35, 90, '+', '35 + 90', 125),
                (24, 6, '*', '24 * 6', 144),
                (99, 99, '-', '99 - 99', 0)
                (10, 12, '-', '10 - 12', -2)
                (0, 2, '*', '0 * 2', 0)
                (285, 856, '+', '285 + 856', 1141)
                (442, 14, '*', '442 * 14', 6188)  
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = execute_arithmetic_calculation(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
            

if __name__ == "__main__":
    unittest.main()
