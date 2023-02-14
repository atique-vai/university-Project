# module for bank project of SD1:
#     accounts()
#     checkbalance()
#     withdrow()
#     deposit()
accountNo = 0
Name = ' '
Code = ' '
Mobile = 0
balance = 0
def Accounts() :
    accountNo = int(input("Enter account number :"))
    Name = input("Enter Your Name :")
    Code = input("Enter Branch Code ")
    Mobile = int(input("Enter Your Mobile No : "))
    balance = int(input("Enter amount to deposit"))

def ShowAccountDetails() :
    print("Account No       : ", accountNo)
    print("Name             : ", name)
    print("Bank Code        : ", Code)
    print("Total Balance    : ", balance)

def Deposit(amount):
    balance = balance + amount
    checkBalance()

def withdraw(amount):
    if(amount > balance):
        print("Your balance is low")
    else:
        balance = balance - amount
    checkbalance()

def checkbalance():
    print("Your Current Balance is        :", balance)
while(True):
    print("[1].  Create account\n[2].   Withdraw\n[3].  Deposit\n[4].   Check Balance")
    ch = int(input("Select any option   "))
    if(ch == 1):
        Accounts()
    elif(ch == 2):
        amount = int(input("Enter amount to withdraw :  "))
        withdraw(amount)
    elif(ch == 3):
        amount =  int(input("Enter amount to deposit :  "))
        Deposit(amount)
    elif ch == 4 :
        checkbalance()
    else :
        exit

