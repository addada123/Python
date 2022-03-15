import psycopg2

conn = psycopg2.connect(host='pg.pg4e.com',
        port='5432',
        database='pg4e_11a47e7d53',
        user='pg4e_11a47e7d53',
        password='pg4e_p_cffa18ffa866593',
        connect_timeout=3)

cur = conn.cursor()
sql = 'DROP TABLE IF EXISTS pythonseq CASCADE;'
print(sql)
cur.execute(sql)

sql = 'CREATE TABLE pythonseq (iter INTEGER, val INTEGER);'
print(sql)
cur.execute(sql)
number = 454504
for i in range(300) :
    print(i+1, number)
    value = number
    sql = "INSERT INTO pythonseq (val) values (%s);"
    cur.execute(sql, (value, ))
    number = int((value * 22) / 7) % 1000000
conn.commit()
cur.close()