class Condominium:
    def __init__(self):
        print('Condominium created')
        self.street_address = 'Waldo Avenue'
        self.number = 3668

    def identify(self):
        print('Condominium')


class Apartment(Condominium):
    def __init__(self, suite, month_fee, month_tax, kind, area):
        Condominium.__init__(self)
        print('Apartment created')
        self.suite = suite
        self.month_fee = month_fee
        self.month_tax = month_tax
        self.kind = kind
        self.area = area

    def identify(self):
        print('Apartment')


class Store(Condominium):
    def __init__(self, store, month_fee, month_tax, kind, area):
        Condominium.__init__(self)
        print('Store created')
        self.store = store
        self.month_fee = month_fee
        self.month_tax = month_tax
        self.kind = kind
        self.area = area


suite201 = Apartment('201', 300, 50, 'Apartment', 44)
suite202 = Apartment('202', 300, 50, 'Apartment', 44)
suite301 = Apartment('301', 300, 50, 'Apartment', 44)
suite302 = Apartment('302', 300, 50, 'Apartment', 44)
suite401 = Apartment('401', 300, 50, 'Apartment', 44)
suite402 = Apartment('402', 300, 50, 'Apartment', 44)
suite501 = Apartment('501', 300, 50, 'Apartment', 44)
suite502 = Apartment('502', 300, 50, 'Apartment', 44)
store01 = Store('Store 01', 350, 50, 'Store', 21)
store02 = Store('Store 02', 350, 50, 'Store', 21)
store03 = Store('Store 03', 350, 50, 'Store', 26)

total_fee = (suite201.month_fee + suite202.month_fee + suite301.month_fee + suite302.month_fee + suite401.month_fee
             + suite402.month_fee + suite501.month_fee + suite502.month_fee + store01.month_fee + store02.month_fee
             + store03.month_fee)
print(total_fee)

total_tax = (suite201.month_tax + suite202.month_tax + suite301.month_tax + suite302.month_tax +suite401.month_tax
             + suite402.month_tax + suite501.month_tax + suite502.month_tax + store01.month_tax + store02.month_tax
             + store03.month_tax)
print(total_tax)
total_revenue = total_fee + total_tax
print(total_revenue)
