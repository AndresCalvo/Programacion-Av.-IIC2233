import random
import time
class Planeta:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
        self.soldados_actuales = 0
        self.magos_actuales = 0
        self.poblacion_maxima = 0
        self.m_por_segundo = random.uniform(1,10)
        self.d_por_segundo = random.uniform(5,15)
        self.ponderador_ataque = 1
        self.ponderador_economia = 1
        self.conquistado = False
        self.edificio1 = False
        self.edificio2 = False
        self.evolucion = 0
        self.ultima_recoleccion = time.time()

        @property
        def minerales(self, m):
            return self.m_por_segundo

        @minerales.setter
        def minerales(self, m):
            if p < 1:
                print("No sirve")
            if p > 10:
                print("No sirve")
            else:
                self.m_por_segundo = m


