from clase_LISTAS import *


class Jugador:
    def __init__(self, id, alias, nombre, club, liga, nacionalidad, overall):
        self.id = str(id)
        self.nombre = str(nombre)
        self.alias = str(alias)
        self.club = str(club)
        self.liga = str(liga)
        self.nacionalidad = nacionalidad
        self.overall = int(overall)
        self.amigos_cercanos = ListaLigada()
        self.amigos_lejanos = ListaLigada()
        self.conocidos = ListaLigada()

        # def __repr__(self):
        # rep2 = "+++++++++++++ \n"
        # rep2 += "ID : {} \n".format(self.id)
        # rep2 += "Nombre : {} \n".format(self.nombre)
        # rep2 += "Alias : {} \n".format(self.alias)
        # rep2 += "Nacionalidad : {} \n".format(self.nacionalidad)
        # rep2 += "liga : {} \n".format(self.liga)
        # rep2 += "club : {} \n".format(self.club)
        # rep2 += "Overall : {} \n".format(self.overall)
        # rep2 += "++++++++++++"
        # return rep2

    def __repr__(self):
        rep2 = "Nombre : {} ".format(self.nombre)

        return rep2

    def comparar_afinidad(self, jugador):
        if jugador not in self.amigos_cercanos:
            if (self.nacionalidad == jugador.nacionalidad) and (self.club == jugador.club):
                self.amigos_cercanos.append(jugador)
                if self not in jugador.amigos_cercanos:
                    jugador.amigos_cercanos.append(self)
            elif jugador not in self.amigos_lejanos:
                if (self.nacionalidad == jugador.nacionalidad) and (self.liga == jugador.liga):
                    self.amigos_lejanos.append(jugador)
                    if self not in jugador.amigos_lejanos:
                        jugador.amigos_lejanos.append(self)
                elif jugador not in self.conocidos:
                    if (self.nacionalidad == jugador.nacionalidad) or (self.club == jugador.club) or (
                            (self.liga == jugador.liga)
                    ):
                        self.conocidos.append(jugador)
                        if self not in jugador.conocidos:
                            jugador.conocidos.append(self)


Mario = Jugador(108, "Crack", "Mario", "c1", "l1", "n1", 99)
Toni = Jugador(17, "Tigre", "Toni", "c2", "l2", "n1", 87)
Franco = Jugador(190, "Tucan", "Franco", "c2", "l3", "n2", 76)
Tomas = Jugador(756, "Bufanda", "Tomas", "c3", "l4", "n2", 56)
