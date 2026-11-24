import random
import string

def generate_password():
    try:
        password_length = int(input("Enter password length: "))

        if password_length <= 0:
            print("Password length must be greater than 0.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation

        password = ""

        for i in range(password_length):
            password += random.choice(characters)

        print(f"Generated Password: {password}")

    except ValueError:
        print("Please enter a valid number!")

def check_password_strength():
    password = input("Enter your password: ")

    has_length = len(password) >= 8
    has_digit = any(char.isdigit() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    strength_score = 0

    if has_length:
        strength_score += 1

    if has_digit:
        strength_score += 1

    if has_uppercase:
        strength_score += 1

    if has_symbol:
        strength_score += 1

    if strength_score == 4:
        print("Password Strength: Strong")

    elif strength_score >= 2:
        print("Password Strength: Medium")

    else:
        print("Password Strength: Weak")

def main():
    while True:
        print("\n===== PASSWORD TOOL =====")
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            generate_password()

        elif choice == "2":
            check_password_strength()

        elif choice == "3":
            print("Thank you for using Password Tool!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")

main()