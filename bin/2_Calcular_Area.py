print("\033[1mCALCULAR EL ÁREA\033[0m")
import math

def case1():
    print("Seleccionó círculo\n")
    def area_circulo(radio):
        area = math.pi * radio ** 2
        return area
    radio = float(input("Ingrese el radio del círculo: ")("\n"))
    area = area_circulo(radio)
    print("El área del círculo es: %.1f\n" % area)

def case2():
    print("Seleccionó cuadrado")
    def area_cuadrado(lado):
        area = lado ** 2
        return area
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))
    area = area_cuadrado(lado)
    print("El área del cuadrado es:", area)

def case3():
    print("Seleccionó triángulo equilátero")
    def area_triangulo_equilatero(lado):
        area = (math.sqrt(3) / 4) * lado ** 2
        return area
    lado = float(input("Ingrese la longitud de un lado del triángulo equilátero: "))
    area = area_triangulo_equilatero(lado)
    print("El área del triángulo equilátero es: %.1f" % area)



opciones = {
    1: case1,
    2: case2,
    3: case3
}

while True:
    print(" ______________________________\033[1mMENU\033[0m______________________________ ")
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║   1. Círculo   ║   2. Cuadrado   ║   3. Triángulo Equilátero   ║")
    print("╚════════════════════════════════════════════════════════════════╝")

    seleccion = int(input("Seleccione una opción: "))

    if seleccion in opciones:
        opciones[seleccion]()
        if seleccion == 1:
            break
    else:
        print("Opción no válida. Inténtelo de nuevo.")
