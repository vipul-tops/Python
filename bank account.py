class Bank:

    def openAccount(self,cname,balance,acno):
        self.cname=cname
        self.balance=balance
        self.acno=acno
        print("Hello",self.cname,",Your Account Number",acno,",Is Your Account Opened with Balance : ",balance)
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            self.needs=amount-self.balance
            print("Sorry You need another ",self.needs,"Rs.")
    def checkBalance(self):
        print("Current Balance : ",self.balance)
b1=Bank()
cname=input("Enter Customer Name : ")
balance=int(input("Enter Initial balance : "))
acno=int(input("Enter Account Number : "))

b1.openAccount(cname,balance,acno)

while True:

    print("*************************")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*************************")
    choice=int(input("Enter Your Choice : "))
    print("**************************")

    if choice==1:
        amount=int(input("Enter Deposit Amount : "))
        b1.deposit(amount)
        print("*************************")
    elif choice==2:
        amount=int(input("Enter Withdraw Amount : "))
        b1.withdraw(amount)
        print("***************************")
    elif choice==3:
        b1.checkBalance()
        print("**************************")
    else:
        print("Thank You for Using Our Service")
        break

    
    
