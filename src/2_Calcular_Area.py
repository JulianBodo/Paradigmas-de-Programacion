print("\033[1mCALCULAR EL ÁREA\033[0m")
import math

def case1():
    print("\nSeleccionó círculo\n")
    def area_circulo(radio):
        area = math.pi * radio ** 2
        return area
    radio = float(input("Ingrese el radio del círculo: "))
    area = area_circulo(radio)
    print("\nEl área del círculo es: %.1f\n"%area, 
          "\n══════════════════════════════════════════════════════════════════")

def case2():
    print("\nSeleccionó cuadrado\n")
    def area_cuadrado(lado):
        area = lado ** 2
        return area
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))
    area = area_cuadrado(lado)
    print("\nEl área del cuadrado es: %.1f\n"%area,
          "\n══════════════════════════════════════════════════════════════════")

def case3():
    print("\nSeleccionó triángulo equilátero\n")
    def area_triangulo_equilatero(lado):
        area = (math.sqrt(3) / 4) * lado ** 2
        return area
    lado = float(input("Ingrese la longitud de un lado del triángulo equilátero: "))
    area = area_triangulo_equilatero(lado)
    print("\nEl área del triángulo equilátero es: %.1f\n"%area,
          "\n══════════════════════════════════════════════════════════════════")


opciones = {
    1: case1,
    2: case2,
    3: case3
}

while True:
    print("\n ______________________________\033[1mMENU\033[0m______________________________ ")
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║   1. Círculo   ║   2. Cuadrado   ║   3. Triángulo Equilátero   ║")
    print("╚════════════════════════════════════════════════════════════════╝")

    seleccion = int(input("Seleccione una opción: "))

    if seleccion in opciones:
        opciones[seleccion]()
    else:
        print("\nOpción no válida. Inténtelo de nuevo.\n")
        continue

    print("\n¿Desea realizar otro cálculo (1) o salir del programa (2)?")
        
    seleccion2 = int(input("\nSeleccione una opción: "))
        
    if seleccion2 == 2:
        print("\nSaliendo del programa.")
        break