import sqlite3
conn=sqlite3.connect('user_db.db')
c=conn.cursor()
# create_query="CREATE TABLE users(user_name TEXT, user_password TEXT);"
# users=[
#     ('Janet', '1234'),
#     ('Alexx', '5678'),
#     ('Sem', '9012')
# ]

# insert_fun="INSERT INTO users VALUES(?,?);"
users_name=input('Enter you name ')
users_pasword=input('Enter you pasword ')
list_info=(users_name,users_pasword)

select_query=f"SELECT * FROM users WHERE user_name=? AND user_password=?"

cursor=conn.cursor()
# cursor.executemany(insert_fun,users)
cursor.execute(select_query, list_info)
data=cursor.fetchone()
if(data):
    print ('You are logged in')
else:
    print ('Wrong!!!')
conn.commit()
conn.close()