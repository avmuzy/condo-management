class Condominium:
    def __init__(self):
        print('Condominium created')
        self.street_address = 'Waldo Avenue'
        self.number = 3668

    def identify(self):
        print('Condominium')

class Apartment(Condominium):
    def __init__(self):
        Condominium.__init__(self)
        print('Apartment created')

    def identify(self):
        print('Apartment')


suite401 = Apartment()
