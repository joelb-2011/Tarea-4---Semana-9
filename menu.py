import os
from py_listas import Lista
from py_pilas import Pila
from py_cola import Cola

class Menu:
    def __init__(self, titulo, opciones=[]):
        self.titulo = titulo
        self.opciones = opciones
        
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija una opción [1...{}]:".format(len(self.opciones)))
        return opc

opc = ""
while opc != "4":
    os.system("cls")
    men = Menu("Menu Principal", ["1) Listas", "2) Pilas", "3) Colas", "4) Salir"])
    opc = men.menu()
    if opc == "1":
        opc1 = ""
        lista1 = Lista()
        while opc1 != "7":
            os.system("cls")
            men1 = Menu("Menu Listas", ["1) Push", "2) Pop", "3) Show", "4) Eliminar", "5) Insertar", "6) Buscar", "7) Salir"])
            opc1 = men1.menu()
            os.system("cls")

            if opc1 == "1":
                print("Push")
                dato = input("Inserte un dato a la lista: ")
                lista1.push(dato)
                print(lista1.lista)
                input("Presione cualquier tecla para continuar.")

            elif opc1 == "2":
                print("Pop")
                dato = lista1.pop()
                if dato: print("El dato eliminado es: {}".format(dato))
                else: print("La lista esta vacía.")
                input("Presione cualquier tecla para continuar.")

            elif opc1 == "3":
                print("Show")
                lista1.mostrar()
                input("Presione cualquier tecla para continuar.")

            elif opc1 == "4":
                print("Eliminar Elemento")
                dato = int(input("Inserte la posición del valor que va a eliminar: "))
                lista1.eliminarElemento(dato)
                print(lista1.lista)
                input("Presione cualquier tecla para continuar.")

            elif opc1 == "5":
                print("Insertar Elemento")
                pos = int(input(("Inserte la posición en la que desea agregarle el valor: ")))
                valor = int(input("Inserte el dato a insertar en la lista: "))
                lista1.insertarElemento(pos, valor)
                print(lista1.lista)
                input("Presione cualquier tecla para continuar.")

            elif opc1 == "6":
                print("Buscar")
                dato = input("Inserte el dato a buscar: ")
                print(lista1.buscar(dato))
                input("Presione cualquier tecla para continuar.")

    elif opc == "2":
        opc2 = ""
        pila1 = Pila()
        while opc2 != "6":
            os.system("cls")
            men2 = Menu("Menu Pilas", ["1) Push", "2) Pop", "3) Show", "4) Buscar", "5) Longitud", "6) Salir"])
            opc2 = men2.menu()
            os.system("cls")

            if opc2 == "1":
                print("Push")
                dato = input("Inserte un dato a la pila: ")
                pila1.push(dato)
                print(pila1.lista)
                input("Presione cualquier tecla para continuar.")

            elif opc2 == "2":
                print("Pop")
                dato = pila1.pop()
                if dato: print("El dato eliminado es: {}".format(dato))
                else: print("La pila esta vacía.")
                input("Presione cualquier tecla para continuar.")

            elif opc2 == "3":
                print("Show")
                print(pila1.show())
                input("Presione cualquier tecla para continuar.")

            elif opc2 == "4":
                print("Buscar")
                buscar = input("Inserte el valor a buscar: ")
                print(pila1.buscar(buscar))
                input("Presione cualquier tecla para continuar.")

            elif opc2 == "5":
                print("Longitud")
                print(pila1.longitud())
                input("Presione cualquier tecla para continuar.")

    elif opc == "3":
        opc3 = ""
        cola1 = Cola()
        while opc3 != "6":
            os.system("cls")
            men3 = Menu("Menu Colas", ["1) Push", "2) Pop", "3) Show", "4) Buscar", "5) Longitud", "6) Salir"])
            opc3 = men3.menu()
            os.system("cls")

            if opc3 == "1":
                print("Push")
                dato = input("Inserte el dato a encolar: ")
                cola1.push(dato)
                print(cola1.cola)
                input("Presione cualquier tecla para continuar.")

            elif opc3 == "2":
                print("Pop")
                dato = cola1.pop()
                if dato: print("El dato eliminado es: {}".format(dato))
                else: print("La cola esta vacía.")
                input("Presione cualquier tecla para continuar.")

            elif opc3 == "3":
                print("Show")
                cola1.show
                input("Presione cualquier tecla para continuar.")

            elif opc3 == "4":
                print("Buscar")
                buscar = input("Ingresar el valor a buscar: ")
                print(cola1.buscar(buscar))
                input("Presione cualquier tecla para continuar.")

            elif opc3 == "5":
                print("Longitud")
                print(cola1.longitud())
                input("Presione cualquier tecla para continuar.")

    elif opc == "4":
            print("Muchas gracias por usar nuestro sistema.")
    else:
            print("Opción incorrecta.")

print("■"*20, "Nos vemos pronto, ¡Que tenga un buen día!", "■"*20)
print("■"*66)
