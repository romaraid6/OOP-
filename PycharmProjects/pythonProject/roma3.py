class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным!")
        self._balance = value

class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        self.balance += self.balance * rate


acc = SavingsAccount("Romka", 10000)
acc.add_interest(0.1)
print(acc.balance)
