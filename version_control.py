def decode(password):
    # Will Crowell
    result = ''
    for i in password:
        if int(i) <= 2:
            result += str(int(i)+7)
        else:
            result += str(int(i) - 3)
    return result

def encode(password):
    # Zachary Novak
    result = ''
    for i in password:
        result += str((int(i) + 3) if (int(i) <= 6) else (int(i)+3-10))
    print("Encoded password: ",result)
    return result

def print_menu():
    print("MENU")
    print("1. Encode password\n2. Decode password\n3. Exit")

def main():
    while True:
        print_menu()
        match int(input()):
            case 1:
                # I changed this part because we need to capture the input to use for decoding in case 2
                print("Please enter your password to encode:", end="")
                encoded_password = encode(input())
                print("Your password has been encoded and stored!")
            case 2:
                # William Crowell
                print(f'The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.')
            case 3:
                break


if __name__ == "__main__":
    main()

