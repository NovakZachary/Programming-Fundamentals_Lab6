

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
                print("Encoded password: ", encode(input("Enter password to encode: ")))
            case 2:
                pass  # TODO PUT CALL TO DECODE METHOD HERE
            case 3:
                break


if __name__ == "__main__":
    main()

