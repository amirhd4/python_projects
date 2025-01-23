# 1) user input => low and high bound
# 2) random => [a, b]
# 3) loop => condition => guess_count=5 => feedback
import random

try:
    low = int(input("Enter lower bound: \n"))
    high = int(input("Enter high bound: \n"))
    if not(high > low):
        raise Exception("The high bound must be grater than the low bound")
except TypeError as error:
    print("Please enter a valid number: ", error)

r = random.randint(low, high)

guess_count = 5

while guess_count > 0:
    try:
        new_guess_str = int(input(f"remained guess: {guess_count} => Enter your next guess: \n"))
        new_guess = int(new_guess_str)
        if new_guess == r:
            print("You won!")
            break
        elif r > new_guess:
            print("Your guess is lower than the selected guess!")
        else:
            print("Your guess is higher than the selected number!")
        guess_count -= 1
        if guess_count == 0:
            print("You lose!")
    except Exception as error:
        print("Please enter a valid number: ", error)

