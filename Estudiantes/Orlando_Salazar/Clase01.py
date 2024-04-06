""" DocStrings
    Esto es un comentario de multiples lineas
    Código: estos son los ejemplos vistos en la clase 1.
    Autor: Andrés Mena A.
"""

linea2 = '\nPrograma Clase 1' # \n caracter especial que representa un salto de linea
print('Bienvenidos al curso de Python' + linea2) # Esto es un mensaje de bienvenida

print("Hola",linea2)

mensaje = "Hola mundo desde Python"
numero = 2024
version = 2.1
visible = False

print(mensaje,numero,version,visible)

print(type(mensaje))
print(type(numero))
print(type(version))
print(type(visible))


Nombre = input("Cual es su nombre? : ")
Edad = input("Cual es su edad: ")

print(f"Bienvenido {Nombre}, su edad es {Edad}")