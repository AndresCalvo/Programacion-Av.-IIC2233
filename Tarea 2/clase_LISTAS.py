# Codigo sacado de la clase de semana 04: Listas ligadas, arboles y grafos
class Nodo:  # con algunas modificaciones y funciones extras
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None

    def __repr__(self):
        return "{}".format(self.valor)


class Iterador:
    def __init__(self, nodo):
        self.actual = nodo

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration()

        res = self.actual.valor
        self.actual = self.actual.siguiente
        return res


class ListaLigada:
    def __init__(self, *valores):
        self.cabeza = None
        self.cola = None
        for valor in valores:
            self.append(valor)

    def append(self, valor):  # Inicializamos el nuevo nodo
        nuevo = Nodo(valor)
        if not self.cabeza:  # Si la lista está vacía (no hay cabeza)
            self.cabeza = nuevo
            self.cola = self.cabeza
        else:
            # Agregamos el nuevo nodo como sucesor del nodo cola actual,
            # y actualizamos la referencia al nodo cola.
            # Debemos hacerlo en este orden.
            self.cola.siguiente = nuevo
            self.cola = self.cola.siguiente

    def __iter__(self):
        return Iterador(self.cabeza)

    def __len__(self):  # longitud de la lista
        n = 0
        nodo_actual = self.cabeza
        while nodo_actual:
            n += 1
            nodo_actual = nodo_actual.siguiente
        return n

    def __getitem__(self, posicion):  # Entrega el valor del nodo en la posicion dada
        # Empezamos en la cabeza
        nodo_actual = self.cabeza
        # Recorremos secuencialmente la lista ligada siguiendo los punteros
        # al nodo siguiente.
        for i in range(posicion):
            if nodo_actual:
                nodo_actual = nodo_actual.siguiente
        # Si buscamos una posición mayor a la longitud de la lista ligada
        if not nodo_actual:
            raise IndexError("Posición no encontrada")
        else:
            return nodo_actual.valor

    def __setitem__(self, posicion, valor):  # Modifica el valor de un nodo cualquiera
        if posicion == 0:
            self.cabeza.valor = valor
        else:
            nodo_actual = self.cabeza
            lista_nueva = ListaLigada()
            for i in range(len(self)):
                if nodo_actual:
                    if i == posicion:
                        lista_nueva.append(valor)
                        nodo_actual = nodo_actual.siguiente
                    else:
                        lista_nueva.append(nodo_actual.valor)
                        nodo_actual = nodo_actual.siguiente
            self.cabeza = lista_nueva.cabeza

    def insertar(self, posicion, valor):
        nodo_nuevo = Nodo(valor)
        nodo_actual = self.cabeza

        if posicion == 0:
            nodo_nuevo.siguiente = self.cabeza
            self.cabeza = nodo_nuevo
            if nodo_nuevo.siguiente == None:
                self.cola = nodo_nuevo
        else:
            for i in range(posicion - 1):
                if nodo_actual:
                    nodo_actual = nodo_actual.siguiente
            if nodo_actual != None:
                nodo_nuevo.siguiente = nodo_actual.siguiente
                nodo_actual.siguiente = nodo_nuevo
                if nodo_nuevo.siguiente == None:
                    self.cola = nodo_nuevo

    def __repr__(self):  # para representar la lista, imita la de una lista estandar de Python
        rep = '['
        nodo_actual = self.cabeza

        while nodo_actual:
            rep += '{}'.format(nodo_actual.valor)
            if nodo_actual.siguiente:
                rep += ', '

            nodo_actual = nodo_actual.siguiente

        rep += ']'
        return rep
