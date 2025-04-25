import random  # Importamos la librería random para elegir elementos al azar
# Lista de caracteres que se pueden usar en la contraseña
caracteres = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
# Pedimos al usuario que elija la longitud de la contraseña
longitud_contraseña = int(input("Introduzca la longitud del pase: "))
contraseña = ""  # Creamos una variable vacía donde guardaremos la contraseña
# Repetimos el proceso 'pass_length' veces para crear la contraseña
for i in range(longitud_contraseña):  
    contraseña += random.choice(caracteres)  # Elegimos un carácter aleatorio y lo agregamos a la contraseña
print(contraseña)  # Mostramos la contraseña generada