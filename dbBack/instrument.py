import numpy

class Instrument:

    def __init__(self, inputname, inputbase, inputdrift, inputvariance):
        self.name = inputname
        self.__price = inputbase
        self.__startingPrice = inputbase
        self.__drift = inputdrift
        self.__variance = inputvariance


    def calculateNextPrice(self, direction):
        newPriceStarter = self.__price + numpy.random.normal(0, 1) * self.__variance + self.__drift
        newPrice = newPriceStarter if (newPriceStarter > 0) else 0.0
        if self.__price < self.__startingPrice * 0.4:
            self.__drift = (-0.7 * self.__drift)
        self.__price = newPrice * 1.01 if direction == 'B' else newPrice * 0.99
        return self.__price
