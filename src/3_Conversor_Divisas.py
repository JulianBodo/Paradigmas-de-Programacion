import conversor

print("\033[1mCONVERSOR DE DIVISAS\033[0m")

def getValue(amount, from_currency, to_currency):
    return conversor.convert_currency(amount, from_currency, to_currency)

def case1():
    monto=input("Ingrese el monto en pesos a convertir en dólares: ")
    getValue(monto, "ARS","USD" )
    
def case2():
    monto=input("Ingrese el monto en pesos a convertir en dólares: ")

opciones={
    1: case1, 2:case2
}

while True:
    print("\n _____________\033[1mMENU\033[0m______________ ")
    print("╔═══════════════════════════════╗")
    print("║   1. Dólares   ║   2. Euros   ║")
    print("╚═══════════════════════════════╝")

    seleccion=int(input("Convertir pesos a: "))

    if seleccion in opciones:
        opciones[seleccion]()
    else:
        print("\nOpción no válida. Inténtelo de nuevo.\n")
        continue