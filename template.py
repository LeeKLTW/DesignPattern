# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('sales.db')
cur = conn.cursor()

cur.execute(
    "CREATE TABLE Sales (salesperson text, amt currency, year integer, model text, new boolean);")  # SQLite currency

