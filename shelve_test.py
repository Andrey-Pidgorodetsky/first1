import shelve


with shelve.open('Shelve_Tests') as cars:
    cars ['Opel']='Germany'
    cars ['Bmv']= 'Germany'
    cars ['Ford']= 'USA'

    print(cars['Opel'])
    print(cars['Bmv'])
    print(cars['Ford'])

    for key in cars:
        print(key)
    while True :
        key=input('Введите имя машины: ' )
        if key=='quit':
            break
        if key in cars:
            country=cars[key]
            print(country)
        else:
            print( key+" нету")
        odered_list_key=list(cars.keys())
        odered_list_key.sort()

        for key in odered_list_key:
            print(key+ ' - '+ cars[key])

        for value in odered_list_key:
            print(cars.values())
        for item in odered_list_key:
            print(cars.items())
