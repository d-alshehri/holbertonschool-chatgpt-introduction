class Checkbook:
    def __init__(self):
        self.balance = 0.0

    # Function description:
    # This function deposits a given amount into the account, updating the balance.
    # It also prints the amount deposited and the updated balance.

    # Parameters:
    # - amount (float): The amount to be deposited into the account.
    #
    # Returns:
    # - None
    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    # Function description:
    # This function withdraws a given amount from the account, updating the balance.
    # If there are insufficient funds, it prints an error message.

    # Parameters:
    # - amount (float): The amount to be withdrawn from the account.
    #
    # Returns:
    # - None
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    # Function description:
    # This function prints the current balance in the account.

    # Parameters:
    # - None
    #
    # Returns:
    # - None
    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
