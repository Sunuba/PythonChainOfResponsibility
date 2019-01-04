from abc import ABC, abstractmethod


class ExchangeAbstractClass(ABC):
    @abstractmethod
    def distribute(self):
        raise NotImplementedError

    @abstractmethod
    def set100(self, amount):
        raise NotImplementedError

    @abstractmethod
    def set50(self, amount):
        raise NotImplementedError

    @abstractmethod
    def set20(self, amount):
        raise NotImplementedError

    @abstractmethod
    def set10(self, amount):
        raise NotImplementedError

    @abstractmethod
    def set5(self, amount):
        raise NotImplementedError

    @abstractmethod
    def set1(self, amount):
        raise NotImplementedError

    @abstractmethod
    def get100(self):
        raise NotImplementedError

    @abstractmethod
    def get50(self):
        raise NotImplementedError

    @abstractmethod
    def get20(self):
        raise NotImplementedError

    @abstractmethod
    def get10(self):
        raise NotImplementedError

    @abstractmethod
    def get5(self):
        raise NotImplementedError

    @abstractmethod
    def get1(self):
        raise NotImplementedError


class CashHandler(ABC):

    def __init__(self):
        self.successor = None

    @abstractmethod
    def give(self, money):
        raise NotImplementedError

    def set_successor(self, successor):
        self.successor = successor

    def next(self, money):
        if self.successor:
            self.successor.give(money)