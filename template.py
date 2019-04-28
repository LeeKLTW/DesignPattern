# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('sales.db')
cur = conn.cursor()

cur.execute(
    "CREATE TABLE Sales (salesperson text, amt currency, year integer, model text, new boolean);")  # SQLite currency

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
