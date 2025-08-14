import random
import string

def Password_Generator(length):
    if length < 4:
        print("Password length should be at least 4 characters for strong security.")
        return 0
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    special = string.punctuation

    password = [random.choice(lower), random.choice(upper), random.choice(digit), random.choice(special)]

    every_character = lower + upper + digit + special

    password += random.choices(every_character,k=length - 4)

    random.shuffle(password)

    return "".join(password)

try:
    length = int(input("Enter the desired password length: "))
    password = Password_Generator(length)
    if password:
        print("Generated Password:",password)
except:
    print("Please enter a numeric value.")