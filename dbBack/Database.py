import pymysql


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
            "SELECT i.instr_name, avg(d.price)"
            "FROM DEAL d INNER JOIN INSTRUMENT i ON d.instrument_id = i.instrument_id"
            "WHERE d.timestamp > '{0}' AND d.timestamp <= '{1}' AND d.type = '{2}'"
            "GROUP BY i.instr_name;".format(start, end, type))
        result = self.cur.fetchall()
        return result

    def dealers_position(self, start, end):
        self.cur.execute("SELECT c.cpty_name, "
                         "SUM(CASE "
                         "WHEN d.type = 'B' THEN -d.price*d.quantity"
                         "WHEN d.type = 'S' THEN d.price*d.quantity END) AS dealer_revenue"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "WHERE d.timestamp > '{0}' AND d.timestamp <= '{1}'"
                         "GROUP BY c.cpty_name;".format(start, end))
        result = self.cur.fetchall()
        return result

    def dealer_position(self, login, start, end):
        self.cur.execute("SELECT c.cpty_name, sum(d.price*d.quantity)"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "WHERE c.cpty_name = '{0}' AND d.timestamp > '{1}' AND d.timestamp <= '{2}'"
                         "GROUP BY c.cpty_name;".format(login, start, end))
        result = self.cur.fetchall()
        return result

    def realised_profit_loss_dealers(self, date):
        self.cur.execute("SELECT c.cpty_name, "
                         "SUM(CASE "
                         "WHEN d.type = 'B' THEN -d.price*d.quantity"
                         "WHEN d.type = 'S' THEN d.price*d.quantity"
                         "END) AS rev"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "WHERE d.timestamp > '%{0}%'"
                         "GROUP BY c.cpty_name;".format(date))
        result = self.cur.fetchall()
        return result

    def realised_profit_loss_dealer(self, date, login):
        self.cur.execute("SELECT c.cpty_name, "
                         "SUM(CASE "
                         "WHEN d.type = 'B' THEN -d.price*d.quantity"
                         "WHEN d.type = 'S' THEN d.price*d.quantity"
                         "END) AS rev"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "WHERE c.cpty_name = '{0}' AND d.timestamp > '%{1}%'"
                         "GROUP BY c.cpty_name;".format(login, date))
        result = self.cur.fetchall()
        return result

    def effective_profit_loss_dealers(self):
        self.cur.execute("SELECT c.cpty_name, "
                         "SUM(CASE"
                         "WHEN d.type = 'B' THEN -d.price*d.quantity"
                         "WHEN d.type = 'S' THEN d.price*d.quantity"
                         "END) AS rev"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "GROUP BY c.cpty_name;")
        result = self.cur.fetchall()
        return result

    def effective_profit_loss_dealer(self, login):
        self.cur.execute("SELECT c.cpty_name,"
                         "SUM(CASE"
                         "WHEN d.type = 'B' THEN -d.price*d.quantity"
                         "WHEN d.type = 'S' THEN d.price*d.quantity"
                         "END) AS rev"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "WHERE c.cpty_name = '{0}'"
                         "GROUP BY c.cpty_name;".format(login))
        result = self.cur.fetchall()
        return result

    def aggregated_ending(self, start, end):
        self.cur.execute("SELECT SUM(CASE"
                         "WHEN d.type = 'B' THEN -d.price*d.quantity"
                         "WHEN d.type = 'S' THEN d.price*d.quantity"
                         "END) AS rev"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "WHERE d.timestamp > '{0}' AND d.timestamp <= '{1}';".format(start, end))
        result = self.cur.fetchall()
        return result

    def aggregated_effective(self, date):
        self.cur.execute("SELECT SUM(CASE"
                         "WHEN d.type = 'B' THEN -d.price*d.quantity"
                         "WHEN d.type = 'S' THEN d.price*d.quantity"
                         "END) AS rev"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "WHERE d.timestamp > '%{0}%';".format(date))
        result = self.cur.fetchall()
        return result

    def aggregated_realised(self):
        self.cur.execute("SELECT SUM(CASE"
                         "WHEN d.type = 'B' THEN -d.price*d.quantity"
                         "WHEN d.type = 'S' THEN d.price*d.quantity"
                         "END) AS rev"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id;")
        result = self.cur.fetchall()
        return result

    def add_stream_data(self, instrumentName, cpty, price, type, quantity, time):
        #TODO MORE INSERTS
        self.cur.execute(
            "INSERT INTO `DEAL`(instrumentName, cpty, price, type, quantity, time) VALUES({0}, {1}, {2}, {3}, {4}, {5})"
                .format(instrumentName, cpty, price, type, quantity, time))
        result = self.cur.fetchall()
        return result

    def get_stream_data(self):
        #TODO Join with other tables
        self.cur.execute("SELECT * FROM `DEAL`")
        result = self.cur.fetchall()
        return result
