print("\033[1mCARGA DE ARTÍCULOS\033[0m")   # Título.

articulos = []  # Lista para almacenar los artículos.

# Opción 1, cargar datos.
def ingresar(): 
    print("\n■ \033[1mCARGA DE ARTÍCULOS\033[0m")  # Título.

    for i in range(3):  # Iterar tres veces para tres artículos (o los que se especifique).
        articulo = [None] * 4  # Inicializar un nuevo artículo con 4 elementos vacíos.

        # Cargar datos requeridos para el artículo actual.
        articulo[0] = str(input("\n● Proporcione el código del artículo: "))
        articulo[1] = int(input("● Proporcione la cantidad vendida: "))
        articulo[2] = str(input("● Proporcione el tipo de artículo: "))
        articulo[3] = float(input("● Proporcione el precio del artículo: "))
        
        articulos.append(articulo)  # Agrega el artículo ingresado a la lista artículos.

        continuar = input("¿Desea continuar ingresando datos? (S/N): ")
        if continuar.lower() != 's':
            break  # Salir del bucle si la respuesta es "n".

# Opción 2, ver datos cargados.
def cargados():
    print("\n■ \033[1mARTÍCULOS CARGADOS\033[0m")  # Título.

    # Verificar si hay datos cargados.
    if not articulos:
        print("\nNo hay artículos cargados.\n")
        return  # Salir de la función si no hay datos cargados.
    
    for idx, articulo in enumerate(articulos, start=1): # Imprimir los datos de todos los artículos.
        print("\n"f"● \033[4mArtículo {idx}\033[0m:")
        print("     ╠○ Código:", articulo[0])
        print("     ╠○ Cantidad vendida:", articulo[1])
        print("     ╠○ Tipo:", articulo[2])
        print(f"     ╚○ Precio unitario: ${articulo[3]:.2f}")

    while True:
        atrás = input("\n(1) Volver al menú: ")
        if atrás == '1':
            break  # Salir del bucle si se ingresa "1".
        else:
            print("\nOpción no válida, inténtelo de nuevo.")
            continue  # Continuar pidiendo la entrada del usuario si no se ingresa el "1".

# Opción 3, mostrar un resumen de los artículos cargados con las operaciones correspondientes realizadas.
def resumen():
    print("\n■ \033[1mRESUMEN\033[0m") # Título.

    # Verificar si hay datos cargados.
    if not articulos:
        print("\nNo hay artículos cargados.\n")
        return  # Salir de la función si no hay datos cargados.

    # Diccionario para almacenar la cantidad vendida, importe total y promedio por tipo de producto.
    tipos_vendidos = {}

    # Calcular la cantidad vendida, importe total y promedio por tipo de producto.
    for articulo in articulos:
        tipo = articulo[2]
        cantidad = articulo[1]
        precio = articulo[3]

        # Calcular el importe total para este artículo.
        importe_total = cantidad * precio

        # Actualizar el diccionario de tipos_vendidos.
        tipos_vendidos[tipo] = tipos_vendidos.get(tipo, {'Cantidad Vendida': 0, 'Importe Total': 0, 'Importe Promedio': 0})
        tipos_vendidos[tipo]['Cantidad Vendida'] += cantidad
        tipos_vendidos[tipo]['Importe Total'] += importe_total
        tipos_vendidos[tipo]['Importe Promedio'] = tipos_vendidos[tipo]['Importe Total'] / tipos_vendidos[tipo]['Cantidad Vendida']

        # Calcular el nuevo precio si el importe del artículo supera al promedio en $400.
        if importe_total > tipos_vendidos[tipo]['Importe Promedio'] + 400:
            aumento = precio * 0.07
            nuevo_precio = precio + aumento
            print(f"\n● El importe del artículo '{tipo}' supera al promedio en $400.")
            print(f"  Se aplicará un aumento del 7% en el precio unitario.")
            print(f"  Nuevo precio unitario: ${nuevo_precio:.2f}")

    # Encontrar el tipo de producto más vendido.
    tipo_mas_vendido = max(tipos_vendidos, key=lambda x: tipos_vendidos[x]['Cantidad Vendida'])
    cantidad_mas_vendida = tipos_vendidos[tipo_mas_vendido]['Cantidad Vendida']

    # Imprimir el tipo de producto más vendido.
    print(f"\n● El tipo de producto más vendido es: {tipo_mas_vendido}, con {cantidad_mas_vendida} unidades vendidas.")

    # Imprimir el importe total y el importe promedio vendido por cada tipo de artículo.
    print("\n● Resumen por tipo de artículo:")
    for tipo, info in tipos_vendidos.items():
        print(f"\n  ▹ Tipo de artículo: {tipo}")
        print(f"  ▹ Cantidad Vendida: {info['Cantidad Vendida']}")
        print(f"  ▹ Importe Total: ${info['Importe Total']:.2f}")
        print(f"  ▹ Importe Promedio: ${info['Importe Promedio']:.2f}")

    while True:
        atrás = input("\n(1) Volver al menú: ")
        if atrás == '1':
            break  # Salir del bucle si se ingresa "1".
        else:
            print("\nOpción no válida, inténtelo de nuevo.")
            continue  # Continuar pidiendo la entrada del usuario.

# Opción 4, termina el programa.
def salir():
    print("\nSaliendo del programa...\n")
    exit()

# Opciones a elegir en el menú.
opciones={
    1:ingresar, 2:cargados, 3:resumen, 4:salir
}

# Imprimir menú en pantalla.
while True:
    print("\n ____________________________________________\033[1m\033[4mMENU\033[0m"
          "____________________________________________ ")
    print("╔════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║   (1) Cargar artículo   ║   (2) Ver artículos cargados   ║   (3) Resumen   ║   (4) Salir   ║")
    print("╚════════════════════════════════════════════════════════════════════════════════════════════╝")

    # Lógica de los botonoes del menú.
    seleccion = int(input("Seleccione una opción: "))

    if seleccion in opciones:
        opciones[seleccion]()   # Si se selecciona un número de las opciones se redirige a la función.
    else:
        print("\nOpción no válida, inténtelo de nuevo.\n")
        continue    # Si no se encuentra el número repite el menú.