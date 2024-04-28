import getpass 
class Banking:
    def __init__(self):
        self.name = {"thejas": 12345,"navdeep": 23456,"suresh": 56789}
        self.logedin_users = 0
        self.balance = {"thejas": 10000,"navdeep": 1000 ,"suresh": 100 }

    def login(self, username, password):
        if username in self.name and str(self.name[username]) == password:
            self.logedin_users = username
            print("Login successful. :)")
        else:
            print("Invalid password or username :(")
            print("PLEASE LOGIN AGAIN")
            breakpoint()

        

    def deposit(self,amount):
        if self.logedin_users:
            if amount > 0:
                if self.balance[self.logedin_users] >=amount:
                   self.balance[self.logedin_users] += amount
                   print("deposited amount is ",amount,"current balance is ",self.balance[self.logedin_users])
                else:
                    print("Insufficient funds.")
            else:
                print("ENTER A CORRECT AMOUNT :)")
        else:
            print("LOGIN ERROR,PLEASE LOGIN FIRST")

    def withdrawal(self,withdraw):
        if self.logedin_users:
            if withdraw > 0:
                if self.balance[self.logedin_users] > withdraw:
                   self.balance[self.logedin_users] -= amount
                   print("WITHDRAW AMOUNT IS :",amount,"CURRENT BALANCE IS :",self.balance[self.logedin_users])
                else:
                    print("INSUFICIENT AMOUNT :(")
                    print("PLEASE LOGIN AGAIN")
            else:
                print("ENTER A VALID AMOUT")

    def display_balance(self):
        if self.logedin_users:
            print("BALANCE = ",self.balance[self.logedin_users])

    def account_details(self):
        print("USERNAME IS : ",name.upper())
        print("PASSWORD IS : ",password)
        print("BALANCE AMOUNT : ",self.balance[self.logedin_users], "$")


user = Banking()
print("\t\t\t\t\tWELCOME TO SBI BANK" )

name = str(input("ENTER THE USERNAME : ")).lower()
password = getpass.getpass(prompt="ENTER THE PASSWORD : ")
user.login(name,password)

while True:
    print("\nChoose an option:")
    print("1. DEPOSIT")
    print("2. WITHDRAW")
    print("3. DISPLAY BALANCE")
    print("4. ACCOUNT DETAILS")
    print("5. EXIT")

    choise = input("ENTER YOUR CHOICE (1/2/3/4) : ")

    if choise == '1':
        print("DEPOSIT MONEY $")
        amount = float(input("ENTER THE AMOUNT TO DEPOSIT $ : "))
        user.deposit(amount)

    elif choise == '2':
        print("WITHDRAW MONEY $")
        withdraw = int(input("ENTER THE AMOUNT TO WITHDRAW $ : "))
        user.withdrawal(withdraw)

    elif choise == '3':
        print("DISPLAY BALANCE")
        user.display_balance()

    elif choise == '4':
        print("ACCOUNT DETAILS")
        user.account_details()

    elif choise == '5':
        print("THANK YOU FOR USING SBI BANK,SEE YOU AGAIN :)")
        break

    again = input("DO YOU WANT TO PERFORM MORE PROCESS ?").lower()
    if again == "no":
        print("THANK YOU FOR USING SBI BANK,SEE YOU AGAIN :)")
        break
    elif again != "yes":
        print("PLEASE ENTER A VALID CHOICE")
