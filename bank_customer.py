class BankCustomer(object):
    """customer of a Bank with a checking account. Customers have the
    following:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name):
        """Return a Customer object whose name is *name* and starting
        balance is 0."""
        self.name = name
        self.balance = 0.0

    def set_balance(self, balance):
        """Set the customer's starting balance."""
        self.balance = balance
        return str(self.name) + ' initial balance is ' + str(self.balance) + ' dollars'

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return str(self.name) + ' withdrew ' + str(self.balance) + ' dollars'

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        self.interest_on(self.name)
        return str(self.name) + ' deposited ' + str(self.balance) + ' dollars'
        """ added message about interest rate """
    def interest_on(self, cust):
        print str(cust) + ' interest is 7%'


x = BankCustomer("Patrick Arthur")
print x.set_balance(120)
print x.withdraw(50)
print x.deposit(10)

y = BankCustomer("Romulus Superior")
print y.set_balance(1000)
print y.withdraw(10)
print y.deposit(100)
