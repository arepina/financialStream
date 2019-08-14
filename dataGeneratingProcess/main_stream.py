import logging
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
        print(stream)
        try:
            logging.info(stream)
            requests.post(endpoint.POST_TO, json=stream)  # ERROR
        except Exception as e:
            logging.error("Error: ", str(e))
            print(e)
            continue


def bootapp():
    app.run(port=endpoint.PORT, threaded=True, host=(endpoint.HOST), debug=True)
    logging.info("I'm running")


if __name__ == '__main__':
    bootapp()
