class Customer:
    last_id = 0

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f'Customer[{self.id}, {self.firstname}, {self.lastname}]'


class Account:
    last_id = 1000

    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0

    #remove
    def deposit(self, amount):
        if(type(amount)==int or type(amount)==float):
            if(amount>0):
                if(amount<=self._balance):
                    self._balance-=amount
    #add
    def charge(self, amount):
        if(type(amount)==int or type(amount)==float):
            if(amount>0):
                self._balance+=amount

    def __repr__(self):
        return f'Account[{self.id}, {self.customer.lastname}, {self._balance}]'


class Bank:
    def __init__(self):
        self.customer_list = []
        self.account_list = []

    def create_customer(self, firstname, lastname):
        c = Customer(firstname, lastname)
        self.customer_list.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.account_list.append(a)
        return a

    def __repr__(self):
        return f'Bank[{self.customer_list}; {self.account_list}]'

bank = Bank()

c = bank.create_customer('John', 'Brown')
print(c)
a = bank.create_account(c)
a2 = bank.create_account(c)
print(a)

c2 = bank.create_customer('Anne', 'Smith')
a3 = bank.create_account(c2)
print(bank)
print("-----------------------------------------")
print(bank.account_list[0])
bank.account_list[0].charge(200)
print("-----------------------------------------")
print(bank.account_list[0])
bank.account_list[0].deposit(100)
print("-----------------------------------------")
print(bank.account_list[0])