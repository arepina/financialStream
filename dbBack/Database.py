import pymysql

from endpoints import DB_HOST


class Database:
    def __init__(self):
        host = DB_HOST
        user = "admin"
        password = "admin"
        db = "sampledb"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db)
        self.cur = self.con.cursor()

    def login(self, login, password):
        self.cur.execute("SELECT * FROM USER "
                         "WHERE login = '{0}' and password = '{1}';".format(login, password))
        result = self.cur.fetchall()
        if len(result) != 0:
            return result
        raise Exception()

    def sign_up(self, login, password, user_type):
        self.cur.execute(
            "INSERT INTO USER(login, password, user_type) "
            "VALUES ('{0}', SHA1('{1}'), '{2}');".format(login, password, user_type))
        self.con.commit()

    def average(self, start, end):
        self.cur.execute("(SELECT i.instrument_name, "
                         "concat('$ ', format((AVG(CASE WHEN d.type = 'B' THEN d.price END))"
                         ", 2)) AS 'Average Buy Price', "
                         "concat('$ ', format((AVG(CASE WHEN d.type = 'S' THEN d.price END))"
                         ", 2)) AS 'Average Sell Price' "
                         "FROM INSTRUMENT i LEFT JOIN DEAL d ON i.instrument_id = d.instrument_id "
                         "WHERE d.timestamp > '{0}'"
                         "AND d.timestamp <= '{1}'"
                         "GROUP BY i.instrument_name) "
                         "UNION "
                         "(SELECT i.instrument_name, NULL, NULL FROM INSTRUMENT i "
                         "WHERE i.instrument_name NOT IN (SELECT i.instrument_name "
                         "FROM INSTRUMENT i LEFT JOIN DEAL d ON i.instrument_id = d.instrument_id "
                         "WHERE d.timestamp > '{0}' AND d.timestamp "
                         "<= '{1}' GROUP BY i.instrument_name)) "
                         "ORDER BY instrument_name asc;".format(start, end))
        result = self.cur.fetchall()
        return result

    def dealers_position(self, start, end):
        self.cur.execute("SELECT c.cpty_name, i.instrument_name, "
                         "concat('$ ', format((SUM(CASE "
                         "WHEN d.type = 'B' THEN -d.price * d.quantity "
                         "WHEN d.type = 'S' THEN d.price * d.quantity END)), 2)) AS 'Ending Position', "
                         "SUM(CASE WHEN d.type = 'B' THEN d.quantity END) AS 'Quantity Bought', "
                         "SUM(CASE WHEN d.type = 'S' THEN d.quantity END) AS 'Quantity Sold', "
                         "SUM(CASE WHEN d.type = 'B' THEN d.quantity "
                         "WHEN d.type = 'S' THEN -d.quantity END) AS 'End Quantity' "
                         "FROM COUNTER_PARTY c LEFT JOIN(DEAL d LEFT JOIN INSTRUMENT i "
                         "ON d.instrument_id = i.instrument_id) "
                         "ON d.counter_party_id = c.counter_party_id "
                         "WHERE d.timestamp > '{0}' AND d.timestamp <= '{1}' "
                         "GROUP BY c.cpty_name, i.instrument_name "
                         "ORDER BY c.cpty_name asc, i.instrument_name asc;".format(start, end))
        result = self.cur.fetchall()
        return result

    def dealer_position(self, login, start, end):
        self.cur.execute("SELECT c.cpty_name, i.instrument_name, "
                         "concat('$ ', format((SUM(CASE "
                         "WHEN d.type = 'B' THEN -d.price * d.quantity "
                         "WHEN d.type = 'S' THEN d.price * d.quantity END)), 2)) AS 'Ending Position', "
                         "SUM(CASE WHEN d.type = 'B' THEN d.quantity END) AS 'Quantity Bought', "
                         "SUM(CASE WHEN d.type = 'S' THEN d.quantity END) AS 'Quantity Sold', "
                         "SUM(CASE WHEN d.type = 'B' THEN d.quantity "
                         "WHEN d.type = 'S' THEN -d.quantity END) AS 'End Quantity' "
                         "FROM COUNTER_PARTY c INNER JOIN(DEAL d INNER JOIN INSTRUMENT i "
                         "ON d.instrument_id = i.instrument_id) "
                         "ON d.counter_party_id = c.counter_party_id "
                         "WHERE d.timestamp > '{0}' AND d.timestamp <= '{1}' "
                         "AND c.cpty_name = '{2}'"
                         "GROUP BY c.cpty_name, i.instrument_name "
                         "ORDER BY c.cpty_name asc, i.instrument_name asc;".format(start, end, login))
        result = self.cur.fetchall()
        return result

    def realised_profit_loss_dealers(self, start, end):
        self.cur.execute("CREATE VIEW realized_profit_loss AS "
                         "SELECT c.cpty_name, (SUM(CASE "
                         "WHEN d.type = 'S' THEN d.quantity END)) * "
                         "((AVG(CASE WHEN d.type = 'S' THEN d.price "
                         "END)) - (AVG(CASE WHEN d.type = 'B' "
                         "THEN d.price END))) AS realized_profit_loss "
                         "FROM INSTRUMENT i INNER JOIN(DEAL d "
                         "INNER JOIN COUNTER_PARTY c "
                         "ON d.counter_party_id = c.counter_party_id) "
                         "ON i.instrument_id = d.instrument_id "
                         "WHERE d.timestamp > '{0}' AND "
                         "d.timestamp < '{1}' "
                         "GROUP BY c.cpty_name, i.instrument_name;".format(start, end))
        self.con.commit()
        self.cur.execute("SELECT cpty_name, "
                         "concat('$ ', format(SUM(realized_profit_loss), 2)) "
                         "AS realized_profit_loss "
                         "FROM realized_profit_loss GROUP BY cpty_name ORDER BY cpty_name asc;")
        result = self.cur.fetchall()
        self.cur.execute("DROP VIEW realized_profit_loss;")
        self.con.commit()
        return result

    def realised_profit_loss_dealer(self, start, end, login):
        self.cur.execute("CREATE VIEW realized_profit_loss AS "
                         "SELECT c.cpty_name, (SUM(CASE "
                         "WHEN d.type = 'S' THEN d.quantity END)) * "
                         "((AVG(CASE WHEN d.type = 'S' THEN d.price "
                         "END)) - (AVG(CASE WHEN d.type = 'B' "
                         "THEN d.price END))) AS realized_profit_loss "
                         "FROM INSTRUMENT i INNER JOIN(DEAL d "
                         "INNER JOIN COUNTER_PARTY c "
                         "ON d.counter_party_id = c.counter_party_id) "
                         "ON i.instrument_id = d.instrument_id "
                         "WHERE d.timestamp > '{0}' AND "
                         "d.timestamp < '{1}' "
                         "GROUP BY c.cpty_name, i.instrument_name;".format(start, end))
        self.con.commit()
        self.cur.execute("SELECT cpty_name, "
                         "concat('$ ', format(SUM(realized_profit_loss), 2)) "
                         "AS realized_profit_loss "
                         "FROM realized_profit_loss "
                         "WHERE cpty_name = '{0}'"
                         "GROUP BY cpty_name ORDER BY cpty_name asc;".format(login))
        result = self.cur.fetchall()
        self.cur.execute("DROP VIEW realized_profit_loss;")
        self.con.commit()
        return result

    def effective_profit_loss_dealers(self, start, end):
        self.cur.execute("CREATE VIEW effective_profit_loss AS SELECT c.cpty_name, "
                         "(SUM(CASE WHEN d.type = 'B' THEN d.quantity WHEN d.type = 'S' THEN -d.quantity "
                         "END)) * ((AVG(CASE WHEN d.type = 'S' THEN d.price END)) - (AVG(CASE "
                         "WHEN d.type = 'B' THEN d.price END))) AS effective_profit_loss "
                         "FROM INSTRUMENT i INNER JOIN (DEAL d INNER JOIN COUNTER_PARTY c "
                         "ON d.counter_party_id = c.counter_party_id) ON i.instrument_id = d.instrument_id "
                         "WHERE d.timestamp > '{0}' AND d.timestamp < '{1}' "
                         "GROUP BY c.cpty_name, i.instrument_name;".format(start, end))
        self.con.commit()
        self.cur.execute("SELECT cpty_name, "
                         "concat('$ ', format(SUM(effective_profit_loss), 2)) AS effective_profit_loss "
                         "FROM effective_profit_loss GROUP BY cpty_name ORDER BY cpty_name asc;")
        result = self.cur.fetchall()
        self.cur.execute("DROP VIEW effective_profit_loss;")
        self.con.commit()
        return result

    def effective_profit_loss_dealer(self, start, end, login):
        self.cur.execute("CREATE VIEW effective_profit_loss AS SELECT c.cpty_name, "
                         "(SUM(CASE WHEN d.type = 'B' THEN d.quantity WHEN d.type = 'S' THEN -d.quantity "
                         "END)) * ((AVG(CASE WHEN d.type = 'S' THEN d.price END)) - (AVG(CASE "
                         "WHEN d.type = 'B' THEN d.price END))) AS effective_profit_loss "
                         "FROM INSTRUMENT i INNER JOIN (DEAL d INNER JOIN COUNTER_PARTY c "
                         "ON d.counter_party_id = c.counter_party_id) ON i.instrument_id = d.instrument_id "
                         "WHERE d.timestamp > '{0}' AND d.timestamp < '{1}' "
                         "GROUP BY c.cpty_name, i.instrument_name;".format(start, end))
        self.con.commit()
        self.cur.execute("SELECT cpty_name, "
                         "concat('$ ', format(SUM(effective_profit_loss), 2)) AS effective_profit_loss "
                         "FROM effective_profit_loss "
                         "WHERE cpty_name = '{0}' "
                         "GROUP BY cpty_name ORDER BY cpty_name asc;".format(login))
        result = self.cur.fetchall()
        self.cur.execute("DROP VIEW effective_profit_loss;")
        self.con.commit()
        return result

    def aggregated_ending(self, start, end):
        self.cur.execute("(SELECT i.instrument_name, concat('$ ', format(SUM(CASE WHEN d.type = 'B' THEN "
                         "-d.price * d.quantity WHEN d.type = 'S' THEN d.price * d.quantity "
                         "END), 2)) AS 'Ending Position', SUM(CASE WHEN d.type = 'B' THEN "
                         "d.quantity END) AS 'Quantity Bought', "
                         "SUM(CASE WHEN d.type = 'S' THEN d.quantity END) AS 'Quantity Sold', "
                         "SUM(CASE WHEN d.type = 'B' THEN d.quantity "
                         "WHEN d.type = 'S' THEN -d.quantity END) AS 'End Quantity' FROM COUNTER_PARTY c LEFT JOIN "
                         "(DEAL d LEFT JOIN INSTRUMENT i ON d.instrument_id = i.instrument_id) ON "
                         "c.counter_party_id = d.counter_party_id WHERE d.timestamp > '{0}' "
                         "AND d.timestamp <= '{1}' GROUP BY i.instrument_name) "
                         "UNION "
                         "(SELECT i.instrument_name, NULL, NULL, NULL, NULL FROM INSTRUMENT i "
                         "WHERE i.instrument_name NOT IN (SELECT i.instrument_name FROM COUNTER_PARTY c "
                         "LEFT JOIN (DEAL d LEFT JOIN INSTRUMENT i ON d.instrument_id = i.instrument_id) "
                         " ON c.counter_party_id = d.counter_party_id WHERE d.timestamp > '{0}' "
                         "AND d.timestamp <= '{1}' GROUP BY i.instrument_name)) "
                         "ORDER BY instrument_name asc;".format(start, end))
        result = self.cur.fetchall()
        return result

    def aggregated_realised(self, start, end):
        self.cur.execute("CREATE VIEW realized_profit_loss AS "
                         "SELECT c.cpty_name, (SUM(CASE "
                         "WHEN d.type = 'S' THEN d.quantity END)) * "
                         "((AVG(CASE WHEN d.type = 'S' THEN d.price "
                         "END)) - (AVG(CASE WHEN d.type = 'B' "
                         "THEN d.price END))) AS realized_profit_loss "
                         "FROM INSTRUMENT i INNER JOIN(DEAL d "
                         "INNER JOIN COUNTER_PARTY c "
                         "ON d.counter_party_id = c.counter_party_id) "
                         "ON i.instrument_id = d.instrument_id "
                         "WHERE d.timestamp > '{0}' AND "
                         "d.timestamp < '{1}' "
                         "GROUP BY c.cpty_name, i.instrument_name;".format(start, end))
        self.con.commit()
        self.cur.execute("SELECT concat('$ ', format(SUM(realized_profit_loss), 2)) "
                         "AS 'Aggregated Realized Profit/Loss' "
                         "FROM realized_profit_loss;")
        result = self.cur.fetchall()
        self.cur.execute("DROP VIEW realized_profit_loss;")
        self.con.commit()
        return result

    def aggregated_effective(self, start, end):
        self.cur.execute("CREATE VIEW effective_profit_loss AS SELECT c.cpty_name, "
                         "(SUM(CASE WHEN d.type = 'B' THEN d.quantity WHEN d.type = 'S' THEN -d.quantity "
                         "END)) * ((AVG(CASE WHEN d.type = 'S' THEN d.price END)) - (AVG(CASE "
                         "WHEN d.type = 'B' THEN d.price END))) AS effective_profit_loss "
                         "FROM INSTRUMENT i INNER JOIN (DEAL d INNER JOIN COUNTER_PARTY c "
                         "ON d.counter_party_id = c.counter_party_id) ON i.instrument_id = d.instrument_id "
                         "WHERE d.timestamp > '{0}' AND d.timestamp < '{1}' "
                         "GROUP BY c.cpty_name, i.instrument_name;".format(start, end))
        self.con.commit()
        self.cur.execute("SELECT concat('$ ', format(SUM(effective_profit_loss), 2)) "
                         "AS 'Aggregated Effective Profit/Loss' "
                         "FROM effective_profit_loss;")
        result = self.cur.fetchall()
        self.cur.execute("DROP VIEW effective_profit_loss;")
        self.con.commit()
        return result

    def get_stream_data(self):
        self.cur.execute("SELECT * FROM INSTRUMENT i INNER JOIN "
                         "(DEAL d INNER JOIN COUNTER_PARTY c "
                         "ON d.counter_party_id = c.counter_party_id) "
                         "ON i.instrument_id = d.instrument_id;")
        result = self.cur.fetchall()
        return result

    def add_stream_data(self, instrumentName, cpty, price, quantity, type, time):
        self.cur.execute("SELECT instrument_id FROM INSTRUMENT "
                         "WHERE instrument_name = '{0}';".format(instrumentName))
        instr_id = self.cur.fetchone()[0]
        self.cur.execute("SELECT counter_party_id FROM COUNTER_PARTY "
                         "WHERE cpty_name = '{0}';".format(cpty))
        cpty_id = self.cur.fetchone()[0]
        time_local = time.replace('-', ' ')
        time_local = time_local.split()
        if time_local[1] == 'Jan':
            time_local[1] = '01'
        elif time_local[1] == 'Feb':
            time_local[1] = '02'
        elif time_local[1] == 'Mrz':
            time_local[1] = '03'
        elif time_local[1] == 'Apr':
            time_local[1] = '04'
        elif time_local[1] == 'May':
            time_local[1] = '05'
        elif time_local[1] == 'Jun':
            time_local[1] = '06'
        elif time_local[1] == 'Jul':
            time_local[1] = '07'
        elif time_local[1] == 'Aug':
            time_local[1] = '08'
        elif time_local[1] == 'Sep':
            time_local[1] = '09'
        elif time_local[1] == 'Oct':
            time_local[1] = '10'
        elif time_local[1] == 'Nov':
            time_local[1] = '11'
        else:
            time_local[1] = '12'
        time_string = time_local[2] + "-" + time_local[1] + "-" + time_local[0] + " " + time_local[3]
        self.cur.execute("INSERT INTO DEAL (instrument_id, counter_party_id, price, quantity, type, timestamp) VALUES ({0}, {1}, {2}, {3}, '{4}', CAST('{5}' AS DATETIME));".format(instr_id, cpty_id, price, quantity, type, time_string))
        self.con.commit()

    def insert_initial_counter_party(self):
        self.cur.execute("INSERT INTO COUNTER_PARTY (cpty_name) VALUES "
                         "('Lewis'), ('Selvyn'), ('Richard'), ('Lina'), ('John'), ('Nidia');")
        self.con.commit()

    def insert_initial_instrument(self):
        self.cur.execute("INSERT INTO INSTRUMENT (instrument_name) VALUES "
                         "('Astronomica'), ('Borealis'), ('Celestial'), ('Deuteronic'), "
                         "('Eclipse'), ('Floral'), ('Galactia'), ('Heliosphere'), "
                         "('Interstella'), ('Jupiter'), ('Koronis'), ('Lunatic');")
        self.con.commit()

    def close_connection(self):
        self.cur.close()
        self.con.close()

