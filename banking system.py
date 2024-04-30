import getpass
import random

class Banking:
    def __init__(self):
        self.name = {"20211": 12345, "20212": 20213, "210214": 56789}
        self.balance = {"20211": 10000, "20212": 1000, "210214": 100}
        self.logged_in_user = 0

    def login(self, username, password):
        if username in self.name and str(self.name[username]) == password:
            self.logged_in_user = username
            print("Login successful. Welcome, {}!".format(username))
        else:
            print("Invalid username or password. Please try again.")
            breakpoint()

    def create_account(self, random_value, new_password):
        if random_value not in self.name:
            self.name[random_value] = new_password
            self.balance[random_value] = 0
            self.logged_in_user = random_value  # Set logged_in_user to the new username
            print("Account created successfully for {}!".format(random_value))
            self.deposit_prompt(random_value)  # Prompt for deposit after account creation
        else:
            print("Username already exists. Please choose a different one.")

    def deposit_prompt(self, username):
        amount = float(input("Enter the amount to deposit for {}: $".format(username)))
        self.deposit(username, amount)

    def deposit(self, username, amount):
        if amount > 0:
            self.balance[username] += amount
            print("Deposited amount: ${}. Current balance for {}: ${}".format(amount, username, self.balance[username]))
        else:
            print("Enter a correct amount.")

    def withdrawal(self, amount):
        if self.logged_in_user:
            if amount > 0:
                if self.balance[self.logged_in_user] >= amount:
                    self.balance[self.logged_in_user] -= amount
                    print("Withdrawn amount: ${}. Current balance: ${}".format(amount, self.balance[self.logged_in_user]))
                else:
                    print("Insufficient funds.")
            else:
                print("Enter a valid amount.")
        else:
            print("Please log in first.")

    def display_balance(self):
        if self.logged_in_user:
            print("Balance for {}: ${}".format(self.logged_in_user, self.balance[self.logged_in_user]))
        else:
            print("Please log in first.")

    def account_details(self):
        if self.logged_in_user:
            print("ACCOUNT NUMBER IS : {}".format(self.logged_in_user))
            print("BALANCE : ${}".format(self.balance[self.logged_in_user]))
        else:
            print("Please log in first.")


user = Banking()

print("\t\t\t\tWELCOME TO SBI BANK")
print("1. Login")
print("2. Account Creation")

choice = input("Enter your choice (1/2): ")

if choice == '1':
    username = input("Enter your username: ").lower()
    password = getpass.getpass(prompt="Enter your password: ")
    user.login(username, password)

elif choice == '2':
    random_value = random.randint(10000, 99999)
    print("YOUR ACCOUNT NUMBER IS : ", random_value)
    new_password = getpass.getpass(prompt="Enter a new password: ")
    user.create_account(random_value, new_password)

else:
    print("Invalid choice.")

while True:
    print("\nCHOOSE AN OPTION FOR YOUR PROCESS2:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Account Details")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        if user.logged_in_user:
            amount = float(input("Enter the amount to deposit: $"))
            user.deposit(user.logged_in_user, amount)
        else:
            print("Please log in first.")

    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: $"))
        user.withdrawal(amount)

    elif choice == '3':
        user.display_balance()

    elif choice == '4':
        user.account_details()

    elif choice == '5':
        print("Thank you for using SBI BANK. Have a great day!")
        break

    else:
        print("Invalid choice.")

    again = input("DO YOU WANT TO PERFORM MORE PROCESS ?").lower()
    if again == "no":
        print("THANK YOU FOR USING SBI BANK,SEE YOU AGAIN :)")
        break
    elif again != "yes":
        print("PLEASE ENTER A VALID CHOICE")
