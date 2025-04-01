mensaje = "Aloooooh"
respuesta = input(mensaje)
print(respuesta)
print(type(respuesta)) #El input siempre será un string
print("")

nombre = input("Nombre: ")
edad = input("Edad: ")
altura = input("Altura: ")

print(nombre,edad,altura)
print("Hola",nombre,"veo que tienes",edad,"años y mides",altura,"centímetros.")
print("Hola {} veo que tienes {} años". format(nombre, edad))