import json
import time
from datetime import datetime, timedelta

import numpy
import random

from instrument import Instrument

instruments = ("Astronomica", "Borealis", "Celestial", "Deuteronic", "Eclipse",
               "Floral", "Galactia", "Heliosphere", "Interstella", "Jupiter", "Koronis", "Lunatic")
counterparties = ("Lewis", "Selvyn", "Richard", "Lina", "John", "Nidia")
NUMBER_OF_RANDOM_DEALS = 2000
TIME_PERIOD_MILLIS = 3600000
EPOCH = datetime.now() - timedelta(days=1)


class RandomDealData:
    def createInstrumentList(self):
        f = open('initialRandomValues.txt', 'r')
        instrumentId = 1000
        instrumentList = []
        for instrumentName in instruments:
            hashedValue = int(f.readline())
            isNegative = hashedValue < 0
            basePrice = (abs(hashedValue) % 10000) + 90.0
            drift = ((abs(hashedValue) % 5) * basePrice) / 1000.0
            drift = 0 - drift if isNegative else drift
            variance = (abs(hashedValue) % 1000) / 100.0
            variance = 0 - variance if isNegative else variance
            instrument = Instrument(instrumentName, basePrice, drift, variance)
            instrumentList.append(instrument)
            instrumentId += 1
        return instrumentList

    def createRandomData(self, instrumentList):
        time.sleep(random.uniform(1, 30) / 100)
        dealId = 20000
        instrument = instrumentList[numpy.random.randint(0, len(instrumentList))]
        cpty = counterparties[numpy.random.randint(0, len(counterparties))]
        type = 'B' if numpy.random.choice([True, False]) else 'S'
        quantity = int(numpy.power(1001, numpy.random.random()))
        dealTime = datetime.now() - timedelta(days=1)
        dealId += 1
        deal = {
            'instrumentName': instrument.name,
            'cpty': cpty,
            'price': instrument.calculateNextPrice(type),
            'type': type,
            'quantity': quantity,
            'time': dealTime.strftime("%d-%b-%Y (%H:%M:%S.%f)"),
        }
        #print(deal)
        return json.dumps(deal)
