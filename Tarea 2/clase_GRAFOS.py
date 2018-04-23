from clase_LISTAS import *
from clase_JUGADORES import *

data = open("players_db_chica.csv", "r", encoding="utf8", errors="ignore")


class NodoGr:
    def __init__(self, jugador):
        self.jugador = jugador
        self.conecciones = ListaLigada()

    def __repr__(self):
        rep = ""
        rep += "{}".format(self.jugador)
        # rep += "Conecciones: {} \n".format(self.conecciones)
        return rep

    def encontrar_conecciones(self):
        for persona1 in self.jugador.amigos_cercanos:
            if persona1 not in self.conecciones:
                self.conecciones.append(NodoGr(persona1))
        for persona2 in self.jugador.amigos_lejanos:
            if persona2 not in self.conecciones:
                self.conecciones.append(NodoGr(persona2))
        for persona3 in self.jugador.conocidos:
            if persona3 not in self.conecciones:
                self.conecciones.append(NodoGr(persona3))


# No pude lograr que funcionara correctamente
def encontrar_camino(inicio, final, camino=ListaLigada()):
    camino.append(inicio)
    print("Es verdad: {}".format(inicio == final))
    if inicio == final:
        return camino
    if len(inicio.conecciones) == 0:
        return None
    for nodo in inicio.conecciones:
        if nodo not in camino:
            camino_nuevo = encontrar_camino(nodo, final, camino)
            if camino_nuevo:
                return camino_nuevo
    if len(camino) == 0:
        print("No hay camino")
        return None
    else:
        return camino


# Por consecuencia de lo anterior, tampoco logré hacer que esta funcionara correctamente
def encontrar_all_caminos(inicio, final,
                          camino=ListaLigada()):
    camino.append(inicio)
    print("Es verdad: {}".format(inicio == final), type(inicio))
    if inicio == final:
        return camino
    if len(inicio.conecciones) == 0:
        return None
    caminos = ListaLigada()
    for nodo in inicio.conecciones:
        if nodo not in camino:
            camino_nuevo = encontrar_camino(nodo, final, camino)
            if camino_nuevo:
                caminos.append(camino_nuevo)
        return camino
