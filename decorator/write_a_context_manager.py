class Account:

    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class
    # into a 'rollback' context manager

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if sum(self._transactions) < 0:
            self._transactions.pop()
        return True


if __name__ == '__main__':
    account = Account()
    with account as acc:
        acc - 5
    print(account.balance)
    assert account.balance == 0

    with account as acc:
        acc + 10
        print(acc.balance)
        acc - 3
        print(acc.balance)
        acc - 6
        print(acc.balance)
        acc - 4
    print(account.balance)
    assert account.balance == 1