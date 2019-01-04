from ChainOfResponsibilityPattern.pattern_classes import AbstractClasses


class ATM(AbstractClasses.ExchangeAbstractClass):

    def __init__(self, money):
        self.money = money
        self.n100 = 0
        self.n50 = 0
        self.n20 = 0
        self.n10 = 0
        self.n5 = 0
        self.n1 = 0

    def distribute(self):
        qaliq100 = self.money - (self.money % 100)
        self.set100(qaliq100 / 100)
        fifties = self.money -qaliq100
        qaliq50 = fifties - (fifties % 50)
        self.set50(qaliq50 / 50)
        twenties = fifties -qaliq50
        qaliq20 = twenties - (twenties % 20)
        self.set20(qaliq20 / 20)
        tens = twenties - qaliq20
        qaliq10 = tens - (tens % 10)
        self.set10(qaliq10 / 10)
        fives = tens -qaliq10
        qaliq5 = fives - (fives % 5)
        self.set5(qaliq5 / 5)
        ones = fives - qaliq5
        qaliq1 = ones - (ones % 1)
        self.set1(qaliq1 / 1)

    def set100(self, amount):
        self.n100 = amount

    def set50(self, amount):
        self.n50 = amount

    def set20(self, amount):
        self.n20 = amount

    def set10(self, amount):
        self.n10 = amount

    def set5(self, amount):
        self.n5 = amount

    def set1(self, amount):
        self.n1 = amount

    def get100(self):
        return self.n100

    def get50(self):
        return self.n50

    def get20(self):
        return self.n20

    def get10(self):
        return self.n10

    def get5(self):
        return self.n5

    def get1(self):
        return self.n1