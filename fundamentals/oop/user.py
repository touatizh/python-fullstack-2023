from __future__ import annotations
from bankAccount import BankAccount

class User:
    """
    A class that serves as a simple modelization of bank clients.

    Attributes:
            name (str): A string representing the client's name. Mandatory
            email (str, optional): An optional string representing the client's email address. Defaults to None.
            account (BankAccount | list(BankAccount)): A BankAccount or list BankAccount object(s) representing the client's account(s). Defaults to None.

    Methods:
            link_account_to_user(self, account_to_link: BankAccount|list(BankAccount)) -> User: Links a BankAccount or a list of BankAccount instances to the current User instance.
            make_deposit(self, amount: int) -> None: Adds the given amount to the client's balance.
            make_withdrawal(self, amount: int) -> None: Substracts the given amount from the client's balance.
            display_user_balance(self) -> None: Displays the client's current balance.
            transfert_money(self, other_user: User, amount: int) -> None: Transfers the given amount between client's accounts.
    """
    def __init__(self, name: str, email: str = None, account: BankAccount|list(BankAccount) = None) -> None:
        """
        Constructs all the necessary attributes for the User object.

        Args:
            name (str): A string representing the client's name. Mandatory
            email (str, optional): An optional string representing the client's email address. Defaults to None.
            account (BankAccount | list(BankAccount), Optional): A BankAccount or list BankAccount object(s) representing the client's account(s). Defaults to None

        Returns: None
        """        
        list_of_accounts = []
        match account:
            case list(_):
                list_of_accounts += account
            case BankAccount():
                list_of_accounts.append(account)
            case _:
                list_of_accounts.append(BankAccount(0,0))

        self.name = name
        self.email = email
        self.account = list_of_accounts

    def add_account(self, accounts_to_link: BankAccount|list(BankAccount) = BankAccount(0,0)):
        """
        Gives the option to add/link different accounts to the client's name.
        This is useful for multiple accounts, joint accounts, or if you want to keep track of your spouse's or children spending habits.

        Args:
            account_to_link (BankAccount | list, optional): Links a BankAccount or a list of BankAccount instances to the current User instance. Defaults to BankAccount(0,0).

        Returns:
            self (User): User object with updated accounts.

        """
        match accounts_to_link:
            case list(_):
                self.account += accounts_to_link
            case BankAccount():
                self.account.append(accounts_to_link)
            case _:
                raise TypeError("Invalid entry. accounts_to_link must be a BankAccount or a list of BankAccount instances.")


    def make_deposit(self, account_to_use: BankAccount, amount: int) -> User:
        """
        Adds the given amount to the balance of the specified account.

        Args:
            amount (int): A number representing the sum of money that the client wants to deposit.

        Returns:
            self (User): User object with updated balance.
        """
        if not account_to_use:
            account_to_use = self.account[0]
        if account_to_use in self.account:
                    account_index = self.account.index(account_to_use)
                    self.account[account_index].deposit(amount)
        else:
            raise ValueError("Account provided does not belong to this user")
        return self

    def make_withdrawal(self, account_to_use: BankAccount, amount: int) -> User:
        """
        Substracts the given amount to the balance of the specified account.

        Args:
            amount (int): A number representing the sum of money that the client wants to withdraw.

        Returns:
            self (User): User object with updated balance.
        """  
        if account_to_use in self.account:
            account_index = self.account.index(account_to_use)
            self.account[account_index].withdraw(amount)
        else:
            raise ValueError("Account provided does not belong to this user")
        return self

    def display_user_balance(self) -> None:
        """
        Displays the client's current balance.
        """
        for account in self.account:
            print(f"User: {self.name}, Balance: ${account.balance}")

    def transfert_money(self, account_to_use: BankAccount, amount: int, other_user: User) -> User:
        """
        Transfers the given amount between client's accounts.

        Args:
            other_user (User): A User type object representing the client that will receive the given amount
            amount (int): A number representing the sum of money to transfer to the given client

        Returns:
            self (User): User object with updated balance.
        """
        if account_to_use in self.account:
            account_index = self.account.index(account_to_use)
            self.account[account_index].withdraw(amount)
            other_user.account[0].deposit(amount) if isinstance(other_user.account, list) else other_user.account.deposit(amount)
        return self

if __name__ == "__main__":
    # Assuming BankAccount is an alias for BankAccount

    # Create 3 instances of User
    user1 = User("Shen Doe", account=BankAccount(5000, 0.02))
    user2 = User(name="Akali Tethi", email="akaliTethi@kinkou.order.com", account=BankAccount(balance=2000, int_rate=0.13))
    user3 = User("Zed Ki")

    # user1: 3 deposits and 1 withdrawal to the first account
    user1.make_deposit(user1.account[0], 300).make_deposit(user1.account[0], 270).make_deposit(user1.account[0], 100)
    user1.make_withdrawal(user1.account[0], 390)
    # user1's balance
    user1.display_user_balance()

    # user2: 2 deposits and 2 withdrawals to the first account
    user2.make_deposit(user2.account[0], 250).make_deposit(user2.account[0], 1400)
    user2.make_withdrawal(user2.account[0], 700).make_withdrawal(user2.account[0], 230)
    # user2's balance
    user2.display_user_balance()

    # user3: 1 deposit and 3 withdrawals to the first account
    user3.make_deposit(user3.account[0], 700)
    user3.make_withdrawal(user3.account[0], 140).make_withdrawal(user3.account[0], 300).make_withdrawal(user3.account[0], 350)
    # user3's balance
    user3.display_user_balance()

    # Bonus task: transfer money from user1's first account to user3's first account
    print("------ BONUS ------")
    user1.transfert_money(user1.account[0], 150, user3)
    # user1 and user3 balances after transfer
    user1.display_user_balance()
    user3.display_user_balance()

    #Sensei Bonus: Allow a user to have multiple accounts; 
    #              update methods so the user has to specify which account they are withdrawing or depositing to

    print("\n------ MULTIPLE ACCOUNTS PER USER ------")

    # Add multiple accounts to user1 and user2
    user1.add_account([BankAccount(7000, 0.03), BankAccount(1000, 0.05)])
    user2.add_account(BankAccount(3000, 0.04))

    # user1: Deposit and withdraw from multiple accounts
    user1.make_deposit(user1.account[1], 500)
    user1.make_withdrawal(user1.account[2], 300)

    # user2: Deposit to the second account and withdraw from the first account
    user2.make_deposit(user2.account[1], 1000)
    user2.make_withdrawal(user2.account[0], 500)

    # Display all account balances for user1 and user2
    print("User1 account balances:")
    user1.display_user_balance()

    print("User2 account balances:")
    user2.display_user_balance()

    # Transfer money between different accounts of user1
    print("\n------ TRANSFER BETWEEN USER1's ACCOUNTS ------")
    user1.transfert_money(user1.account[1], 200, user1)
    user1.display_user_balance()

    # Transfer money from user1's second account to user2's first account
    print("\n------ TRANSFER FROM USER1's SECOND ACCOUNT TO USER3's FIRST ACCOUNT ------")
    user1.transfert_money(user1.account[1], 500, user3)
    user1.display_user_balance()
    user3.display_user_balance()
