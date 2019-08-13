from flask import Flask, Response
from flask_cors import CORS

from randomDealData import RandomDealData

app = Flask(__name__)
CORS(app)


@app.route('/')
def getstream():
    def data_stream():
        stream = RandomDealData()
        instrumentList = stream.createInstrumentList()
        while True:
            yield stream.createRandomData(instrumentList)
    return Response(data_stream())



def bootapp():
    app.run(port=8080, threaded=True, host=('localhost'))

if __name__ == '__main__':
    bootapp()

#output like:
#{"instrumentName": "Borealis", "cpty": "Richard", "price": 5710.3126391859405, "type": "S", "quantity": 2, "time": "12-Aug-2019 (08:32:16.873460)"}
