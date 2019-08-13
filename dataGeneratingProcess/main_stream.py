import requests
from flask import Flask
from flask_cors import CORS
import endpoint

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

    for stream in data_stream():
        requests.post(endpoint.POST_TO, json=stream)


def bootapp():
    app.run(port=8080, threaded=True, host='localhost')


if __name__ == '__main__':
    bootapp()
