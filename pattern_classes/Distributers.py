from ChainOfResponsibilityPattern.pattern_classes import AbstractClasses


class Give1(AbstractClasses.CashHandler):

    def give(self, money):
        if money.get1() > 0:
            print("Give " + str(money.get1()) + " 1 in cash. ")
        self.next(money)


class Give5(AbstractClasses.CashHandler):

    def give(self, money):
        if money.get5() > 0:
            print("Give " + str(money.get5()) + " 5 in cash. ")
        self.next(money)


class Give10(AbstractClasses.CashHandler):

    def give(self, money):
        if money.get10() > 0:
            print("Give " + str(money.get10()) + " 10 in cash. ")
        self.next(money)


class Give20(AbstractClasses.CashHandler):

    def give(self, money):
        if money.get20() > 0:
            print("Give " + str(money.get20()) + " 20 in cash. ")
        self.next(money)


class Give50(AbstractClasses.CashHandler):

    def give(self, money):
        if money.get50() > 0:
            print("Give " + str(money.get50()) + " 50 in cash. ")
        self.next(money)


class Give100(AbstractClasses.CashHandler):

    def give(self, money):
        if money.get100() > 0:
            print("Give " + str(money.get100()) + " 100 in cash. ")
        self.next(money)