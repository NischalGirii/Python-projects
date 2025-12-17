# Python Mini Bank Management System
# Concepts you’ll use
# dict → store users & balances
# list → transaction history
# tuple → fixed transaction records
# set → unique usernames
# if / else → conditions
# while → menu loop


users = {
    "Nischal": {
        "password": "NischalPwd",
        "balance": 25000,
        "transactions":[]
    },
    "Giri": {
        "password": "GiriPwd",
        "balance": 20000,
         "transactions":[]
    },
    "Python": {
        "password": "PythonPwd",
        "balance": 10000,
         "transactions":[]
    }
}

usersname = input("Enter your username: ")
password = input("Enter your password: ")
if usersname in users and users[usersname]["password"]==password:
    print("Validation Successful")
    while True:
        try:
            choice = int(input("\n1)Check Balance\n2)Deposit Money\n3)Withdraw Money\n4)Transaction History\n5)Exit\n"))
        except ValueError:
            print("Enter a valid number")
            continue
        match choice:
            case 1:
                print("Your current balance is: ",(users[usersname]["balance"]))
            case 2:
                deposit=int(input("Enter amount to be deposited:"))
                users[usersname]["balance"]+=deposit
                users[usersname]["transactions"].append(("Deposit", deposit, users[usersname]["balance"]))
                print("Your new balance is:",str(users[usersname]["balance"]))
            case 3:
                withdraw=int(input("Enter amount to be withdrawn:"))
                if withdraw<=users[usersname]["balance"]:
                    users[usersname]["balance"] -=withdraw
                    users[usersname]["transactions"].append(("Withdraw", withdraw, users[usersname]["balance"]))
                    print("Your new balance is:",str(users[usersname]["balance"]))
                else:
                    print("Insufficient Balance")
            case 4:
                print("Transactional History:")
                for t in users[usersname]["transactions"]:
                    print(t)

            case 5:
                print("Exiting")
                break




    

else:
    print("Invalid Credentials")
    