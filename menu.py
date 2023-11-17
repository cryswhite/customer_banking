# Show main menu to user and provide options to select from the menu
import customer_banking

def show_main_menu():
    print("Welcome to the Customer Banking System")
    print("1. Create Savings Account")
    print("2. Create CD Account")
    print("3. Exit")
    return input("Enter your choice: ")

# Prompt the user to select an option from the main menu and call the appropriate function
def main():
    while True:
        choice = show_main_menu()

        if choice == '1':
            print("Creating Savings Account...")
            balance = float(input("Enter savings balance: "))
            interest_rate = float(input("Enter interest rate: "))
            months = int(input("Enter the number of months: "))
            updated_balance, interest_earned = customer_banking.create_savings_account(balance, interest_rate, months)
            print(f"Updated Balance: {updated_balance}, Interest Earned: {interest_earned}")

        elif choice == '2':
            print("Creating CD Account...")
            balance = float(input("Enter CD balance: "))
            interest_rate = float(input("Enter interest rate: "))
            months = int(input("Enter the number of months: "))
            updated_balance, interest_earned = customer_banking.create_cd_account(balance, interest_rate, months)
            print(f"Updated Balance: {updated_balance}, Interest Earned: {interest_earned}")

        elif choice == '3':
            print("Exiting the Customer Banking System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
