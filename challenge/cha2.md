## Challenge: Bank Account System (OOP)

### Description:
Create a class-based system to manage multiple types of bank accounts. The system should handle deposits, withdrawals, interest calculation, and overdraft limits. Implement proper OOP concepts: encapsulation, inheritance, and polymorphism.

### Requirements:
1. Classes and Attributes:
  - Account (base class):
    - account_number (str): Unique account number.
    - balance (float): Current balance.
  - SavingsAccount (inherits Account):
    - interest_rate (float): Annual interest rate.
  - CheckingAccount (inherits Account):
    - overdraft_limit (float): Maximum negative balance allowed.
2. Methods:
  - Account.deposit(amount):
    - Increase the balance by amount.
  - Account.withdraw(amount):
    - Decrease the balance by amount if possible.
  - SavingsAccount.calculate_interest():
    - Calculate and return interest based on current balance.
  - CheckingAccount.withdraw(amount):
    - Override to allow overdraft up to limit.
  - Account.show_balance():
    - Display the current balance.

**Extra Challenges:**
- Prevent withdrawal of negative amounts.
- Add transaction history tracking.
- Implement monthly interest addition for SavingsAccount.
