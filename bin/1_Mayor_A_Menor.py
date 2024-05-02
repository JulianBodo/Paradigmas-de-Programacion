print("Ingrese tres numeros: ")
num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Tercer número: "))

numbers = [0, 0, 0]

if num1 >= num2 and num1 >= num3:
    numbers[0] = num1
    if num2 >= num3:
        numbers[1] = num2
        numbers[2] = num3
    else:
        numbers[1] = num3
        numbers[2] = num2
elif num2 >= num1 and num2 >= num3:
    numbers[0] = num2
    if num1 >= num3:
        numbers[1] = num1
        numbers[2] = num3
    else:
        numbers[1] = num3
        numbers[2] = num1
elif num3 >= num1 and num3 >= num2:
    numbers[0] = num3
    if num2 >= num1:
        numbers[1] = num2
        numbers[2] = num1
    else:
        numbers[1] = num1
        numbers[2] = num2

print(numbers)
