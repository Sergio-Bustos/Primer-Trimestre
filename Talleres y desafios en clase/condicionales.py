# Ejercicios de condicionales en clase

print("--- Ejercicios de condicionales en clase ---")

# Ejercicio 1: Verificar si un numero es positivo,negativo o es cero

print("------------------ Ejercicio 1 --------------------")

numero1 = float(input("Ingresa un numero: "))
if numero1 > 0:
    print(f"El numero 1 ({numero1}) es mayor que cero osea es positivo ")
elif numero1 < 0:
    print(f"El numero 1 ({numero1}) es menor que cero osea es negativo")
else:
    print(f"El numero 1 ({numero1}) es 0")

# Ejercicio 2: Calcula el mayor de dos numeros ingresados

print("------------------ Ejercicio 2 --------------------")

num1 = float(input("Ingresa un numero 1: "))
num2 = float(input("Ingresa un numero 2: "))
if num1 > num2:
    print(f"El numero 1 ({num1}) es mayor que el numero 2 ({num2})")
elif num2 > num1:
    print(f"El numero 2 ({num2}) es mayor que el numero 1 ({num1})")
else:
    print(f"Los numeros ({num1}), ({num2}) son iguales")

# Ejercicio 3: Determina si un numero es par o impar

print("------------------ Ejercicio 3 --------------------")

num11 = float(input("Ingresa un numero 1: "))
numero = 2
if num11 % numero == 0:
    print(f"El numero ({num11}) es par")
else:
    print(f"El numero ({num11}) no es par")


# Ejercicio 4: Dado un numero verifica si esta entre 10 y 20

print("------------------ Ejercicio 4 --------------------")

num22 = float(input("Ingresa un numero: "))
if num22 >= 10 and num22 <= 20:
    print(f"El numero ({num22}) esta entre 10 y 20")
else:
    print(f"El numero ({num22}) no esta entre 10 y 20")

# Ejercicio 5: Dados tres numeros,encuentra el mayor usando condicionales

print("------------------ Ejercicio 5 --------------------")

num_uno = float(input("Ingresa un primer numero no puede ser igual al otro: "))
num_dos = float(input("Ingresa un segundo numero no puede ser igual al otro: "))
num_tres = float(input("Ingresa un tercer numero no puede ser igual al otro: "))

if num_uno > num_dos and num_uno > num_tres:
    print(f"El número mayor es: {num_uno}")
elif num_dos > num_uno and num_dos > num_tres:
    print(f"El número mayor es: {num2}")
elif num_tres > num_uno and num_tres > num2:
    print(f"El número mayor es: {num_tres}")
else:
    print("Hay al menos dos números iguales")

# Ejercicio 6: Calcula el precio final con un 10% de descuento si el total es mayor a 100$

print("------------------ Ejercicio 6 --------------------")

precio = float(input("¿A cuanto esta el precio de la papa actualmente?: "))
if precio > 100:
    prod = precio * 0.10
    preciofinal = precio - prod
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
    segundo = precio - primero
    print(f"El precio final con el 20% de descuento por ser VIP es: {segundo}$ teniendo en cuenta que el precio actual es: {precio}$")
else:
    print(f"No eres VIP,por lo tanto el total que debes pagar por entrar es: {precio}$")

# # Ejercicio 9: Determina si un numero es multiplo de 5 y de 3 al mismo tiempo

print("------------------ Ejercicio 9 --------------------")

numero = float(input("Ingresa un numero el cual creas que es multiplo de 5 y 3 al mismo tiempo: "))
if numero % 3 == 0 and numero % 5 == 0:
    print(f"El numero {numero} si es multiplo de 5 y 3")
else: 
    print(f"El numero {numero} no es multiplo de 5 y 3")

# Ejercicio 10: Dado un numero,verifica si es divisibe entre dos numeros dados 

print("------------------ Ejercicio 10 --------------------")

numero = int(input("Ingresa el número principal: "))
div1 = int(input("Ingresa el primer divisor: "))
div2 = int(input("Ingresa el segundo divisor: "))

if numero % div1 == 0 and numero % div2 == 0:
    print(f"{numero} es divisible entre {div1} y {div2}")
elif numero % div1 == 0:
    print(f"{numero} solo es divisible entre {div1}")
elif numero % div2 == 0:
    print(f"{numero} solo es divisible entre {div2}")
else:
    print(f"{numero} no es divisible entre ninguno de los dos")


# Taller de condicionales en clase

print("---- Taller numero 3: Condicionales en clase ------")

# 1 - Pide tu edad y muestra si eres menor de edad,mayor de edad o adulto mayor (65+)

print("------Ejercicio 1 ------")

edadd = int(input("Ingresa tu edad: "))

if edadd < 18:
    print(f"Eres menor de edad por que tienes menos de 18 años")
elif edadd < 65:
    print(f"Eres mayor de edad por que tienes mas de 18 años,felicidades! :)")
else:
    print(f"Eres un adulto mayor,estas ya viejo por que tienes mas de 65 años :(")

# 2 -  Solicita tu estatura en metros. Si mide menos de 1.5 m, eres considerado bajo; entre 1.5 y 1.8 m, estatura media; más de 1.8 m, alto

print("------Ejercicio 2 ------")

estatura = float(input("Ingresa tu estatura actual por favor: "))
if estatura < 1.5:
    print(f"Eres bajo,lo sentimos,en un años crecerás! :)")
elif estatura >= 1.5  and estatura <= 1.8:
    print(f"Eres considera con una estatura media,felicidades estas en una altura promedia! :)")
else:
    print(f"Eres considera alto,felicitaciones! :)")

# 3 - Ingresa un número y muestra si es múltiplo de 2, de 3, o de ninguno.

print("------Ejercicio 3 ------")

numero = int(input("Ingresa un numero por el cual creas que es multiplo de 2 y 3: "))


if numero % 2 == 0 and numero % 3 == 0:
    print(f"El numero {numero} si es multiplo de 3 y de 2")
elif numero % 2 == 0:
    print(f"El numero {numero} solo es multiplo de 2")
elif numero % 3 == 0:
    print(f"El numero {numero} solo es multiplo de 3")
else:
    print(f"El numero {numero} no es multiplo ni de 3 ni de 2")

# 4 -Pide un número decimal y determina si tiene 1, 2 o más de 2 decimales (usa str() y split()).

print("------Ejercicio 4 ------")

numero = input("Ingresa un número: ")
if '.' in numero:
    decimales = numero.split('.')[1]
    if len(decimales) == 1:
        print("El numero tiene 1 decimal")
    elif len(decimales) > 2:
        print("El numero tiene más de 2 decimales")
    else:
        print("El numero tiene 2 decimales")
else:
    print("No tiene decimales")

# 5 - Solicita un país y muestra si está en la siguiente tupla: ("Colombia", "Perú", "Argentina", "México").

print("------Ejercicio 5 ------")

tupla = ("Colombia","Peru","Argentina","Mexico")
pais = input("Ingresa el pais en el que vives,empiezalo por mayuscula por favor: ")
if pais in tupla:
    print(f"{pais} si esta en la tupla {tupla}")
else: 
    print(f"{pais} no esta en la tupla {tupla}")

# 6 - Pide tu tipo de sangre (A, B, AB, O) y muestra tu compatibilidad según un diccionario predefinido.

print("------Ejercicio 6 ------")

compatibilidad = {
    "O": "Puede donar a todos (O, A, B, AB). Solo recibe de O.",
    "A": "Puede donar a A y AB. Recibe de A y O.",
    "B": "Puede donar a B y AB. Recibe de B y O.",
    "AB": "Puede recibir de todos (donante universal). Solo dona a AB."
}

tipo = input("Ingresa tu tipo de sangre (A, B, AB, O) escribelo tal cual por favor: ")

if tipo in compatibilidad:
    print("Compatibilidad:", compatibilidad[tipo])
else:
    print("Tipo de sangre no válido.")


# 7 - Ingresa una temperatura en °C. Si es menor de 10, hace frío. Si está entre 10 y 25, templado. Más de 25, hace calor.

print("------Ejercicio 7 ------")

temp = float(input("Ingresa la temperatura actual de Palmira en grados centigrados: "))

if temp < 10:
    print(f"Hace mucho frio en Palmira con esos {temp} °C como aguantas ese clima!")
elif temp > 10 and temp <= 25:
    print(f"La temperatura en Palmira es de {temp} °C lo que esta templado,que bonito dia y clima juntos!")
else:
    print(f"Con esos {temp} °C hace mucho calor en Palmira,como aguantas eso!")

# 8 - Crea un menú con opciones 1. Sumar, 2. Restar, 3. Multiplicar. Pide dos números y ejecuta la operación seleccionada.

print("------Ejercicio 8 ------")

print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")

opcion = input("Selecciona una opción (1-3): ")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion == "1":
    resultado = num1 + num2
    print("La suma es:", resultado)
elif opcion == "2":
    resultado = num1 - num2
    print("La resta es:", resultado)
elif opcion == "3":
    resultado = num1 * num2
    print("La multiplicación es:", resultado)
else:
    print("Opción no válida,no esta en la lista de operaciones que te dimos.")

# 9 - Pide un número entre 1 y 12 y muestra el mes correspondiente usando un diccionario.

print("------Ejercicio 9 ------")


numero = int(input("Ingresa un numero del 1 al 12: "))

if numero == 1:
    print(f"El numero {numero} corresponde al mes Enero")
elif numero ==2:
    print(f"El numero {numero} corresponde al mes Febrero")
elif numero ==3: 
    print(f"El numero {numero} corresponde al mes Marzo ")
elif numero ==4: 
    print(f"El numero {numero} corresponde al mes Abril")
elif numero ==5: 
    print(f"El numero {numero} corresponde al mes Mayo ")
elif numero ==6: 
    print(f"El numero {numero} corresponde al mes Junio ")
elif numero ==7: 
    print(f"El numero {numero} corresponde al mes Julio ")
elif numero ==8: 
    print(f"El numero {numero} corresponde al mes Agosto")
elif numero ==9: 
    print(f"El numero {numero} corresponde al mes Septiembre")
elif numero ==10: 
    print(f"El numero {numero} corresponde al mes Octubre")
elif numero ==11: 
    print(f"El numero {numero} corresponde al mes Noviembre ")
elif numero ==12: 
    print(f"El numero {numero} corresponde al mes Diciembre")
else:
    print(f"El numero {numero} no corresponde a ningun mes,solo tenemos 12 meses")

# 10 - Solicita un número de 4 dígitos y determina si comienza con 1, 2 o cualquier otro

print("------Ejercicio 10 ------")


numeroo = input("Ingresa un numero de 4 digitos por favor: ")
if numeroo[0] ==  "1":
    print(f"El numero de 4 digitos: {numeroo} comienza por el numero uno")
elif numeroo[0] == "2":
    print(f"El numero de 4 digitos: {numeroo} comienza por el numero dos")
else:
    print(f"El numero de 4 digitos: {numeroo} no comienza ni por el numero 2 ni por el numero 1, empieza por  cualquier otro")

# 11 - Ingresa una palabra. Muestra si su primera letra es vocal, consonante o un numero.

print("------Ejercicio 11 ------")


palabra = input("Ingresa una palabra cualquiera por favor: ")
if palabra [0] == "A":
    print(f"La palabra {palabra} empieza por la vocal A")
elif palabra [0] == "E":
    print(f"La palabra {palabra} empieza por la vocal E")
elif palabra [0] == "I":
    print(f"La palabra {palabra} empieza por la vocal I")
elif palabra [0] == "O":
    print(f"La palabra {palabra} empieza por la vocal O")
elif palabra [0] == "U":
    print(f"La palabra {palabra} empieza por la vocal U")
elif palabra [0] == "B":
    print(f"La palabra {palabra} empieza por la consonante 'B'")
elif palabra [0] == "C":
    print(f"La palabra {palabra} empieza por la consonante 'C'")
elif palabra [0] == "D":
    print(f"La palabra {palabra} empieza por la consonante 'D'")
elif palabra [0] == "F":
    print(f"La palabra {palabra} empieza por la consonante 'F'")
elif palabra [0] == "G":
    print(f"La palabra {palabra} empieza por la consonante 'G'")
elif palabra [0] == "H":
    print(f"La palabra {palabra} empieza por la consonante 'H'")
elif palabra [0] == "J":
    print(f"La palabra {palabra} empieza por la consonante 'J'")
elif palabra [0] == "K":
    print(f"La palabra {palabra} empieza por la consonante 'K'")
elif palabra [0] == "L":
    print(f"La palabra {palabra} empieza por la consonante 'L'")
elif palabra [0] == "M":
    print(f"La palabra {palabra} empieza por la consonante 'M'")
elif palabra [0] == "N":
    print(f"La palabra {palabra} empieza por la consonante 'N'")
elif palabra[0] == "Ñ":
    print(f"La palabra {palabra} empieza por la consonante 'Ñ'")
elif  palabra[0] == "P":
    print(f"La palabra {palabra} empieza por la consonante 'P'")
elif palabra[0] == "Q":
    print(f"La palabra {palabra} empieza por la consonante 'Q'")
elif palabra[0] == "R":
    print(f"La palabra {palabra} empieza por la consonante 'R'")
elif palabra[0] == "S":
    print(f"La palabra {palabra} empieza por la consonante 'S'")
elif palabra[0] == "T":
    print(f"La palabra {palabra} empieza por la consonante 'T'")
elif palabra[0] == "V":
    print(f"La palabra {palabra} empieza por la consonante 'V'")
elif palabra[0] == "W":
    print(f"La palabra {palabra} empieza por la consonante 'W'")
elif palabra[0] == "X":
    print(f"La palabra {palabra} empieza por la consonante 'X'")
elif palabra[0] == "Y":
    print(f"La palabra {palabra} empieza por la consonante 'Y'")
elif palabra[0] == "Z":
    print(f"La palabra {palabra} empieza por la consonante 'Z'")
else:
    print(f"La palabra {palabra} empieza por un numero")

# 12 - Pide una fruta. Si está en la lista ["manzana", "pera", "piña"], muestra su precio. Si no, indica que no está disponible.

print("------Ejercicio 12 ------")


fruta = [
"Manzana","1300 Pesos",
"Pera","1500 Pesos",
"Piña","1800 Pesos"
]

frutass = input("Ingresa una fruta para comprar,escribalo empezando por mayuscula por favor: ")
if frutass in fruta:
    posicion = fruta.index(frutass)
    print(f"El precio de la {frutass} es {fruta[posicion +1]}")
else:
    print(f"La fruta {frutass} no esta disponible en la lista {fruta}")


# 13 -  Pide tu calificación (0 a 5). Si es menor que 3, reprobado. Entre 3 y 4, aprobado. Mayor a 4, excelente.

print("------Ejercicio 13 ------")


calificacion =  float(input("Ingresa tu nota en Programacion: "))
if calificacion < 3:
    print("Tu calificacion es reprobado,te esperamos el otro año :)")
elif calificacion > 3 and calificacion < 4:
    print("Tu calificacion es aprobatoria pero regular,ve avanzando")
else:
    print("Tu nota es excelente,vas bien!")

# 14 - Pide un número y muestra si es divisible entre 4, entre 6, o no lo es.

print("------Ejercicio 14 ------")


num1 = int(input("Ingresa un numero por el cual creas que sea divisible por 4 o 6: "))
if num1 % 4 == 0 and num1 % 6 == 0:
    print(f"El numero {num1} si es divisble por 4 y 6")
elif num1 % 4 == 0:
    print(f"El numero {num1} solo es divisible por el 4")
elif num1 % 6 == 0:
    print(f"El numero {num1} solo es divisible por 6")
else:
    print(f"El numero {num1} no es divisible ni por 4 ni por 6")

# 15 - Crea un sistema de autenticación básico. Pide usuario y clave. Usa un diccionario para validar.

print("------Ejercicio 15 ------")

usuarios = {
    "juan": "1234",
    "maria": "abcd",
    "admin": "admin123"
}


usuario = input("Ingrese su nombre de usuario: ")
clave = input("Ingrese su clave: ")

if usuario in usuarios:
    if usuarios[usuario] == clave:
        print(f"Acceso concedido. Bienvenido {usuario} a nuestro sistema.")
    else:
        print("Clave incorrecta.")
else:
    print("Usuario no registrado en el sistema.")

# 16 - Solicita una edad y muestra a qué grupo pertenece: niño (0-12), adolescente (13-17), adulto (18-64), mayor (65+).

print("------Ejercicio 16 ------")

edad333 = int(input("Ingresa tu edad: "))
if edad333 > 0 and edad333 <= 12:
    print(f"Eres un niño aun por tener {edad333} años")
elif edad333  >= 13 and edad333 <= 17:
    print(f"Eres un adolescente por tener {edad333} años,que dura etapa!")
elif edad333 > 18 and edad333 < 64:
    print("Eres un adulto ya,felicidades")
else:
    print("Eres un adulto mayor lo sentimos")


# 17 - Pide el nombre de una ciudad. Si está en una tupla, muestra que es capital; si no, muestra “ciudad secundaria”.

print("------Ejercicio 17 ------")

# 17 - Pide el nombre de una ciudad. Si está en una tupla, muestra que es capital; si no, muestra “ciudad secundaria”.

print("------Ejercicio 17 ------")

tuplaaaa = ("Bogota", "Palmira", "Cali", "Washington D.C.", "Caracas")
ciudaddd = input("Ingresa una ciudad, empezando por mayúscula por favor: ")

if ciudaddd in tuplaaaa:
    if ciudaddd == "Bogota":
        print(f"La ciudad {ciudaddd} es capital de Colombia y está en la tupla: {tuplaaaa}")
    elif ciudaddd == "Washington D.C.":
        print(f"La ciudad {ciudaddd} es capital de Estados Unidos y está en la tupla: {tuplaaaa}")
    elif ciudaddd == "Caracas":
        print(f"La ciudad {ciudaddd} es capital de Venezuela y está en la tupla: {tuplaaaa}")
    else:
        print(f"La ciudad {ciudaddd} está en la tupla, pero no es capital de país.")
else:
    print(f"La ciudad {ciudaddd} no está en la tupla, es una ciudad secundaria.")

# 18 -  Ingresa el valor de una compra. Si es mayor de $200.000 aplica un 15% de descuento. Entre $100.000 y $200.000 aplica 10%. Si es menor, no hay descuento.

print("------Ejercicio 18 ------")


compra = float(input("Ingresa el valor de una Television: "))
if compra > 200000:
    descu = compra * 0.15
    descuento_final = compra - descu
    print(f"El precio final a pagar con un 15% de descuento del Televisor por un precio mayor a 200000$ es {descuento_final}$")
elif compra > 100000 and compra < 200000:
    descu2 = compra * 0.10
    descuento_final2 = compra - descu2
    print(f"El precio final a pagar con un 10% de descuento del televisor por un precio entre 100000 y 200000$ es: {descuento_final2}$")
else:
    print("No aplica descuento para este precio")

# 19 - Pide el nombre y el número de horas trabajadas. Calcula el salario con tarifa de $10.000/hora. Si trabajó más de 40 horas, aplica un bono del 20%.

print("------Ejercicio 19 ------")


nombreeee = input("Ingresa tu nombre: ")
horas = int(input("Ingresa el numero de horas trabajadas: "))
tarifa = 10000
if horas  < 40:
    print(f"Tu salario sera de $10.000/hora ya que no trabajaste mas de 40 horas,gracias por su servicio")
else:
    abono = horas * 0.20
    abono2 = tarifa + abono
    print(f"Tu tarifa de $10.000/hora se le abono un 20% dando un total de {abono2}$:")

# 20 - Ingresa tu puntaje en una prueba (0 a 100). Si es menor a 50, insuficiente. De 50 a 79, aceptable. 80 a 100, sobresaliente.

print("------Ejercicio 20 ------")


puntaje = int(input("Ingresa tu puntaje en las olimpiadas de 0 a 100: "))
if puntaje < 50:
    print(f"Tu puntaje de {puntaje} puntos es un puntaje insufciente,siguelo intentando!")
elif puntaje > 50 and puntaje < 79:
    print(f"Tu puntaje de {puntaje} puntos es un puntaje aceptable,muy bien!")
else:
    print(f"Tu puntaje de {puntaje} puntos es sobresaliente,felicitaciones!!")