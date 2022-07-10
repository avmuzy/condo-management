class Condominium:
    def __init__(self):
        self.street_address = 'Waldo Avenue'
        self.number = 3668
        self.suite = 501
        self.month_fee = 350.00
        self.month_tax = 55.00


Condominium1 = Condominium()
print(type(Condominium1))
print(Condominium1)
print('The apartment address is:', Condominium1.number, Condominium1.street_address, ', Suite:', Condominium1.suite)
print('Total cost:', Condominium1.month_fee + Condominium1.month_tax,)
