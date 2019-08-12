#import mysql.connector
#mysql.connector.connect(host='192.168.99.100',database='mydata',user='root',password='ppp')
from randomDealData import RandomDealData#
from flask import Flask
app = Flask(__name__)

@app.route("/")
def data_stream():
    data_stream = RandomDealData()
    instrumentList = data_stream.createInstrumentList()
    while True:
        data_stream.createRandomData(instrumentList)

if __name__ == "__main__":
    app.run()