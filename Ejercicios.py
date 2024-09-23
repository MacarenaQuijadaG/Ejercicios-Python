def menu():
    print("Seleccione un ejercicio:")
    print("1. Imprimir un mensaje")
    print("2. Sumar dos números")
    print("3. Número par o impar")
    print("4. Área de un triángulo")
    print("5. Intercambio de valores")
    print("6. Conversión de temperatura")
    print("7. Números consecutivos")
    print("8. Suma de una lista")
    print("9. Número mayor")
    print("10. Invertir una cadena")
    print("11. Contador de vocales")
    print("12. Adivina el número")
    print("13. Factorial")
    print("14. Números pares en una lista")
    print("15. Tablas de multiplicar")
    print("16. Conversión de horas a segundos")
    print("17. Suma de dígitos")
    print("18. Verificar palíndromo")
    print("19. Imprimir números impares")
    print("20. Contador de palabras")
    print("0. Salir")

    while True:
        try:
            opcion = int(input("Introduce el número del ejercicio que deseas ejecutar: "))
            if 0 <= opcion <= 20:
                return opcion
            else:
                print("Por favor, introduce un número entre 0 y 20.")
        except ValueError:
            print("Entrada no válida. Debes introducir un número entero.")

def ejecutar_ejercicio(opcion):
    if opcion == 1:
        print("Hola, Python")
    elif opcion == 2:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        print(f"La suma es: {a + b}")
    elif opcion == 3:
        num = int(input("Introduce un número: "))
        if num % 2 == 0:
            print(f"{num} es par.")
        else:
            print(f"{num} es impar.")
    elif opcion == 4:
        base = float(input("Introduce la base del triángulo: "))
        altura = float(input("Introduce la altura del triángulo: "))
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")
    elif opcion == 5:
        a = input("Introduce el valor de a: ")
        b = input("Introduce el valor de b: ")
        a, b = b, a
        print(f"Los valores intercambiados son: a = {a}, b = {b}")
    elif opcion == 6:
        celsius = float(input("Introduce la temperatura en grados Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"La temperatura en Fahrenheit es: {fahrenheit}")
    elif opcion == 7:
        for i in range(1, 11):
            print(i)
    elif opcion == 8:
        lista = [int(x) for x in input("Introduce una lista de números separados por espacios: ").split()]
        print(f"La suma de la lista es: {sum(lista)}")
    elif opcion == 9:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        c = float(input("Introduce el tercer número: "))
        mayor = max(a, b, c)
        print(f"El número mayor es: {mayor}")
    elif opcion == 10:
        cadena = input("Introduce una cadena: ")
        print(f"La cadena invertida es: {cadena[::-1]}")
    elif opcion == 11:
        cadena = input("Introduce una cadena: ")
        vocales = "aeiouAEIOU"
        contador = sum(1 for char in cadena if char in vocales)
        print(f"El número de vocales es: {contador}")
    elif opcion == 12:
        import random
        numero_aleatorio = random.randint(1, 10)
        adivinado = False
        while not adivinado:
            intento = int(input("Adivina el número entre 1 y 10: "))
            if intento == numero_aleatorio:
                print("¡Correcto!")
                adivinado = True
            else:
                print("Intenta de nuevo.")
    elif opcion == 13:
        num = int(input("Introduce un número: "))
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        print(f"El factorial de {num} es: {factorial}")
    elif opcion == 14:
        lista = [int(x) for x in input("Introduce una lista de números separados por espacios: ").split()]
        pares = [num for num in lista if num % 2 == 0]
        print(f"Los números pares son: {pares}")
    elif opcion == 15:
        num = int(input("Introduce un número: "))
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    elif opcion == 16:
        horas = int(input("Introduce la cantidad de horas: "))
        segundos = horas * 3600
        print(f"{horas} horas son {segundos} segundos.")
    elif opcion == 17:
        num = input("Introduce un número entero: ")
        suma_digitos = sum(int(digito) for digito in num)
        print(f"La suma de los dígitos es: {suma_digitos}")
    elif opcion == 18:
        cadena = input("Introduce una cadena: ")
        if cadena == cadena[::-1]:
            print(f"{cadena} es un palíndromo.")
        else:
            print(f"{cadena} no es un palíndromo.")
    elif opcion == 19:
        for i in range(1, 21, 2):
            print(i)
    elif opcion == 20:
        frase = input("Introduce una frase: ")
        palabras = frase.split()
        print(f"El número de palabras es: {len(palabras)}")
    else:
        print("Opción no válida.")

# Ejecutar el menú en un bucle
while True:
    opcion_seleccionada = menu()
    if opcion_seleccionada == 0:
        print("Saliendo del programa...")
        break
    try:
        ejecutar_ejercicio(opcion_seleccionada)
    except Exception as e:
        print(f"Ocurrió un error: {e}. Por favor intenta de nuevo.")
