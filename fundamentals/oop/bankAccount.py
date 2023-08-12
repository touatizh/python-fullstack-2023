from __future__ import annotations

class BankAccount:
    """
    A class that serves as a simple modelization of bank accounts.

    Attributes:
            balance (int, optional): Client's starting balance. Defaults to 0.
            int_rate (float): Set the interest rate for the account. Defaults to 0.
            class_instances (list): A list that keeps track of all class instances.

    Methods:
            display_all_accounts_info(cls) -> None: Display information of all class instances at once.
            eposit(self: BankAccount, amount: float = 0) -> BankAccount: Adds the amount to the balance of a BankAccount object.
            withdraw(self: BankAccount, amount: float = 0) -> BankAccount: Subtracts the amount from the balance of a BankAccount object. If there are insufficient funds, a  $5 fee will be charged.
            display_account_info(self: BankAccount) -> None: Prints the balance of a BankAccount object.
            yield_interest(self: BankAccount) -> BankAccount: Adds (current balance * interest rate) to the balance of a BankAccount object as long as the balance is positive.
    """
    class_instances = [] #stores all BankAccount instances
    _next_id = 1 # used to assign sequential id numbers to each new instance
    @classmethod
    def display_all_accounts_info(cls) -> None:
        """
        Display information of all class instances at once.
        
        Args:
            cls: Represent the class object itself.
        
        Returns:
            None
        """
        for instance in cls.class_instances:
            instance.display_account_info()

    def __init__(self: BankAccount, balance: float = 0, int_rate: float = 0) -> None:
        """
        Constructs all the necessary attributes for the BankAccount object. 
        Adds the new created BankAccount instance to a class variable that keeps track of all BankAccount instances
        
        Args:
            self: Represent the instance of the object itself
            id (int): Represent the account identifier
            balance: float: Set the initial balance of the account
            int_rate: float: Set the interest rate for the account
        
        Returns:
            None
        """
        self.id = BankAccount._next_id
        self.balance = balance
        self.int_rate = int_rate
        BankAccount._next_id += 1
        BankAccount.class_instances.append(self)

    def __eq__(self, account_to_compare: BankAccount) -> bool:
        """
        Used to compare two BankAccount objects. 
        
        Args:
            self: Refer to the current instance
            account_to_compare: BankAccount: Compare the id of the account to another account
        
        Returns:
            True if the id of the current account is equal to the id of the account passed in as an argument
        """
        return self.id == account_to_compare.id

    def deposit(self: BankAccount, amount: float = 0) -> BankAccount:
        """
        Adds the amount to the balance of a BankAccount object.
        
        Args:
            self: BankAccount: Represent the instance the object that is calling the function
            amount: float: Specify the amount of money to be deposited into the account. Defaults to 0 if no value is provided by the user.
        
        Returns:
            self: BankAccount: The instance of the object that is calling the function with updated balance
        """
        self.balance += amount
        return self
    
    def withdraw(self: BankAccount, amount: float = 0) -> BankAccount:
        """
        Subtracts the amount from the balance of a BankAccount object.
        If there are insufficient funds, a  $5 fee will be charged.
        
        Args:
            self: BankAccount: Represent the instance the object that is calling the function
            amount: float: Specify the amount of money to be withdrawn from the account. Defaults to 0 if no value is provided by the user.
        
        Returns:
            self: BankAccount: The instance of the object that is calling the function with updated balance
        """
        if self.balance < amount: print("Insufficient funds: Charging a $5 fee")
        self.balance -= amount if self.balance > amount else amount + 5
        return self
    
    def display_account_info(self: BankAccount) -> None:
        """
        Prints the balance of a BankAccount object.
        
        Args:
            self: BankAccount: Represent the instance the object that is calling the function
        
        Returns:
            None
        """
        print(f"Balance: ${self.balance}")

    def yield_interest(self: BankAccount) -> BankAccount:
        """
        Adds (current balance * interest rate) to the balance of a BankAccount object as long as the balance is positive.

        Args:
            self: BankAccount: Represent the instance the object that is calling the function

        Returns:
            self: BankAccount: The instance of the object that is calling the function with updated balance
        """        
        self.balance += self.balance * self.int_rate if self.balance > 0 else 0
        return self
    
if __name__ == "__main__":
    #Create 2 accounts
    account1 = BankAccount(450, 0.04)
    account2 = BankAccount(1400, 0.1)

    #account1: 3 deposits and 1 withdrawal
    account1.deposit(300).deposit(550).deposit(1200).withdraw(680.56).yield_interest().display_account_info()

    #account2: 2 deposits and 4 withdrawals
    account2.deposit(680).deposit(275).withdraw(880).withdraw(700).withdraw(400).withdraw(550).yield_interest().display_account_info()

    #Bonus
    print("------ Using classmethod ------")
    BankAccount.display_all_accounts_info()