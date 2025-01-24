"""
 This math quiz is only for calculations to 2 decimal places and no more than
 2 digits are applied in the calculation.
"""

import math
import random
from decimal import *
import time
format_number = lambda number, digits: ".".join([str(number).split(".")[0], str(number).split(".")[1][0:digits]])

def reformat_number():
    rand_type = ["float", "int"]
    if random.choice(rand_type) == "float":
        rand = float(format(random.uniform(1, 10), ".2f"))
    else:
        rand = random.randint(1, 9)
    # num = float(format(rand, "0.2f"))
    # modf_num = math.modf(num)

    return rand

def question_generator():
    # generate two random numbers
    a = reformat_number()
    b = reformat_number()

    # random operator
    operator_list = ["+", "-", "*", "/"]
    selected_operator = random.choice(operator_list)
    print(f"{a} {selected_operator} {b} = ?")

    if selected_operator == "+":
        res = a + b
    elif selected_operator == "-":
        res = a - b
    elif selected_operator == "*":
        res = a * b
    else:
        res = a / b
    return res


question_number_limit = 5
score, question_number = 0, 0
time_limit = 10

while question_number < question_number_limit:
    # Done: 1) generate a random question
    result = question_generator()
    if not(float.is_integer(float(result))):
        result = format_number(result, 2)
    start_time = time.time()

    # Done: 2) get user answer
    while True:
        try:
            user_answer = float(input("Enter your answer: "))
            break
        except:
            print("Invalid answer. try again")
            continue

    if not (float.is_integer(user_answer)):
        user_answer = format_number(user_answer, 2)
    end_time = time.time()
    time_difference = end_time - start_time

    # Done: 3) check the answer and time
    if time_difference < time_limit:
        if float(result) == float(user_answer):
            score += 1
            print(f"Perfect, score: {score}\n")
        else:
            print(f"Sorry, the answer is wrong!")
    else:
        print("You are too late!")
    question_number += 1

print(f"Final score: {score} out of {question_number_limit}")