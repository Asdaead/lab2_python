_next = 0


import pickle
import shelve

def _next_number():
    global _next
    _next +=1
    return _next

class PersistenceAccount(object):
    @staticmethod
    def shelve_method(account):
        str_number = "{0}".format(account.number)
        with shelve.open("transaction", flag="c") as states:
            states[str_number] = account.balance
            print(states[str_number])

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
    def __init__(self, amount, type):
        self.when = datetime.today()
        self.amount = amount
        self.type = type

class BankAccount(object):
    def __str__(self):
        return 'number: {0}, balance: {1}'.format(self.number, self.balance)
    def __init__(self, balance = 0):
        self.number = _next_number()
        self.balance = balance
        self.queue = []
    def deposit(self, amount):
        self.balance += amount
        self.queue.append(BankTransaction(amount, "deposit"))
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        self.queue.append(BankTransaction(amount, "withdraw"))
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
            print('when {0} : amount {1}, type: {2}'.format(item.when, item.amount, item.type))
    @classmethod
    def create_bank_account(cls, value):
        return cls(value)

class PersonalBankAccount(BankAccount):
    def __init__(self, balance = 0, name = None, dateDay = 25, percents = .1):
        super(PersonalBankAccount, self).__init__(balance)
        self.name = name
        self.percents = percents
        self.dateDay = dateDay
    def __str__(self):
        datar = datetime.now()
        datar = datar.replace(day = self.dateDay)
        return 'number: {0}, balance: {1}, name: {2}, percenst: {3}, date of payment: {4}'.format(self.number, self.balance, self.name, self.percents, datar)
    def interest(self):
        self.balance *= (1 + self.percents)

class OverdrawnBankAccount(PersonalBankAccount):
    def __init__(self, balance = 0, overdrawn = -1000, overdrawnPercents = 0.05):
        super(OverdrawnBankAccount, self).__init__(balance)
        self.overdrawn = overdrawn
        self.overdrawnPercents = overdrawnPercents
    def __str__(self):
        return 'number: {0}, balance: {1}, name: {2}, overdrawn: {3}, overdrawnPercents: {4}'.format(self.number, self.balance, self.name, self.overdrawn, self.overdrawnPercents)
    def withdraw(self, amount):
        if self.balance - amount > self.overdrawn:
            self.balance -= amount
        self.balance -= self.balance * self.overdrawnPercents

class CheckingAccount(BankAccount):
    def __init__(self, balance = 0, taxes = 0.01, operationsLimit = 100, count = 0):
        super(CheckingAccount, self).__init__(balance)
        self.taxes = taxes
        self.operationsLimit = operationsLimit
        self.count = count
    def __str__(self):
        return 'number: {0}, balance: {1}, taxes: {2}, operations left: {3}, count: {4}'.format(self.number, self.balance, self.taxes, self.operationsLimit, self.count)
    def deposit(self, amount):
        self.balance += amount
        self.balance -= self.balance * self.taxes
        self.queue.append(BankTransaction(amount, "deposit"))
        self.count += 1
        self.operationsLimit -= 1
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            self.balance -= self.balance * self.taxes
            self.queue.append(BankTransaction(amount, "withdraw"))
            self.count += 1
            self.operationsLimit -= 1
        else: 
            print('error: too big amount')

def test_deposit(account):
   print(account)
   amount = int(input('enter amount to deposit on number {0}:'.format(account.number)))
   account.deposit(amount)
   print(account)  
   
def test_withdraw(account):
   print(account)
   amount = int(input('enter amount to withdraw on number {0}:'.format(account.number)))
   account.withdraw(amount)
   print(account)  
   
if __name__ == '__main__':
    from datetime import datetime
    ba1 = BankAccount(100)
    ba2 = BankAccount(100)
    print(ba1)
    print(ba2)
    ba1.transfer_from(ba2, 50)

    person = PersonalBankAccount(100, 'Alex')
    person.interest()
    print(person)

    oba = OverdrawnBankAccount(100)
    oba.withdraw(50)
    print(oba)    

    ca = CheckingAccount(100)
    ca.deposit(50)
    print(ca)
    ca.withdraw(20)
    print(ca)
 
