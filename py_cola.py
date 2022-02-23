class Cola:
    def __init__(self, tamaño=9):
        self.cola = []
        self.tope = 0
        self.size = tamaño

    def empty(self):
        return self.tope == 0

    def push(self, dato):
        self.cola.append(dato)
        self.tope += 1

    def pop(self):
        if self.empty():
            return("La cola se encuentra vacía.")
        else:
            return self.cola.pop(0)

    def show(self):
        for top in range(self.tope):
            print("[{}]".format(self.cola[top]))

    def buscar(self, buscado):
        enc = False
        for pos,ele in enumerate(self.cola):
            if ele == buscado:
                enc = True
                break
        if enc == True: return pos
        else: return -1

    def longitud(self):
        return self.tope

cola1 = Cola(10)
cola1.push("5")
cola1.push("6")
cola1.push("8")
cola1.push("10")
cola1.show()
print(cola1.buscar("6"))
print(cola1.longitud())
