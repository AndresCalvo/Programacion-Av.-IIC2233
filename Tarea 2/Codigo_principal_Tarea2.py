from clase_LISTAS import *
from clase_JUGADORES import *
from clase_GRAFOS import *

data = open("players_db.csv", "r", encoding="utf8", errors="ignore")

Jugadores = ListaLigada()

data.readline(-1)
for line in data:
    Jugadores.append(Jugador(line.split(",")[0], line.split(",")[1],
                             line.split(",")[2], line.split(",")[3], line.split(",")[4], line.split(",")[5],
                             line.split(",")[6].strip("\n")))


# Unicamente alcanzo a cargar los datos al programa.
