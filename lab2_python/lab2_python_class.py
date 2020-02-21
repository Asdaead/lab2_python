_next = 0

def _next_number():
    global _next
    _next +=1
    return _next

class BankAccount(object):
    def __str__(self):
        return 'number: {0}, balance: {1}'.format(self.number, self.balance)
    def __init__(self, balance = 0):
        self.number = _next_number()
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
    def percents(self):
        if self.balance < 10000:
            self.balance = self.balance * 1.05
        else:
            self.balance *= self.balance * 1.1
    def transfer_from(self, account, amount):
        account.withdraw(amount)
        self.deposit(amount)
        print('success!')

def test_deposit(account):
   print(account)
   amount = int(input('enter amount to deposit on number {0}:'.format(account.number)))
   print(account)   

if __name__ == '__main__':
    ba1 = BankAccount(100)
    ba2 = BankAccount(100)
    print(ba1)
    print(ba2)
    ba1.transfer_from(ba2, 50)
    print(ba1)
    print(ba2)
    ba = BankAccount(100)
    test_deposit(ba)
    from datetime import date
    ba1.date = date.today()
    print(ba1.date)
