_next = 0


import pickle

def _next_number():
    global _next
    _next +=1
    return _next

class PersistenceAccount(object):

    @staticmethod
    def serialize(account):
        with open('bank_account.pkl', 'wb') as f:
            pickle.dump(account, f)
        f.closed

    @staticmethod
    def deserialize():
        with open('bank_account.pkl', 'rb') as f:
            account = pickle.load(f)
        f.closed
        return account

class BankTransaction(object):
    def __init__(self, amount):
        self.when = datetime.today()
        self.amount = amount
    def __del__(self):
        with open('transaction.txt', 'a') as f:
            f.write('when {0} : amount {1} \n'.format(self.when, self.amount))
        f.closed

class BankAccount(object):
    def __str__(self):
        return 'number: {0}, balance: {1}'.format(self.number, self.balance)
    def __init__(self, balance = 0):
        self.number = _next_number()
        self.balance = balance
        self.queue = []
    def deposit(self, amount):
        self.balance += amount
        self.queue.append(BankTransaction(amount))
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
    def percents(self):
        if self.balance < 10000:
            self.balance = self.balance * 1.05
        else:
            self.balance *= self.balance * 1.1
    def transfer_from(self, account, amount):
        if account.balance > amount:
            account.withdraw(amount)
            self.deposit(amount)
            print('success!')
        else: 
            print('error: too big amount')
    def get_transaction(self):
        for i in range(len(self.queue)):
            item = self.queue.pop(0)
            print('when {0} : amount {1}'.format(item.when, item.amount))
    @classmethod
    def create_bank_account(cls, value):
        return cls(value)

def test_deposit(account):
   print(account)
   amount = int(input('enter amount to deposit on number {0}:'.format(account.number)))
   account.deposit(amount)
   print(account)  
   
def test_withdraw(account):
   print(account)
   amount = int(input('enter amount to deposit on number {0}:'.format(account.number)))
   account.withdraw(amount)
   print(account)  
   


if __name__ == '__main__':
    from datetime import datetime
    ba1 = BankAccount(100)
    ba2 = BankAccount(100)
    print(ba1)
    print(ba2)
    ba1.transfer_from(ba2, 50)
    print(ba1)
    print(ba2)

    ba3 = BankAccount(200)
    test_deposit(ba3)
    test_withdraw(ba3)
    ba3.get_transaction()

    ba4 = BankAccount(100)
    PersistenceAccount.serialize(ba4)
    print(PersistenceAccount.deserialize())
