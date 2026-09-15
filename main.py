import csv

filename = "teams.csv"

with open(filename) as file:
    count_lines = 1
    for line in file:
        if count_lines == 1:
            #si copunt_lines es 1, significa que estamos en la primera fila, es decir, el header
            header = line.split(',')
        else:
            #en cualquier otro caso, estamos en un equipo
            team = line.split(',')
            for i in range(len(team)):
                print(f"{header[i]}: {team[i]}")



        count_lines += 1
        