numero = int(input("ingresa un numero entero para verificar si es primo: "))

if numero <= 1:
    print("El nuumero no es primo")
else:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print("numero es primo")
    else:
        print("numero no es primo")