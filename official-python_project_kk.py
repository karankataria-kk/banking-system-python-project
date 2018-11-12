balance = 0
balance = float(balance)
money = 5000
money = float(money)
loop = 1

def menu():
    money = int(5000)
    money = float(money)
    print ("Welcome to the Python Bank System")
    print ("Your Transaction Options Are:")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("1) Deposit Money")
    print ("2) Withdraw Money")
    print ("3) Check Balance")
    print ("4) Quit Python Bank System")
    choice=int(input ("Choose your option: "))
    return choice
def deposit(balance):
    d = input("How much: $")
    d = float(d)
    balance = d + balance
    balance = float(balance)
    print ("You've successfully deposited $", deposit, "into your account.")
    print (bank_balance(balance))
    return balance
def withdrawl(balance):
    r=int(input("enter the amount to withdraw from bank account"))
    if(r > balance):
        print("Insufficient balance")
        return
    else:
        print("please collect cash Rs",r)
        balance=balance-r
    return balance
def bank_balance(balance):
    print ("Balance: Rs", balance)
    return balance
while(loop!=0):
    choice = menu()
    if (choice==1):
        balance = deposit(balance)
    elif (choice==2):
        balance = withdrawl(balance)
    elif (choice==3):
        balance = bank_balance(balance)
    elif (choice==4):
        loop=0
print ("Thank-You for stopping by the bank!")
