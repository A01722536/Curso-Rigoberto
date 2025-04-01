#Le preguntamos al usuario por quién votar con un mensaje de bienvenida:
mensaje= """Bienvenid@ al INE, las opciones de candidatos son las siguientes:
Candidato A
Candidato B
Candidato C
¿Por cuál candidato desea votar?
Favor de sólo introducir la letra que representa al candidato: """
candidato=input(mensaje)
#Definimos que información darle al usuario dependiendo de su voto:
if candidato.upper() == "A":
    print("Usted ha votado por el partido rojo.")
elif candidato.upper() == "B":
    print("Usted ha votado por el partido verde.")
elif candidato.upper() == "C":
    print("Usted ha votado por el partido azul.")
else:
    #Si la letra es errónea, le aparece este mensaje:
    print("La opción es errónea.")
    print("Favor de elgir una letra que represente a un candidato")