print('Bienvenid@ a "ManejaYa"')
edad=int(input("Ingresa tu edad por favor: "))

if edad<16:
    print("No eres apt@ para conducir.")
elif edad==16 or edad==17:
    print("Puedes sacar un permiso de conducir.")
elif edad>=18 and edad<=70:
    print("Puedes sacar una licencia de conducir.")
elif edad>70:
    print("Puedes sacar una licencia especial.")
else: print("Lo escrito no es una válido.")