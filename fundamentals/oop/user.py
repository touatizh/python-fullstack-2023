from __future__ import annotations
from bankAccount import BankAccount

class User:
    """
    A class that serves as a simple modelization of bank clients.

    Attributes:
            name (str): A string representing the client's name. Mandatory
            email (str, optional): An optional string representing the client's email address. Defaults to None.
            account (BankAccount, optional): An optional BankAccount object representing the client's account. Defaults to BankAccount(0,0).

    Methods:
            make_deposit(self, amount: int) -> None: Adds the given amount to the client's balance.
            make_withdrawal(self, amount: int) -> None: Substracts the given amount from the client's balance.
            display_user_balance(self) -> None: Displays the client's current balance.
            transfert_money(self, other_user: User, amount: int) -> None: Transfers the given amount between client's accounts.
    """
    def __init__(self, name: str, email: str = None, account: BankAccount = BankAccount(0,0)) -> None:
        """
        Constructs all the necessary attributes for the User object.

        Args:
            name (str): A string representing the client's name. Mandatory
            email (str, optional): An optional string representing the client's email address. Defaults to None.
            account BankAccount, optional): An optional BankAccount object representing the client's account. Defaults to BankAccount(0,0).

        Returns: None
        """        
        self.name = name
        self.email = email
        self.account = account

    def make_deposit(self, amount: int) -> User:
        """
        Adds the given amount to the client's balance.

        Args:
            amount (int): A number representing the sum of money that the client wants to deposit.

        Returns:
            self (User): User object with updated balance.
        """        
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount: int) -> User:
        """
        Substracts the given amount from the client's balance.

        Args:
            amount (int): A number representing the sum of money that the client wants to withdraw.

        Returns:
            self (User): User object with updated balance.
        """
        self.account.withdraw(amount)
        return self

    def display_user_balance(self) -> None:
        """
        Displays the client's current balance.
        """
        print(f"User: {self.name}, Balance: ${self.account.balance}")

    def transfert_money(self, other_user: User, amount: int) -> User:
        """
        Transfers the given amount between client's accounts.

        Args:
            other_user (User): A User type object representing the client that will receive the given amount
            amount (int): A number representing the sum of money to transfer to the given client

        Returns:
            self (User): User object with updated balance.
        """
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self

if __name__ == "__main__":
    #Create 3 instances of User
    user1 = User("Shen Doe", account=BankAccount(5000, 0.02))
    user2 = User(name="Akali Tethi", email="akaliTethi@kinkou.order.com", account=BankAccount(balance=2000, int_rate=0.13))
    user3 = User("Zed Ki")

    #user1: 3 deposits and 1 withdrawal
    user1.make_deposit(300).make_deposit(270).make_deposit(100)
    user1.make_withdrawal(390)
    #user1's balance
    user1.display_user_balance()

    #user2: 2 deposits and 2 withdrawals
    user2.make_deposit(250).make_deposit(1400)
    user2.make_withdrawal(700).make_withdrawal(230)
    #user2's balance
    user2.display_user_balance()

    #user3: 1 deposit and 3 withdrawls
    user3.make_deposit(700)
    user3.make_withdrawal(140).make_withdrawal(300).make_withdrawal(350)
    #user3's balance
    user3.display_user_balance()

    #Bonus task: transfer money from user1's account to user3's account
    print("------ BONUS ------")
    user1.transfert_money(user3, 150)
    #user1 and user3 balances after transfer
    user1.display_user_balance()
    user3.display_user_balance()

