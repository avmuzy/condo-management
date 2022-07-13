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


suite401 = Apartment(401, 350, 50, 'Apartment', 44)
