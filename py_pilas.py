class Pila:
    def __init__(self, tamaño=9):
        self.lista = []
        self.tope = 0
        self.size = tamaño

    def empty(self):
        return self.tope == 0

    def push(self, dato):
        if self.tope < self.size:
            self.lista += [dato]
            self.tope += 1
        else:
            print("La pila está llena.")

    def pop(self):
        if self.empty():
            return ("La lista esta vacía.")
        else:
            top = self.lista[-1]
            self.tope -= 1
            self.lista = self.lista[:-1]
            return top

    def longitud(self):
        return self.tope

    def show(self):
        if self.empty():
            print("Lista vacia")
        else:
            for tope in range(self.tope-1, -1, -1):
                print("[{}]".format(self.lista[tope]))

    def buscar(self, buscado):
        enc = False
        for pos,ele in enumerate(self.lista):
            if ele == buscado:
                enc = True
                break
        if enc == True: return pos
        else: return -1


pila = Pila(10)
pila.push("4")
pila.push("2")
pila.push("5")
pila.push("7")
pila.push("20")
pila.push("10")
pila.pop()
pila.show()
print(pila.buscar("1"))

