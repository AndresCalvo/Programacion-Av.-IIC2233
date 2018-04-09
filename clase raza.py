import random

class Raza:
    def __init__(self, p, c_s, c_m, a_s, a_m, v_s, v_m, grito):
        self.poblacion_maxima = p
        self.min_costo_soldado = int(c_s[0])
        self.min_costo_mago = int(c_m[0])
        self.deu_costo_soldado = int(c_s[1])
        self.deu_costo_mago = int(c_m[1])
        self.ataque_soldado = a_s
        self.ataque_mago = a_m
        self.vida_soldado = v_s
        self.vida_mago = v_m
        self.grito = grito








Maestro = Raza(100, [200, 100], [300, 400], random.randint(60,80), random.randint(80,120), random.randint(200,250), random.randint(150,200), "¡Nuestro conocimiento nos ha otorgado una victoria mas!")

Aprendiz = Raza(150, [300, 400], [0, 0], random.randint(60,80), 0, random.randint(600, 700), 0, "Con una gran defensa y medicinas, nuestros soldados son invencibles!")

Asesino = Raza(400, [100, 200], [0, 0], random.randint(40, 45), 0, random.randint(250, 270), 0, "¡El poder de las sombras es lo unico necesario para ganar estas batallas!")


