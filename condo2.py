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
