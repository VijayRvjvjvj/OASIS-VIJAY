import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "No character types selected. Please try again."

    password = "".join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive number for the length.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the length.")

    use_letters = input("Include letters (y/n)? ").strip().lower() == 'y'
    use_numbers = input("Include numbers (y/n)? ").strip().lower() == 'y'
    use_symbols = input("Include symbols (y/n)? ").strip().lower() == 'y'

    if not (use_letters or use_numbers or use_symbols):
        print("You must select at least one character type (letters, numbers, or symbols).")
        return

    password = generate_password(length, use_letters, use_numbers, use_symbols)

    print("Generated Password:", password)

if __name__ == "__main__":
    main()


