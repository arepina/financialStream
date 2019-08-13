import json

from flask import Flask, request
from flask_cors import CORS

from database import Database

app = Flask(__name__)
CORS(app)


class Database:
    def __init__(self):
        host = "192.168.99.100"
        user = "root"
        password = "ppp"
        db = "mydata"
        self.con = pymysql.connect(
            host=host, user=user, password=password, db=db)
        self.cur = self.con.cursor()

    def login(self, login, password, user_type):
        self.cur.execute(
            "INSERT INTO `USER`(`login`, `password`, `user_type`) "
            "VALUES ('{0}', '{1}', '{2}')".format(login, password, user_type))
        self.con.commit()

    def sign_up(self, login, password):
        self.cur.execute("SELECT * FROM `USER` "
                         "WHERE `login` = '{0}' and `password` = '{1}'".format(login, password))
        result = self.cur.fetchall()
        return result

    def average(self, type, start, end):
        self.cur.execute(
            "SELECT i.instr_name, avg(d.price) "
            "FROM `DEAL` d INNER JOIN `INSTRUMENT` i "
            "ON d.instrument_id = i.instrument_id "
            "WHERE timestamp > '{0}' AND timestamp < '{1}' AND type = '{2}'"
            "GROUP BY i.instr_name;".format(start, end, type))
        result = self.cur.fetchall()
        return result

    def dealers_position(self, date):
        self.cur.execute("SELECT c.cpty_name, sum(d.price*d.quantity)"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "GROUP BY c.cpty_name;")
        result = self.cur.fetchall()
        return result

    def dealer_position(self, login, date):
        self.cur.execute("SELECT c.cpty_name, sum(d.price*d.quantity)"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "WHERE c.cpty_name = '{0}'"
                         "GROUP BY c.cpty_name;".format(login))
        result = self.cur.fetchall()
        return result

    def insert_deal(self, deal):
        self.cur.execute(
            "INSERT INTO `DEAL` (`name`, `cpty`, `price`, `type`, `quantity`, `time`) "
            "VALUES (deal[0], deal[1], deal[2], deal[3], deal[4], deal[5]")
        self.con.commit()


@app.route('/create_user', methods=['POST'])
def create_user():
    try:
        login = request.json.get('login')
        password = request.json.get('password')
        user_type = request.json.get('userType')
        db = Database()
        db.login(login, password, user_type)
        return app.response_class(
            response=json.dumps('OK'),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )


@app.route('/get_user', methods=['GET'])
def get_user():
    try:
        login = request.json.get('login')
        password = request.json.get('password')
        db = Database()
        data = db.sign_up(login, password)
        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )


@app.route('/average', methods=['GET'])
def average():
    try:
        type = request.json.get('type')  # buy(B) or sell(S)
        start = request.json.get('start')
        end = request.json.get('end')
        db = Database()
        data = db.average(type, start, end)
        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )
        return response


@app.route('/dealers_position', methods=['GET'])
def dealers_position():
    try:
        db = Database()
        data = db.dealers_position()
        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )
        return response


@app.route('/dealer_position', methods=['GET'])
def dealer_position():
    try:
        login = request.json.get('login')
        db = Database()
        data = db.dealer_position(login)
        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )
        return response

@app.route('/streamTime/sse')
def deal_stream():
    def eventStream():
        db = Database()
        while True:
            # nonlocal instrList
            #yield 'data:{}\n\n'.format(get_deal())
            yield db.insert_deal(get_deal())

    #return Response(eventStream(), mimetype="text/event-stream")

@app.route('/deals', methods=['GET'])    
def get_deal():
    """this could be any function that blocks until data is ready"""
    deal = request.json
    name = deal['instrumentName']
    cpty = deal['cpty']
    price = deal['price']
    deal_type = deal['type']
    quantity = deal['quantity']
    time = deal['time']

    return [name, cpty, price, deal_type, quantity, time]


@app.route('/realised_profit_loss_dealers', methods=['GET'])
def realised_profit_loss_dealers():
    try:
        date = request.json.get('date')
        db = Database()
        data = db.realised_profit_loss_dealers(date)
        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )
        return response


@app.route('/realised_profit_loss_dealer', methods=['GET'])
def realised_profit_loss_dealer():
    try:
        login = request.json.get('login')
        date = request.json.get('date')
        db = Database()
        data = db.realised_profit_loss_dealer(date, login)
        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )
        return response


@app.route('/effective_profit_loss_dealers', methods=['GET'])
def effective_profit_loss_dealers():
    try:
        db = Database()
        data = db.effective_profit_loss_dealers()
        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )
        return response


@app.route('/effective_profit_loss_dealer', methods=['GET'])
def effective_profit_loss_dealer():
    try:
        login = request.json.get('login')
        db = Database()
        data = db.effective_profit_loss_dealer(login)
        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )
        return response


@app.route('/aggregated_ending', methods=['GET'])
def aggregated_ending():
    try:
        start = request.json.get('start')
        end = request.json.get('end')
        db = Database()
        data = db.aggregated_ending(start, end)
        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )
        return response


@app.route('/aggregated_effective', methods=['GET'])
def aggregated_effective():
    try:
        date = request.json.get('date')
        db = Database()
        data = db.aggregated_effective(date)
        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )
        return response


@app.route('/aggregated_realised', methods=['GET'])
def aggregated_realised():
    try:
        db = Database()
        data = db.aggregated_realised()
        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )
        return response


@app.route('/add_stream_data', methods=['GET', 'POST'])
def add_stream_data():
    try:
        instrumentName = request.json.get("instrumentName")
        cpty = request.json.get("cpty")
        price = request.json.get("price")
        type = request.json.get("type")
        quantity = request.json.get("quantity")
        time = request.json.get("time")
        db = Database()
        data = db.add_stream_data(instrumentName, cpty, price, type, quantity, time)
        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )
        return response


@app.route('/get_stream_data', methods=['GET'])
def get_stream_data():
    try:
        db = Database()
        data = db.get_stream_data()
        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )
        return response


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)
