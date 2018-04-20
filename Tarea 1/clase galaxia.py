class Galaxia:
    _g_id=100000
    def __init__(self):
        self._id = Galaxia._g_id
        self.planetas =[]
        Galaxia._g_id += 1

    def modificar_galaxia(self, planeta):
        if planeta not in self.planetas:
            print("Ese planeta no se encuentra en esta galaxia")
        else:
            i = int(input("¿Que atributo deseas modificar? Introduzca el numero asociado: "))
            print("0 : Tasa de minerales")
            print("1 : Tasa de deuterio")
            print("2 : Cantidad de soldados")
            print("3 : Cantidad de magos")
            print("4 : Crear planeta")
            print("5 : Eliminar planeta")

            if i == 0:
                n = int(input("Introduzca el nuevo valor para la tasa de minerales: "))
                while n < 1 or n > 10:
                    print("Ese valor no es valido.")
                    n = int(input("Introduzca el nuevo valor para la tasa de minerales: "))




