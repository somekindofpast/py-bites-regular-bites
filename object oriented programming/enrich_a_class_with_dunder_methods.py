class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []
        self.next_pos = 0

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below

    def __len__(self):
        return len(self._transactions)

    def __eq__(self, other):
        if not isinstance(other, Account):
            return False
        return self.balance == other.balance

    def __ne__(self, other):
        if not isinstance(other, Account):
            return False
        return self.balance != other.balance

    def __lt__(self, other):
        if not isinstance(other, Account):
            return False
        return self.balance < other.balance

    def __le__(self, other):
        if not isinstance(other, Account):
            return False
        return self.balance <= other.balance

    def __gt__(self, other):
        if not isinstance(other, Account):
            return False
        return self.balance > other.balance

    def __ge__(self, other):
        if not isinstance(other, Account):
            return False
        return self.balance >= other.balance

    def __getitem__(self, index):
        return self._transactions[index]

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_pos >= len(self._transactions):
            self.next_pos = 0
            raise StopIteration
        value = self._transactions[self.next_pos]
        self.next_pos += 1
        return value

    def __add__(self, amount):
        if not isinstance(amount, int):
            raise TypeError
        self._transactions.append(amount)

    def __sub__(self, amount):
        if not isinstance(amount, int):
            raise TypeError
        self._transactions.append(-amount)

    def __str__(self):
        return f"{self.name} account - balance: {self.balance}"