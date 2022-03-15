import psycopg2
import time
import myutils
import requests
import json

conn = psycopg2.connect(host='pg.pg4e.com',
        port='5432',
        database='pg4e_11a47e7d53',
        user='pg4e_11a47e7d53',
        password='pg4e_p_cffa18ffa866593',
        connect_timeout=3)
cur = conn.cursor()
sql = 'CREATE TABLE IF NOT EXISTS pokeapi (id INTEGER, body JSONB);'
cur.execute(sql)
defaulturl = 'https://pokeapi.co/api/v2/pokemon/1'
for i in range(1, 100):
        sql = f"INSERT INTO swapi (url) VALUES ( 'https://pokeapi.co/api/v2/pokemon/{i}' )";
        print(sql)
        cur.execute(sql, (defaulturl))
conn.commit()
