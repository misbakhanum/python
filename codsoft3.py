import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_characters = string.punctuation if use_special else ''

    # Combine all characters
    all_characters = lowercase + uppercase + digits + special_characters

    # Ensure at least one character from each selected category is included
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special_characters))

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - len(password))

    # Shuffle the password to avoid predictable sequences
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Password Generator")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 6): "))
            if length < 6:
                print("Password length should be at least 6 characters.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Ask user for complexity preferences
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        # Generate the password
        password = generate_password(length, use_uppercase, use_digits, use_special)
        print(f"Generated Password: {password}")

        # Check if the user wants to generate another password
        next_generation = input("Do you want to generate another password? (yes/no): ")
        if next_generation.lower() != 'yes':
            break

if __name__ == '__main__':
    main()
