def main():
    # Inicializar variables para almacenar las ventas por tipo de producto y el promedio de ventas por artículo
    ventas_tipo = {'A': 0, 'B': 0, 'C': 0}
    cantidad_articulos = {'A': 0, 'B': 0, 'C': 0}
    total_importe = {'A': 0, 'B': 0, 'C': 0}
    precio_articulos = {'A': 0, 'B': 0, 'C': 0}

    # Variables para calcular el promedio de ventas por artículo
    total_ventas = 0
    total_articulos = 0

    # Ciclo para ingresar los datos de ventas
    while True:
        codigo = input("Ingrese el código del artículo (-1 para terminar): ")
        if codigo == '-1':
            break

        cantidad = int(input("Ingrese la cantidad vendida: "))
        tipo = input("Ingrese el tipo de producto (A, B o C): ").upper()
        precio = float(input("Ingrese el precio del artículo: "))

        # Actualizar las ventas por tipo de producto
        ventas_tipo[tipo] += cantidad

        # Actualizar el total de ventas y el total de artículos
        total_ventas += cantidad * precio
        total_articulos += cantidad

        # Actualizar la cantidad de artículos vendidos por tipo
        cantidad_articulos[tipo] += cantidad

        # Actualizar el importe total vendido por tipo de artículo
        total_importe[tipo] += cantidad * precio

        # Almacenar el precio del artículo
        precio_articulos[tipo] = precio

    # Calcular el tipo de producto más vendido
    tipo_mas_vendido = max(ventas_tipo, key=ventas_tipo.get)

    # Mostrar el tipo de producto más vendido
    print(f"El tipo de producto más vendido es: {tipo_mas_vendido}")

    # Mostrar el importe total vendido por cada tipo de artículo
    for tipo, importe in total_importe.items():
        print(f"Importe total vendido para el tipo {tipo}: {importe:.2f}")

    # Calcular y mostrar el importe promedio de venta por cada artículo
    for tipo, cantidad in cantidad_articulos.items():
        if cantidad != 0:
            promedio = total_importe[tipo] / cantidad
            print(f"Importe promedio de venta para el tipo {tipo}: {promedio:.2f}")

    # Calcular y mostrar el nuevo precio para los artículos que superan el promedio en $400
    for tipo, precio in precio_articulos.items():
        if total_importe[tipo] / cantidad_articulos[tipo] > 400:
            nuevo_precio = precio * 1.07
            print(f"Nuevo precio para el artículo de tipo {tipo}: {nuevo_precio:.2f}")

if __name__ == "__main__":
    main()
