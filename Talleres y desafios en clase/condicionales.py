# # Ejercicio 1: Verificar si un numero es positivo,negativo o es cero

# print("------------------ Ejercicio 1 --------------------")

# numero1 = float(input("Ingresa un numero: "))
# if numero1 > 0:
#     print(f"El numero 1 ({numero1}) es mayor que cero osea es positivo ")
# elif numero1 < 0:
#     print(f"El numero 1 ({numero1}) es menor que cero osea es negativo")
# else:
#     print(f"El numero 1 ({numero1}) es 0")

# # Ejercicio 2: Calcula el mayor de dos numeros ingresados

# print("------------------ Ejercicio 2 --------------------")

# num1 = float(input("Ingresa un numero 1: "))
# num2 = float(input("Ingresa un numero 2: "))
# if num1 > num2:
#     print(f"El numero 1 ({num1}) es mayor que el numero 2 ({num2})")
# elif num2 > num1:
#     print(f"El numero 2 ({num2}) es mayor que el numero 1 ({num1})")
# else:
#     print(f"Los numeros ({num1}), ({num2}) son iguales")

# # Ejercicio 3: Determina si un numero es par o impar

# print("------------------ Ejercicio 3 --------------------")

# num11 = float(input("Ingresa un numero 1: "))
# numero = 2
# if num11 % numero == 0:
#     print(f"El numero ({num11}) es par")
# else:
#     print(f"El numero ({num11}) no es par")


# # Ejercicio 4: Dado un numero verifica si esta entre 10 y 20

# print("------------------ Ejercicio 4 --------------------")

# num22 = float(input("Ingresa un numero: "))
# if num22 >= 10 and num22 <= 20:
#     print(f"El numero ({num22}) esta entre 10 y 20")
# else:
#     print(f"El numero ({num22}) no esta entre 10 y 20")

# # Ejercicio 5: Dados tres numeros,encuentra el mayor usando condicionales

# print("------------------ Ejercicio 5 --------------------")

# num_uno = float(input("Ingresa un primer numero: "))
# num_dos = float(input("Ingresa un segundo numero: "))
# num_tres = float(input("Ingresa un tercer numero: "))

# if num_uno > num_dos and num_uno > num_tres:
#     print(f"El numero uno ({num_uno}) es mayor que el numero dos: {num_dos} y que el numero tres: {num_tres}")
# else: 
#     print(f"El numero 1 ({num_uno}) no es mayor que el numero dos: {num_dos} y que el numero tres: {num_tres}")

# if num_dos > num_uno and num_dos > num_tres:
#     print(f"El numero 2 ({num_dos}) es mayor que el numero uno: {num_uno} y que  el numero tres: {num_tres}")
# else:
#     print(f"El numero 2 ({num_dos}) no es mayor que el numero uno: {num_uno} y que el numero tres: {num_tres}")

# if num_tres > num_dos and num_tres > num_uno:
#     print(f"El numero tres ({num_tres}) es mayor que el numero dos: {num_dos} y que el numero uno: {num_uno}")
# else:
#     print(f"El numero tres ({num_tres}) no es mayor que el numero dos: {num_dos} y que el numero uno: {num_uno}")


# Ejercicio 6: Calcula el precio final con un 10% de descuento si el total es mayor a 100$

print("------------------ Ejercicio 6 --------------------")

precio = float(input("¿A cuanto esta el precio de la papa actualmente?: "))
if precio > 100:
    prod = precio * 0.10
    preciofinal = prod - precio
    print(f"El precio final con el 10% de descuento de {precio}$ de la papa  es {prod}$")
else:
    print(f"El producto esta en menos que 100$,es un buen precio y no se le hara descuento")

# Ejercicio 7: Verifica si una persona puede votar (mayor o igual a 18 años)

print("------------------ Ejercicio 7 --------------------")

edad = int(input("Ingresa tu edad actual: "))
if edad >= 18:
    print(f"Puedes votar ya que tienes {edad} años,que bueno!")
else:
    print(f"Aun no puedes votar ya que tienes {edad} años")

# Ejercicio 8: Dado el precio y tipo de cliente (VIP o normal),aplica un descuento del 20% solo a VIP

print("------------------ Ejercicio 8 --------------------")

cliente = input("Eres un cliente VIP o Normal,se sincero y ponlo exactamente igual,el precio de la entrada es 200: ")
precio = 200
if cliente == "VIP":
    primero = precio * 0.20
    print(f"El precio final con el 20% de descuento por ser VIP es: {primero}$ teniendo en cuenta que el precio actual es: {precio}$")
else:
    print(f"No eres VIP,por lo tanto el total que debes pagar por entrar es: {precio}$")

# Ejercicio 9: Determina si un numero es multiplo de 5 y de 3 al mismo tiempo


numero = float(input("Ingresa un numero: "))
if numero % 3 == 0 and numero % 5 == 0:
    print(f"El numero {numero} si es multiplo de 5 y 3")
else: 
    print(f"El numero {numero} no es multiplo de 5 y 3")

# Ejercicio 10: Dado un numero,verifica si es divisibe entre dos numeros dados 

numerouno = float(input("Ingresa un primer numero: "))
numerodos = float(input("Ingresa un numero por el cual creas que es divisible: "))
numerotres = float(input("Ingresa un numero por el cual creas que es divisible: "))

if numerouno % numerodos and numerouno % numerotres == 0:
    print(f"El numero {numerouno} es divisible por el {numerodos} y por el {numerotres}")
else:
    print(f"El numero {numerouno} no es divisible por el {numerodos} y por el {numerotres}")

if numerodos % numerouno and numerodos % numerotres == 0:
    print(f"El numero {numerodos} es divisible por {numerouno} y por el {numerotres}")
else:
    print(f"El numero {numerodos} no es divisible por {numerouno} y por el {numerotres}")

if numerotres % numerouno and numerotres % numerodos == 0:
    print(f"El numero {numerotres} es divisible por el numero {numerouno} y por el {numerodos}")
else:
    print(f"El numero {numerotres} no es divisible por el numero {numerouno} ni por el numero {numerodos}")
    

