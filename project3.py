# Project of TIMED MATH CHALLENGE
# This project will randomly ask users Math questions that let
# them answer until they get the correct answers

import random
import time

# Constant variables
OPERATORS = ['*', '+', '-']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

# function to generate Operands and Operator
def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + ' ' + operator + ' ' + str(right)
    answer = eval(expr)

    return expr, answer

# Check accurancy of the answer
wrong = 0
input('Press "Enter" key to start')
print('-----------------------------------')

start_time = time.time()

# Loop in range of problems and ask user
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    
    while True:
        guess = input('Problem #' + str(i + 1) + ': ' + expr + ' = ')
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print('-----------------------------------')
print('Nice work! You finished in', total_time, 'seconds!')