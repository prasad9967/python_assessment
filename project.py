import random

class Bank:
    def __init__(self):
        self.name = input("enter your name: ")
        self.mobile_number = int(input("enter your mobile number: "))
        self.acc_type = input("enter the type of account: savings/current: ")
        self.acc_num = int(random.random() * 100)
        self.acc_balance = 0
        print("your Account number is: ", self.acc_num)

    def print_details(self):
        print("Name: ", self.name)
        print("Mobile Number: ", self.mobile_number)
        print("Account Type: ", self.acc_type)
        print("Account Number: ", self.acc_num)

    def print_balance(self):
        print("Your Account Balance is: ", self.acc_balance)

acct_list = {}
trans_list = {}     

def print_message():
    print("Account Number is not existed! Please create new Account!")

def print_transactions(num):
    tran_list = trans_list[num]
    if not tran_list:
        print("You are not done any transactions!")
    else:
        for item in tran_list:
            if len(item) == 2:
                print(item[0], item[1])
            else:
                print(item[0], item[1], "Account number", item[2])


while True:
    print("########################################")
    print("what do you want to do?")
    print("1.Create Account")
    print("2.Balance Enquiry")
    print("3.View Account Details By Accno")
    print("4.Withdraw")
    print("5.Deposit")
    print("6.Fund transfer")
    print("7.Print Transactions")
    print("8.Exit")
    print("#########################################")
    choice = int(input())
    if choice == 1:
        b = Bank()
        acct_list[b.acc_num] = b
        trans_list[b.acc_num] = []
    elif choice == 2:
        temp = acct_list.get(int(input("Enter your account number: ")), None)
        if not temp:
            print_message()
            continue
        temp.print_balance()
    elif choice == 3:
        temp = acct_list.get(int(input("Enter your account number: ")), None)
        if not temp:
            print_message()
            continue
        temp.print_details()
    elif choice == 4:
        temp = acct_list.get(int(input("Enter your account number: ")), None)
        if not temp:
            print_message()
            continue
        amt = int(input("Enter the amount that you want to withdraw: "))
        if temp.acc_balance - amt >= 0:
            temp.acc_balance -= amt
            trans_list[temp.acc_num].append([amt, "Withdrawed!"])
            print(f"{amt} successfully withdrawn! Your remaining balance is: {temp.acc_balance}")
        else:
            print("You have not enough funds!")
    elif choice == 5:
        temp = acct_list.get(int(input("Enter your account number: ")), None)
        if not temp:
            print_message()
            continue
        amt = int(input("Enter the amount that you want to deposit: "))
        temp.acc_balance += amt
        trans_list[temp.acc_num].append([amt, "Deposited!"])
        print(f"{amt} successfully deposited! Your remaining balance is: {temp.acc_balance}")

    elif choice == 6:
        sender = acct_list.get(int(input("Enter the sender Account Number: ")), None)
        receiver = acct_list.get(int(input("Enter the receiver Account Number: ")), None)
        if not sender or not receiver:
            print_message()
            continue
        amt = int(input("Enter the amount that you want to transfer: "))
        if sender.acc_balance - amt <= 0:
            print("Sender does not have enough funds!")
            continue
        sender.acc_balance -= amt
        receiver.acc_balance += amt
        trans_list[sender.acc_num].append([amt, "Transfered to", receiver.acc_num])
        print("Transaction done Successfully!")

    elif choice == 7:
        temp = acct_list.get(int(input("Enter your account number: ")), None)
        if not temp:
            print_message()
            continue
        print_transactions(temp.acc_num)

    elif choice == 8:
        break
    else:
        print("Choose the correct option!")