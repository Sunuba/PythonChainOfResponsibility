from ChainOfResponsibilityPattern.pattern_classes.Distributers import Give100, Give1, Give5, Give10, Give20, Give50
from ChainOfResponsibilityPattern.pattern_classes.ATM import ATM
from ChainOfResponsibilityPattern.pattern_classes.BankBranch import BankBranch

give100 = Give100()
give50 = Give50()
give20 = Give20()
give10 = Give10()
give5 = Give5()
give1 = Give1()

give100.set_successor(give50)
give50.set_successor(give20)
give20.set_successor(give10)
give10.set_successor(give5)
give5.set_successor(give1)

money = ATM(99) # money = BankBranch(199) - where 50 nominal values are not available, so outcome will be different.
money.distribute()
# print(money.__dict__)

give100.give(money)

