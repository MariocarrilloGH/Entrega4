from pyspark import SparkContext, SparkConf
import json
from pprint import pprint
import datetime
import sys

def get_trip(line):
    data = json.loads(line)
    s_date = data["unplug_hourTime"]
    if isinstance(s_date, str):
        s_date = s_date.replace("Z","+0000")
        data["unplug_hourTime"] = datetime.datetime.strptime(s_date, "%Y-%m-%dT%H:%M:%S%z")
    else:
        s_date = s_date['$date']
        data["unplug_hourTime"] = datetime.datetime.strptime(s_date, "%Y-%m-%dT%H:%M:%S.%f%z")
    return data

def mapper(line):
    data = get_trip(line)
    user_age = data['ageRange']
    trip_hour = data['unplug_hourTime']
    return user_age, trip_`hour

def get_return_users(rdd, selected_age, selected_hour):
    users = rdd.map(mapper)\
        .filter(lambda x: x[0]==selected_age and selected_hour*8<=x[1]<=(selected_hour+1)*8)\#NOTA: Lo del x[1] en el rango de hora hay que arreglarlo 100% porque no se como es el formato de x[1]
    return users

def main(sc, years, months, datadir):
     rdd = sc.parallelize([])
     for y in years:
         for m in months:
             filename = f"{datadir}/{y}{m:02}_movements.json"
             print(f"Adding {filename}")
             rdd = rdd.union(sc.textFile(filename))
     for ageRange in range(0,7):
         for hourRange in range(0,3):
             rddAux = rdd #Meto el rddAux porque no se si al calcular con la siguiente hourRange el rdd se habrá jodido por hacerle el filter dentro de get_return_users (tal vez no hace falta)
             users = get_return_users(rddAux, ageRange,)
             print("............Starting computations.............")
             print(f"Age range: {ageRange}, Hour range: {hourRange*8}:00-{(hourRange+1)*8}:00")
             print(f"There are {trips.count()} return trips")
             for t in users.take(10):
                 print(t)

if __name__=="__main__":
    if len(sys.argv)<2:
        years = [2021]
    else:
        years = list(map(int, sys.argv[1].split()))

    if len(sys.argv)<3:
        months = [3]
    else:
        months = list(map(int, sys.argv[2].split()))

    if len(sys.argv)<4:
        datadir = "."
    else:
        datadir = sys.argv[3]

    print(f"years: {years}")
    print(f"months: {months}")
    print(f"datadir: {datadir}")
    
    sc = SparkContext()1
        main(sc, years, months, datadir)