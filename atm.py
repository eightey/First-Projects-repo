account = {
    "name": "John",
    "balance": 500,
    "password": 1234
}

menu_opt = ""

while menu_opt != 4:

    menu_opt = int(input(
        "Hello!\n"
        "1. Check balance\n"
        "2. Withdraw cash\n"
        "3. Deposit\n"
        "4. Exit\n"
    ))

    if menu_opt == 1:

        psswd = int(input("Enter your password: "))

        if psswd == account["password"]:
            print("Current balance:", account["balance"])

        else:
            print("Wrong password")

    elif menu_opt == 2:

        cash_withdraw = int(input("Enter amount: "))
        psswd = int(input("Enter your password: "))

        if psswd == account["password"]:

            if cash_withdraw <= account["balance"]:

                account["balance"] -= cash_withdraw

                print("Withdrawal successful")
                print("Remaining balance:", account["balance"])

            else:
                print("Insufficient balance")

        else:
            print("Wrong password")

    elif menu_opt == 3:

        cash_deposit = int(input("Enter amount: "))
        psswd = int(input("Enter your password: "))

        if psswd == account["password"]:

            account["balance"] += cash_deposit

            print("Deposit successful")
            print("Current balance:", account["balance"])

        else:
            print("Wrong password")

    elif menu_opt == 4:

        print("Thank you for using our service...bye")

    else:
        print("Enter an option between 1 and 4")
 