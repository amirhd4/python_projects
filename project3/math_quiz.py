import math
import random
import decimal

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
    print(res)
    return res


question_number_limit = 5
score, question_number = 0, 0

while question_number < question_number_limit:
    # TODO: 1) generate a random question
    result = str(int((question_generator() * 100)) / 100)
    print(result)
    # TODO: 2) get user answer
    user_answer = float(input("Enter your answer: "))
    user_answer = str(int((user_answer * 100)) / 100)
    print(user_answer)
    # TODO: 3) check the answer and time
    if result == user_answer:
        score += 1
        print(f"Perfect, score: {score}")
    else:
        print(f"Sorry, the answer is wrong!")



    question_number += 1