# -*- coding: utf-8 -*-
import sqlite3


def init_db():
    conn = sqlite3.connect('sales.db')
    cur = conn.cursor()

    cur.execute(
        "CREATE TABLE Sales (salesperson text, amt currency, year integer, model text, new boolean);")  # currency is a special dtype in SQLite

    cur.execute("INSERT INTO Sales VALUES ('Tim',16000,2010,'Honda Fit','true')")
    conn.commit()
    cur.execute("INSERT INTO Sales VALUES ('Tim',9000,2006,'Ford Focus','false')")
    conn.commit()
    cur.execute("INSERT INTO Sales VALUES ('Gayle', 8000, 2004, 'Dodge Neon', 'false')")
    conn.commit()
    cur.execute("INSERT INTO Sales VALUES ('Gayle', 28000, 2009, 'Ford Mustang', 'true')")
    conn.commit()
    cur.execute("INSERT INTO Sales VALUES ('Gayle', 50000, 2010, 'Lincoln Navigator', 'true')")
    conn.commit()
    cur.execute("INSERT INTO Sales VALUES ('Don', 20000, 2008, 'Toyota Prius', 'false')")
    conn.commit()
    conn.close()


class QueryTemplate:
    def connect(self):
        self.conn = sqlite3.connect('sales.db')
        # self.results, self.query, self.formatted_results

    # todo
    def construct_query(self):
        raise NotImplemented

    def do_query(self):
        cur = self.conn.cursor()
        results = cur.execute(self.query)
        self.results = results.fetchall()

    def format_results(self):
        output = []
        for row in self.results:
            row = [str(i) for i in row]
            output.append(','.join(row))
        self.formatted_results = '\n'.join(output)

    # todo
    def output_results(self):
        raise NotImplemented


class NewVehiclesQuery(QueryTemplate):
    pass


class UserGrossQuery(QueryTemplate):
    pass

