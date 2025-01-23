import random

# 1) list of names
# 2) select of name randomly
# 3) get user char
# 4) check => show feedback
# 5) guess > 0 => win/lose

names = ["Amir", "Sina", "Mohammad", "Milad", "Hossein", "Soheil", "Amir hossein", "Shahab"]

selected_name = random.choice(names).lower()

guess_count = len(selected_name)
guess_list = ["-"] * guess_count

current_guess = " ".join(guess_list)
print(current_guess)

while guess_count > 0:
    guess_char = input("Guess a character: \n")
    if guess_char.isalpha():
        if guess_char in selected_name:
            if guess_char in guess_list:
                print("You have guessed before, try new character!\n")
            else:
                for idx, char in enumerate(selected_name):
                    if char == guess_char:
                        guess_list[idx] = guess_char
                current_guess = " ".join(guess_list)
                print(f"Perfect! => {current_guess}")

                if not("-" in guess_list):
                    print("You won!")
                    break
        else:
            guess_count -= 1
            print(f"Wrong! => remained guesses: {guess_count}")
        pass
    else:
        print("Please enter a valid character.")