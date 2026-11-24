
import random
import string

def generate_password():
    length = int(input("Enter password length: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)


def check_password():
    password = input("Enter password: ")

    if (len(password) >= 8 and any(c.isdigit() for c in password)
        and any(c.isupper() for c in password)
        and any(c in string.punctuation for c in password)):
        print("Strong")
    elif len(password) >= 8:
        print("Medium")
    else:
        print("Weak")


while True:
    print("\n1. Generate Password")
    print("2. Check Strength")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        generate_password()
    elif choice == "2":
        check_password()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
