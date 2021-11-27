import csv
import os
import json

main_dir = "C:/Tema R.Cristian"     #creeaza fisier principal in care va fi lista n_cars.csv

try:
    os.mkdir(main_dir)
    print("Directory " , main_dir ,  " Created ",'\n')
except FileExistsError:
    print("Directory " , main_dir ,  " already exists",'\n')

sec_dir = "C:/Tema R.Cristian/output_data"       #creeaza fisier secundar in care vor fi fisierele ptr catalogare masini

try:
    os.mkdir(sec_dir)
    print("Directory " , sec_dir ,  " Created ",'\n')
except FileExistsError:
    print("Directory " , sec_dir ,  " already exists",'\n')

o =  {"id":"1","brand":"Opel","model":"Astra","hp":101,"price":900}
m =  {"id":"2","brand":"Mazda","model":"6","hp":120,"price":2000}
f =  {"id":"3","brand":"Ford","model":"Focus","hp":185,"price":6000}
g =  {"id":"4","brand":"Golf","model": "4","hp": 160,"price": 7000}
me = {"id":"5","brand":"Mercedes","model": "C-Class","hp": 140,"price": 4000}

lista = [o,m, f, g,me]

with open('C:/Tema R.Cristian/n_cars.csv','w',newline='') as new_cars:
    cars = csv.writer(new_cars, delimiter=',')
    cars.writerow(['id','Brand','Model','hp','price'])
    cars.writerow(o.values())
    cars.writerow(m.values())
    cars.writerow(f.values())
    cars.writerow(g.values())
    cars.writerow(me.values())


with open('C:/Tema R.Cristian/n_cars.csv','r') as new_cars:
    rows = csv.reader(new_cars, delimiter=',')
    next(new_cars)
    for row in rows:
        print (row)
print()

slow_cars = [i['brand'] for i in lista if i["hp"]<120]
fast_cars = [i['brand'] for i in lista if 120<= i["hp"]<180]
sport_cars = [i['brand'] for i in lista if i["hp"]>=180]

cheap = [i['brand'] for i in lista if i["price"]<1000]
medium = [i['brand'] for i in lista if 1000<= i["price"]<5000]
expensive = [i['brand'] for i in lista if i["price"]>=5000]

print("Slow_cars:", [i['brand'] for i in lista if i["hp"]<120])
print("Fast_cars:", [i['brand'] for i in lista if 120<= i["hp"]<180])
print("Sport_cars:", [i['brand'] for i in lista if i["hp"]>=180],"\n")

print("Cheap", [i['brand'] for i in lista if i["price"]<1000])
print("Medium:", [i['brand'] for i in lista if 1000<= i["price"]<5000])
print("Expensive", [i['brand'] for i in lista if i["price"]>=5000],"\n")


with open('C:/Tema R.Cristian/output_data/slow_cars.json','w') as slow:
    sl = json.dumps(slow_cars)
    slow.write(sl)

with open('C:/Tema R.Cristian/output_data/fast_cars.json','w') as fast:
    fa = json.dumps(fast_cars)
    fast.write(fa)

with open('C:/Tema R.Cristian/output_data/sport_cars.json','w') as sport:
    sp = json.dumps(sport_cars)
    sport.write(sp)

with open('C:/Tema R.Cristian/output_data/cheap_cars.json','w') as ieftin:
    ch = json.dumps(cheap)
    ieftin.write(ch)

with open('C:/Tema R.Cristian/output_data/medium_cars.json', 'w') as mediu:
    me = json.dumps(medium)
    mediu.write(me)

with open('C:/Tema R.Cristian/output_data/expensive_cars.json', 'w') as scump:
    sc = json.dumps(expensive)
    scump.write(sc)


with open('C:/Tema R.Cristian/output_data/Opel.json', 'w') as opel:
    for i in lista:
        if i['brand']=='Opel':
            z=i
            opel.write(str(i))

with open('C:/Tema R.Cristian/output_data/Mazda.json', 'w') as mazda:
    for i in lista:
        if i['brand']=='Mazda':
            z=i
            mazda.write(str(i))

with open('C:/Tema R.Cristian/output_data/Ford.json', 'w') as ford:
    for i in lista:
        if i['brand']=='Ford':
            z=i
            ford.write(str(i))

with open('C:/Tema R.Cristian/output_data/Golf.json', 'w') as golf:
    for i in lista:
        if i['brand']=='Golf':
            z=i
            golf.write(str(i))

with open('C:/Tema R.Cristian/output_data/Mercedes.json', 'w') as mercedes:
    for i in lista:
        if i['brand']=='Mercedes':
            z=i
            mercedes.write(str(i))

# nu am stiut cum sa fac sa imi aranjeze frumos datele cu indent la ultima parte