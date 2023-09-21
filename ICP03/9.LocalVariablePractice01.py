# Function to withdraw money
def withdraw(money):
    global balance
    if balance - money < 0:
        return -1
    else:
        balance = balance - money
        return

# Function to deposit money
def deposit(money):
    global balance
    balance = balance + money

# Main program
balance = int(input("Enter the initial balance: "))
money = int(input("Enter the deposit amount: "))
deposit(money)
print("Current balance is", balance)

money = int(input("Enter the withdrawal amount: "))
if withdraw(money) == -1:
    print("Insufficient balance for withdrawal.")
else:
    print("Current balance is", balance)
