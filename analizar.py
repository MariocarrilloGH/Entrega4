"""
Programa para analizar los datos obtenidos.
"""
from itertools import islice
f = open('datos.txt','r',encoding="utf8")
edades = [0,1,2,3,4,5,6]
años = ['2019','2020']
estaciones = ['Primavera','Verano','Otoño','Invierno']
lines = f.readlines()
datos =[[],[],[]]
Porcentajes2019=[[],[],[],[]]
Porcentajes2020=[[],[],[],[]]
totales19 = []
totales20 = []
estacion = ''
for i in lines:
    for k in estaciones:
        if k in i:
            estacion = k
    l = i.split()
    new = []
    try:
        if estacion != '':
            if l[5]=='0':
                new = [l[2],l[8][:-1],l[10][:-1]]
                datos[0].append([estacion,new])
            elif l[5]=='1':
                new = [l[2],l[8][:-1],l[10][:-1]]
                datos[1].append([estacion,new])
            elif l[5]=='2':
                new = [l[2],l[8][:-1],l[10][:-1]]
                datos[2].append([estacion,new])
    except:
        next
for k in range(3):
    t = 0
    p = 0
    for i in datos[k]:
        p = t//7
        Porcentajes2019[p].append(int(i[1][1]))
        Porcentajes2020[p].append(int(i[1][2]))
        t = t+1
for k in range(4):
    total = 0
    p = 0
    for i in Porcentajes2019[k]:
        total = total + i
        p += 1
        if (p)%7==0:
            totales19.append(total)
            total = 0
    for i in Porcentajes2020[k]:
        total = total + i
        p += 1
        if (p)%7==0:
            totales20.append(total)
            total = 0
p = 0
for i in Porcentajes2019:
    for k in range(len(i)):
        i[k]= round(i[k]/totales19[(k//7) + 3*p],3)
    p += 1
p = 0
for i in Porcentajes2020:
    for k in range(len(i)):
        i[k]= round(i[k]/totales20[(k//7)+3*p],3)
    p += 1
primavera2019 = {0:Porcentajes2019[0][0:6],1:Porcentajes2019[0][7:13],2:Porcentajes2019[0][14:20]}
verano2019 = {0:Porcentajes2019[1][0:6],1:Porcentajes2019[1][7:13],2:Porcentajes2019[1][14:20]}
otoño2019 = {0:Porcentajes2019[2][0:6],1:Porcentajes2019[2][7:13],2:Porcentajes2019[2][14:20]}
invierno2019 = {0:Porcentajes2019[3][0:6],1:Porcentajes2019[3][7:13],2:Porcentajes2019[3][14:20]}
primavera2020 = {0:Porcentajes2020[0][0:6],1:Porcentajes2020[0][7:13],2:Porcentajes2020[0][14:20]}
verano2020 = {0:Porcentajes2020[1][0:6],1:Porcentajes2020[1][7:13],2:Porcentajes2020[1][14:20]}
otoño2020 = {0:Porcentajes2020[2][0:6],1:Porcentajes2020[2][7:13],2:Porcentajes2020[2][14:20]}
invierno2020 = {0:Porcentajes2020[3][0:6],1:Porcentajes2020[3][7:13],2:Porcentajes2020[3][14:20]}
print('en primavera los porcentajes son:',primavera2019,'para 2019 y',primavera2020,'para 2020')
print('en verano los porcentajes son:',verano2019,'para 2019 y',verano2020,'para 2020')
print('en otoño los porcentajes son:',otoño2019,'para 2019 y',otoño2020,'para 2020')
print('en invierno los porcentajes son:',invierno2019,'para 2019 y',invierno2020,'para 2020')
















