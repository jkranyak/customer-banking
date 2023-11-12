"""Imports the SavingsAccount class and attributes from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    savings_account = Account(balance, 0)
    # Calculate interest earned
     # ADD YOUR CODE HERE
    
    #interest_earned = balance * (interest_rate / 12) * months
    #or
    #interest_earned = ((balance * (1 + interest_rate)**months) - balance))
    #this formula needs work, it requires a few extra variables, the formula would technically be the following;
    # amount = principle * (1 + interest(whole number) / 100) ** months then the amount - principle is the compounded interest
    interest_earned = balance * (interest_rate / 100 * months / 12)
    #if using the class hint, need to ask for an int as input, not a float, then convert to float through this formula
    #this is the same as the formula used in the class, for an input with a decimal, like i request.  the assignment doest 
    #ask us to include or be graded for cverifying isdigit operations... and this formula is incorrect, imo.  the correct formula
    #would be a simple compounding interest, as the balance grows over time, the interest would also grow.  
    

    # ADD YOUR CODE HERE
    # savings_account = float(savings_account)
    # interest_earned = float(interest_earned)
    updated_balance = savings_account.balance + interest_earned
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_account.set_balance(updated_balance)
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_account.set_interest(interest_earned)
    # Return the updated balance and interest earned.
    return updated_balance, interest_earned # ADD YOUR CODE HERE
