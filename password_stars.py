password = input("Enter your password: ")
while len(password) < 8:
    print("*" * len(password))
    password = input("Enter your password: ")
