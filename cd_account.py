# Import the Account class from Account.py
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        Account: The updated CD account object after adding the interest earned.
        float: The interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    cd_account = Account(balance, interest_rate)

    # Calculate interest earned
    interest_earned = cd_account.balance * (cd_account.interest_rate / 100) * (months / 12)

    # Update the CD account balance by adding the interest earned
    updated_balance = cd_account.balance + interest_earned

    # Update the account balance using the set_balance method
    cd_account.set_balance(updated_balance)

    # Return the updated CD account object and interest earned.
    return cd_account, interest_earned

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
    cd_account = Account(balance, interest_rate)

    # Calculate interest earned
    interest_earned = cd_account.balance * (cd_account.interest_rate / 100) * (months / 12)

    # Update the CD account balance by adding the interest earned
    updated_balance = cd_account.balance + interest_earned

    # Return the updated balance and interest earned
    return updated_balance, interest_earned
# Define a function to get CD account details
def get_cd_account_details(cd_account, interest_earned):
    """Get CD account details including balance and interest earned.

    Args:
        cd_account (Account): The CD account object.
        interest_earned (float): The interest earned on the CD account.

    Returns:
        float: The CD account balance.
        float: The interest earned.
    """
    return cd_account.balance, interest_earned
