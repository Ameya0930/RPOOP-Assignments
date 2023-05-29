
import random 
r1=random.randint(1000000,2000000)
r2=random.randint(1000,10000)

class Bank_Account:

    def _init_(self,name,account_type,):
        self.name = name
        self.account_number = r1
        self.account_type = account_type
        self.balance = r2
        
    def display(self):
        print(f"Welcome {self.name}")
        print()    
        print("Following are the details of your bank account ")
        print(f"Name: {self.name}")
        print(f"Account number: {r1}")
        print(f"Account type: {self.account_type}")
        print(f"Balance: {r2}$")
        
    def check_balance(self):
        min_balance = 2000
        if self.balance >= min_balance:
            print(f"Bank Balance = {self.balance}$")
        else:
            print(f"Your bank balance is {self.balance}$, which is lower than minimum amount required")
            
    def deposit(self):
        amount=int(input("Please the enter the amount to be deposited :"))
        self.balance = self.balance+amount
        print(f"Amount deposited {amount}$. New Account balance is {self.balance}$.")

    def withdraw(self):
        amount=int(input("Please the enter the withdraw amount :"))
        if self.balance >= amount:
            self.balance = self.balance-amount
            print(f"Amount withdrew {amount}$. New Account balance is {self.balance}$.")
        else:
            print("You have low bank balance , Amount cannot be withdrawn !!")

print("Do you want to create account? press 1 if yes 2 if no")
g=int(input("Enter you response : "))
if(g==1):
    a=str(input("Please Enter your name :"))
    print(""""account type:
              savings : 1
              current : 2""")
    l=int(input("Please Enter your account type response :"))
    if (l==1):
        c="savings"
    elif (l==2) :
        c="current"
    else:
        print("Please enter a valid response")
        if (l==1):
            c="savings"
        elif (l==2) :
            c="current"


    # acc1=Bank_Account(a,c)
    # print()

    z=1
    while (z!=0): 
        print()
        print("""press following number for respective procesess        
              Account details - 1
              Check Balance - 2
              deposit - 3
              withdraw -4
              """)

        y=int(input("Please Enter your response :"))
        print()
        if (y==1):
            acc1.display()
            print()
            print("if you are satisfied then press 0, else for further processes press 1")
            p=int(input("Enter your response : "))
            print()
            z=p

        if (y==2):

            acc1.check_balance()
            print()
            print("if you are satisfied then press 0, else for further processes press 1")
            p=int(input("Enter your response : "))
            print()
            z=p

        if (y==3):

            acc1.deposit()
            print()
            print("if you are satisfied then press 0, else for further processes press 1")
            p=int(input("Enter your response : "))
            print()
            z=p
        if(y==4):
            acc1.withdraw()
            print()
            print("if you are satisfied then press 0, else for further processes press 1")
            p=int(input("Enter your response : "))
            print()
            z=p
    print()   
    print("Thank you, please don't share transaction details with anyone else ")
elif(g==2):
    print("please open an bank account")
else:
    "please give a valid response"
