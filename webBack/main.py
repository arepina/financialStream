import math
import time
from random import random

import requests
import simplejson
from flask import Flask, request, Response
from flask_cors import CORS

from endpoints import *

app = Flask(__name__)
CORS(app)


def json_response(payload, status=200):
    return (simplejson.dumps(payload), status, {'content-type': 'application/json'})


@app.route('/register', methods=["POST"])
def register():
    login = request.json['login']
    password = request.json['password']
    userType = request.json['userType']
    resp = requests.post(CREATE_USER,
                         json={"login": login, "password": password, "userType": userType})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/login', methods=["POST"])
def login():
    login = request.json['login']
    password = request.json['password']
    resp = requests.get(GET_USER,
                        json={"login": login, "password": password})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/average', methods=["POST"])
def average():
    start = request.json['start']
    end = request.json['end']
    resp = requests.get(AVERAGE,
                        json={"start": start, "end": end})
    # '[["an", "\\u00a3 321.00", null], ["en", null, "\\u00a3 743.00"], ["in", "\\u00a3 3,416.00", null], ["un", null, "\\u00a3 123.00"]]'
    averageBuy = []
    averageSell = []
    for item in resp.text.split('], ['):
        item = item.replace('[', '').replace(']', '').replace('\\u00a3', '')
        item = item[item.index(',') + 2:]
        sep = item.index(', ')
        buy = item[:sep].replace(" ", '').replace("\"", "")
        sell = item[sep + 2:].replace(" ", '').replace("\"", "")
        if buy == 'null':
            averageBuy.append(0)
        else:
            averageBuy.append(float(buy.replace(',', '').replace("$", "")))
        if sell == 'null':
            averageSell.append(0)
        else:
            averageSell.append(float(sell.replace(',', '').replace("\"", "").replace("$", "")))
    return json_response({'averageBuy': averageBuy, 'averageSell': averageSell})


@app.route('/dealers_position', methods=["POST"])
def dealers_position():
    start = request.json['start']
    end = request.json['end']
    resp = requests.get(DEALERS_POSITION,
                        json={"start": start, "end": end})
    endingDealers = []
    for item in resp.text.split('], ['):
        item = item.replace('[', '').replace(']', '').replace('\\u00a3', '')
        item = item[item.index(',') + 2:]
        item = item[item.index(',') + 2:]
        item = item[:item.index('\",')].replace('\"', '').replace(" ", "").replace(",", "")
        item = item.replace(',', '').replace("\"", "").replace("$", "")
        if item == 'null':
            endingDealers.append(0)
        else:
            endingDealers.append(float(item))
    return json_response({"endingDealers": endingDealers})


@app.route('/realised_profit_loss_dealers', methods=["POST"])
def realised_profit_loss_dealers():
    start = request.json['start']
    end = request.json['end']
    resp = requests.get(REALISED_DEALERS, json={"start": start, "end": end})
    realised = []
    for item in resp.text.split('], ['):
        item = item.replace('[', '').replace(']', '').replace('\\u00a3', '')
        item = item[item.index(',') + 2:]
        if item == 'null':
            realised.append(0)
        else:
            realised.append(float(item.replace(',', '').replace("\"", "").replace("$", "")))
    return json_response({"realisedDealers": realised})


@app.route('/effective_profit_loss_dealers', methods=["POST"])
def effective_profit_loss_dealers():
    start = request.json['start']
    end = request.json['end']
    resp = requests.get(EFFECTIVE_DEALERS, json={"start": start, "end": end})
    effectiveDealers = []
    for item in resp.text.split('], ['):
        item = item.replace('[', '').replace(']', '').replace('\\u00a3', '')
        item = item[item.index(',') + 2:]
        if item == 'null':
            effectiveDealers.append(0)
        else:
            effectiveDealers.append(float(item.replace(',', '').replace("\"", "").replace("$", "")))
    return json_response({"effectiveDealers": effectiveDealers})


@app.route('/aggregated_ending', methods=["POST"])
def aggregated_ending():
    start = request.json['start']
    end = request.json['end']
    resp = requests.get(AGGREGATED_ENDING, json={"start": start, "end": end})
    endingAggregated = []
    for item in resp.text.split('], ['):
        item = item.replace('[', '').replace(']', '').replace('\\u00a3', '')
        item = item[item.index(',') + 2:]
        item = item[:item.index('\",')].replace('\"', '').replace(" ", "").replace(",", "")
        if item == 'null':
            endingAggregated.append(0)
        else:
            endingAggregated.append(float(item.replace(',', '').replace("\"", "").replace("$", "")))
    return json_response({"endingAggregated": endingAggregated})


@app.route('/aggregated_effective', methods=["POST"])
def aggregated_effective():
    start = request.json['start']
    end = request.json['end']
    resp = requests.get(AGGREGATED_EFFECTIVE, json={"start": start, "end": end})
    effectiveAggregated = resp.text.replace('[', '').replace(']', '').replace('\\u00a3', '')
    if effectiveAggregated == 'null':
        effectiveAggregated = 0
    effectiveAggregated = str(effectiveAggregated).replace("\"", "").replace(" ", "").replace(",", "")
    return json_response({"effectiveAggregated": effectiveAggregated})


@app.route('/aggregated_realised', methods=["POST"])
def aggregated_realised():
    start = request.json['start']
    end = request.json['end']
    resp = requests.get(AGGREGATED_REALISED, json={"start": start, "end": end})
    realisedAggregated = resp.text.replace('[', '').replace(']', '').replace('\\u00a3', '')
    if realisedAggregated == 'null':
        realisedAggregated = 0
    realisedAggregated = str(realisedAggregated).replace("\"", "").replace(" ", "").replace(",", "")
    return json_response({"realisedAggregated": realisedAggregated})


@app.route('/connection', methods=["GET"])
def connection():
    resp = requests.get(PATH + "connection")
    return json_response({"status": resp.text})


def get_data(id):
    time.sleep(1.0)
    data = {"instrumentName": id, "cpty": "Lewis", "price": 9964.235074757127, "type": "S", "quantity": 71,
            "time": "11-Aug-2019 (12:07:06.471252)"}
    return data


@app.route('/get_stream_data')
def get_stream_data():
    def eventStream():
        while True:
            yield 'data:{}\n\n'.format(get_data(random() * 10000))

    return Response(eventStream(), mimetype="text/event-stream")

    # resp = requests.get(GET_STREAM_DATA)
    # return json_response(resp)


def bootapp():
    app.run(port=PORT, threaded=True, host=HOST, debug=True)


if __name__ == '__main__':
    bootapp()
