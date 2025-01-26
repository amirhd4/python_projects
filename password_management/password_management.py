from cryptography.fernet import Fernet


def my_dec(func):
    def wrapper(*args, **kwargs):
        # before
        res = func(*args, **kwargs)
        # after
        return res

    return wrapper


@my_dec
def input_strip(*args, **kwargs):
    return input(*args, **kwargs).strip()


# def write_key():
#     key = Fernet.generate_key()
#     with open("./key.key", "wb") as f:
#         f.write(key)

# write_key()
def load_key():
    with open("./key.key", "rb") as f:
        return f.read()


key = load_key()
fernet = Fernet(key)


def add_pass(username: str, password: str):
    try:
        with open("./passwords.txt", "a") as f:
            encrypted_pass = fernet.encrypt(password.encode()).decode()
            f.write(f"{username}|{encrypted_pass}\n")
        print("Added!")
    except Exception as e:
        print(e)


def view_pass():
    with open("./passwords.txt", "r") as f:
        for item in f:
            item = item.rstrip()
            username, encrypted_password = item.split("|")
            print(f"username: {username} - password: {fernet.decrypt(encrypted_password).decode()}")


while True:
    user_input = input_strip("Enter the mode (v: view, a: add, q: quit): ")

    if user_input == "v":
        print("Your passwords are as follows:")
        view_pass()

    elif user_input == "a":
        print("Let's add a new username-password")

        try:
            us_name = str(input_strip("Enter new username: "))
            pass_word = str(input_strip("Enter new password: "))
            add_pass(us_name, pass_word)
        except Exception as ex:
            print(ex)

    elif user_input == "q":
        break
    else:
        print("Wrong mode!")
