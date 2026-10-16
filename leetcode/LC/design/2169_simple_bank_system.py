class Bank:
    def __init__(self, balance: list[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 < 1 or account2 < 1 or account1 > len(self.balance) or account2 > len(self.balance):
            return False
        if self.balance[account1 - 1] < money:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> None:
        if account < 1 or account > len(self.balance):
            return
        self.balance[account - 1] += money

    def withdraw(self, account: int, money: int) -> bool:
        if account < 1 or account > len(self.balance):
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True
