# import requests
#
# url=('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02&latitude=51.51&longitude=-0.12&maxradiuskm=20000')
# res=requests.get(url, headers={'Accept':"application/json"})
#
# data=res.json()
# print(data['features'][0]['properties']["place"])


import requests

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
count=0
for earthquake in earthquake_list:
    count+=1
    print(f"{count}.Place:{earthquake['properties']['place']}.")


