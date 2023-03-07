# This is the beginning of Lab 6

# 3/8/2023
# Xin Zhao


def encoder(password):
    res = ""
    for num in password:
        new_num = str((int(num) + 3) % 10)
        res += new_num

    return res


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter your password to encode: ")

            encoder(password)

            print("Your password has been encoded and stored!")

        if option == "2":
            password = input("Please enter your password to decode: ")
            print("The encoded password is", password, "and the original password is", decoder(password))

        elif option == "3":

            break

        print()


main()

