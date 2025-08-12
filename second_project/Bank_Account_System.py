class bankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def createAccount(self,name,balance):
        self.name=name
        self.balance=balance

    def deposite(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"{amount} Deposited Successfully ")
        else:
            print("Deposite amount must be positive.")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Withdraw amount: {amount}")
        elif amount<=0:
            print("Withdraw amount must be positive.")
        else:
            raise ValueError("Insufficient balance")
    @property
    def check_balance(self):
        return self.balance
    

    def __str__(self):
        return f"Account Holder: {self.name} |Current Balance: {self.balance}"
    



print("Welcome to Small bank Account System\nEnter your choice(number)\n1.Create Account\n2.Deposite\n3.With-Draw\n")
try:
    choice=int(input(""))
    if choice >3 or choice<1:
        print("Choose choice 1. or 2. or 3.")

    # create account
    if choice == 1:
        name=input("Enter name: ")
        balance=int(input("Enter balance: "))
        if balance<=0:
            print("Enter valid balance")
        else:
            acc = bankAccount(name,balance)
            acc.createAccount(name,balance)
            print(f"Account Created Successfully\n\n{acc}")
    # deposite
    elif choice == 2:
        name=input("Enter name: ")
        balance=int(input("Enter balance: "))
        if balance<=0:
            print("Enter valid balance")
        else:
            amount=int(input("Enter amount of deposite"))
            acc= bankAccount(name,balance)
            acc.deposite(amount)
            print(acc)

    # withdraw
    elif choice == 3:
        name=input("Enter name: ")
        balance=int(input("Enter balance: "))
        if balance<=0:
            print("Enter valid balance")
        else:
            amount=int(input("Enter amount of withdraw"))
            acc= bankAccount(name,balance)
            acc.withdraw(300)
            print(acc)
        
except ValueError:
    print("Enter a valid number please.")
    