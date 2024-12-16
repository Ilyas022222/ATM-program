balance = 2000  #the current balance in the account
transactions = [] #empty list that which will later on store transaction history
pin = "1234"  #the current pin to access the bank


def check_balance(): # this function displays the current balance
    print(f"Your current balance is £{balance}")

def deposit(): # this function lets user deposit money
    global balance  # global updates the variable
    amount = float(input("Enter the amount you wish to deposit: £"))
    if amount > 0:
        balance += amount
        transactions.append(f"You have deposited £{amount} into your account.")
    #Adds the deposit action to the transactions list for history every time. transaction.appends will reoccur again.

        print(f'£{amount} has been deposited successfully!')
    else:
        print('Invalid amount. Please try again.')


def withdraw(): #this function allows users to withdraw money and allows custom withdraws
    global balance
    print("Select an amount to withdraw: ")
    print("1: £10")
    print("2: £20")
    print("3: £50")
    print("4: £100")
    print("5: £200")
    print("6: Enter a custom amount")

    choice = input("Please select your option (1-6): ")

    if choice in ["1", "2", "3", "4", "5"]:

        fixed_amounts = {"1": 10, "2": 20, "3": 50, "4": 100, "5": 200}
        amount = fixed_amounts[choice]
    elif choice == "6":
        # Allows user to input the amount they want
        amount = float(input("Enter the amount you wish to withdraw: £"))
    else:
        print("Invalid option. Please try again.")
        return  # Exit the function if the input is invalid

    # Check if the withdrawal amount is valid
    if 0 < amount <= balance:
        balance -= amount
        transactions.append(f"You have withdrawn £{amount} from your account.")
        print(f'£{amount} has been withdrawn successfully')
    elif amount > balance:
        print('Insufficient funds.')
    else:
        print("Invalid amount. Please try again.")
        #f the withdrawal amount is invalid (e.g., negative or zero), an error message is shown.


def view_transactions():    # prints the history of transactions
    if transactions:
        print('Transaction History:')
        for transaction in transactions:  #if true, it prints each transaction.
            print(transaction)
    else:
        print('No transactions have been made yet.')   # if no transactions have been made then a message will appear


def authenticate_user():

    attempts = 3    #The amount of attempts the user is allowed to enter
    while attempts > 0:
        entered_pin = input("Please enter your PIN: ")
        if entered_pin == pin:
            print("Access granted")    #If correct access is granted.
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. You have {attempts} attempts left.")
         #If incorrect, the number of attempts is reduces and an error message is shown.

    print("Too many incorrect attempts. Access denied, Goodbye.")
    return False   #If user gets pin incorrect after 3 times then access is denied

def main_menu():
    # calls functions of (check_balance(), deposit(), withdraw(), view_transactions()
    if authenticate_user():
        while True:
            print("Welcome to the main menu")
            print("1: Check current balance")
            print("2: Deposit money")
            print("3: Withdraw money")
            print("4: View transaction history")
            print("5: Exit")

            choice = input("Please select your option: ")
            if choice == "1":
                check_balance()

            elif choice == "2":
                deposit()

            elif choice == "3":
                withdraw()

            elif choice == "4":
                view_transactions()

        # if user selects "5" then the program should print thank you then the programs should exit the loop
            elif choice == "5":
                print("Thank you for using this cash machine.")
                break

            else:
                print("Invalid, Please try again.")
    # if an invalid option is selected then an error message will print


# Call the main menu function to start the program
main_menu()              
