from __future__ import annotations

class User:
    """
    A class that serves as a simple modelization of bank accounts.

    Attributes:
            name (str): A string representing the client's name. Mandatory
            email (str, optional): An optional string representing the client's email address. Defaults to None.
            balance (int, optional): An optional number representing the client's starting balance. Defaults to 0.

    Methods:
            make_deposit(self, amount: int) -> None: Adds the given amount to the client's balance.
            make_withdrawal(self, amount: int) -> None: Substracts the given amount from the client's balance.
            display_user_balance(self) -> None: Displays the client's current balance.
            transfert_money(self, other_user: User, amount: int) -> None: Transfers the given amount between client's accounts.
    """
    def __init__(self, name: str, email: str = None, balance: int = 0) -> None:
        """
        Constructs all the necessary attributes for the User object.

        Args:
            name (str): A string representing the client's name. Mandatory
            email (str, optional): An optional string representing the client's email address. Defaults to None.
            balance (int, optional): An optional number representing the client's starting balance. Defaults to 0.

        Returns: None
        """        
        self.name = name
        self.email = email
        self.balance = balance

    def make_deposit(self, amount: int) -> None:
        """
        Adds the given amount to the client's balance.

        Args:
            amount (int): A number representing the sum of money that the client wants to deposit.

        Returns: None
        """        
        self.balance += amount

    def make_withdrawal(self, amount: int) -> None:
        """
        Substracts the given amount from the client's balance.

        Args:
            amount (int): A number representing the sum of money that the client wants to withdraw.

        Returns: None
        """
        self.balance -= amount

    def display_user_balance(self) -> None:
        """
        Displays the client's current balance.
        """
        print(f"User: {self.name}, Balance: ${self.balance}")

    def transfert_money(self, other_user: User, amount: int) -> None:
        """
        Transfers the given amount between client's accounts.

        Args:
            other_user (User): A User type object representing the client that will receive the given amount
            amount (int): A number representing the sum of money to transfer to the given client

        Returns: None
        """
        self.balance -= amount
        other_user.balance += amount

if __name__ == "__main__":
    #Create 3 instances of User
    user1 = User("Shen Doe", 5000)
    user2 = User(name="Akali Tethi", email="akaliTethi@kinkou.order.com", balance=2000)
    user3 = User("Zed Ki")

    #user1: 3 deposits and 1 withdrawal
    user1.make_deposit(300)
    user1.make_deposit(270)
    user1.make_deposit(100)
    user1.make_withdrawal(390)
    #user1's balance
    user1.display_user_balance()

    #user2: 2 deposits and 2 withdrawals
    user2.make_deposit(250)
    user2.make_deposit(1400)
    user2.make_withdrawal(700)
    user2.make_withdrawal(230)
    #user2's balance
    user2.display_user_balance()

    #user3: 1 deposit and 3 withdrawls
    user3.make_deposit(700)
    user3.make_withdrawal(140)
    user3.make_withdrawal(300)
    user3.make_withdrawal(350)
    #user3's balance
    user3.display_user_balance()

    #Bonus task: transfer money from user1's account to user3's account
    print("------ BONUS ------")
    user1.transfert_money(user3, 150)
    #user1 and user3 balances after transfer
    user1.display_user_balance()
    user3.display_user_balance()

