"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        float: The interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    cd_account = Account(balance, interest_rate)

    # Calculate interest earned
    # ADD YOUR CODE HERE
    interest_earned = cd_account.balance * (cd_account.interest_rate / 100) * (months / 12) 

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
# Calculate the updated balance by adding the interest earned to the current balance
# Create a CD account using the `create_cd_account` function
# ADD YOUR CODE HERE
balance = 1000  # Replace 1000 with the desired initial balance
interest_rate = 2.5  # Replace 2.5 with the desired interest rate
months = 12  # Replace 12 with the desired number of months

cd_account, interest_earned = create_cd_account(balance, interest_rate, months)

# Update the CD account balance by passing the interest earned to the `set_balance` method
# ADD YOUR CODE HERE
cd_account.set_balance(cd_account.balance + interest_earned)

# Pass the interest_earned to the set interest method using the instance of the CDAccount class.
# ADD YOUR CODE HERE
cd_account.set_interest(interest_earned)

# Return the updated balance and interest earned.
def get_cd_account_details(cd_account, interest_earned):
    # ADD YOUR CODE HERE
    return cd_account.balance, interest_earned

print(get_cd_account_details(cd_account, interest_earned))

