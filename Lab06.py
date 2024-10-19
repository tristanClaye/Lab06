def encode(password):
    encoded_password = ''
    for char in password: #loops through each character of the password
        encoded_digit = (int(char) + 3) % 10 #changes characters to ints then shifts by 3
        encoded_password += str(encoded_digit)
    return encoded_password #returns encoded pass


def decode(encoded_password):
    pass

def main():
    encoded_password = None #variable to store encoded password

    while True:
        print("\nMenu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("\nPlease enter an option: ") #takes in users menu choice

        if choice == '1':
            password = input("Please enter your password to encode: ") #prompt user for password
            if len(password) == 8 and password.isdigit():
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            else: #if password doesnt meet requirements, display invalid message
                print("Invalid password. Please enter an 8-digit numeric password.")

        elif choice == '2':
            if encoded_password: #checks if encoded password is stored
                original_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
            else:
                print("No encoded password found. Please encode a password first.")

        elif choice == '3': #quits program
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
