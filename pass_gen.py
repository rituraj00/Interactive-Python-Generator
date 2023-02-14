import random
import string
import clipboard as c
import math



def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    # special = "@!#$%^&*()-+="
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special

    return pwd

def gen_star_string(pas_length):
    cipher_string = ""
    for _ in range(0, int(math.ceil(pas_length * 80 / 100))):
        cipher_string += "*"
    return cipher_string

def get_input():
    password_length = int(input("Enter the length you want for password: \n"))
    want_numbers = input("Do you numbers in your password ? Enter Y for Yes and N for No: \n").lower()
    want_special_chars = input("Do you special characters in your password ? Enter Y for Yes and N for No: \n").lower()

    generated_password = generate_password(password_length, (True if want_numbers == "y" else False), (True if want_special_chars == "y" else False))
    pass_to_view = generated_password[0:int((len(generated_password) * 20 / 100))] + gen_star_string(len(generated_password))
    print(f"For security reason you will see 20% of password")
    print("------------------------------------------\n")
    print(f"Password generated is: {pass_to_view}\n")
    print("------------------------------------------\n")
    c.copy(generated_password)
    print("Your password has been copied to clipboard")
    



get_input()