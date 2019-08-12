from flask import Flask, render_template
import pymysql
import json

app = Flask(__name__)


class Database:
    def __init__(self):
        host = "192.168.99.100"
        user = "root"
        password = "ppp"
        db = "mydata"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db)
        self.cur = self.con.cursor()

    def login(self, login, password, user_type):
        self.cur.execute(
            "INSERT INTO `USER`(login, password, user_type) VALUES ({0}, {1}, {2})".format(login, password, user_type))
        result = self.cur.fetchall()
        return result

    def sign_up(self, login, password):
        self.cur.execute("SELECT * FROM `USER` WHERE `login` = {0} and `password` = {1}".format(login, password))
        result = self.cur.fetchall()
        return result

@app.route('/login', methods=['POST'])
def login():
    login = request.args.get('login')
    password = request.args.get('password')
    user_type = request.args.get('user_type')
    try:
        db = Database()
        data = db.login(login, password, user_type)
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )
        return response


@app.route('/signup', methods=['GET'])
def signup():
    login = request.args.get('login')
    password = request.args.get('password')
    try:
        db = Database()
        data = db.sign_up(login, password)
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )
        return response

@app.route('/', methods=['GET'])
def test():
   return json.dumps("hi!")