class Condominium:
    def __init__(self, suite, month_fee, month_tax, kind, area):
        self.street_address = 'Waldo Avenue'
        self.number = 3668
        self.suite = suite
        self.month_fee = month_fee
        self.month_tax = month_tax
        self.kind = kind
        self.area = area


suite201 = Condominium(suite=201, month_fee=350, month_tax=50, kind='Apartment', area=44)
print(suite201.number, suite201.street_address,)
print('Apartment number:',suite201.suite)
print('Monthly fee:', suite201.month_fee, '+', suite201.month_tax, '=', suite201.month_fee+suite201.month_tax)
print('Property type:', suite201.kind)
print('Total area:', suite201.area)
