import csv
with open("data.csv") as fh:
    for row in csv.reader(fh):
        Duration,Average_Pulse,Max_Pulse,Calorie_Burnage,Hours_Work,Hours_Sleep = row
        print(Duration,Average_Pulse,Max_Pulse,Calorie_Burnage,Hours_Work,Hours_Sleep)