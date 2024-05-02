from collections import Counter

# Arrays de ejemplo
array1 = [1, 2, 3, 4, 5, 1, 2, 1]
array2 = [2, 3, 4, 5, 6, 2, 3, 2]
array3 = [3, 4, 5, 6, 7, 3, 3, 3]

# Combinar todos los arrays en uno solo
todos_los_arrays = array1 + array2 + array3

# Contar la frecuencia de cada elemento en el array combinado
frecuencia = Counter(todos_los_arrays)

# Encontrar el elemento más común y su frecuencia
elemento_mas_comun, cantidad = frecuencia.most_common(1)[0]

print("El elemento más común es:", elemento_mas_comun)
print("Se repite", cantidad, "veces.")
