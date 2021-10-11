import requests
import sqlite3
def save_earthquake(magnitude_list):
    conn=sqlite3.connect('earthquake_db.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE earthquake(place TEXT, magnitude REAL)''')
    c.executemany("INSERT INTO earthquake VALUES(?,?)",magnitude_list)
    conn.commit()
    conn.close()
    
    
    


url='https://earthquake.usgs.gov/fdsnws/event/1/query?'

start=input('Введите время начала ')
end=input('Введите время конца ')
shir=input('Введите широту ')
long=input("Введите долготу ")
km=input("Введите расстояние в км ")


response=requests.get(url, headers={"Accept":'application/json'}, params={
    'format':'geojson',
    'starttime':start,
    'endtime':end,
    'latitude':shir,
    'longitude':long,
    'maxradiuskm':km
})

data= response.json()

earthquake_list=data['features']
magnitude_list=[]
count=0
for earthquake in earthquake_list:
    count+=1
    # print(f"{count}.Place:{earthquake['properties']['place']}.")
    magnitude_list.append((earthquake['properties']['place'], earthquake['properties']['mag']))



save_earthquake(magnitude_list)
