import sqlite3
conn=sqlite3.connect('cars_db.db')
c=conn.cursor()

# c.execute('''CREATE TABLE cars(model TEXT, price INTEGER, make TEXT)''')
# c.execute('''INSERT INTO cars VALUES('Tesla', 100000, 'Tesla Factory')''')
# first_model='A8'
# cost= 10000
# factory= 'Audi'
# list_sql=(first_model,cost,factory)
# insert_qery="INSERT INTO cars VALUES(?,?,?)"
# c.execute(insert_qery, list_sql)
# conn.commit()
# conn.close()
list_models=[
    ('SLS',50000,'Mercedes'),
    ('R8',80000,'Audi'),
    ('HZ',50000,'Kia')
]
insert="INSERT INTO cars VALUES(?,?,?);"
for car in list_models:
    c.executemany(insert, list_models)
conn.commit()
conn.close()