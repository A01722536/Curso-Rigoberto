cadena = "MImi mIMI"
print(cadena)
print(cadena.lower())
print(cadena.upper())
print(cadena.capitalize())
print(cadena.title())
print(cadena.swapcase())

cadenita=input("Dato alfanúmerico: ")
if cadenita.isalnum(): #Detecta si la entrada NO tiene caracteres especiales NI espacios
    print("Entrada válida")
else:
    print("Entrada inválida")

#Método FIND
email=input("Email: ")
print(email.find("@"))
if email.find("@") >= 0 and email.find(".") >= 0:
    print("{} Email válido". format(email))
else:
    print("Email inválido")

cadenota= "mi mimi mi. mimimimi mi mi. mimimimi mi mimi"
cadenota1= cadenota.replace("mi","per")
print(cadenota1)
cadenota2= cadenota.replace("mi","per",2)
print(cadenota2)