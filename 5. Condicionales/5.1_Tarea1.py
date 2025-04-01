#Le preguntamos al usuario cuáles quiere que sean los cuatro valores:
A=float(input("Punto A: "))
B=float(input("Punto B: "))
X=float(input("Eje X: "))
Y=float(input("Eje Y: "))
#Después hacemos un filtro para saber que las cuatros variables sean números válidos:
if A>=0 or A<=0:
    if B>=0 or B<=0:
        if X>=0 or X<=0:
            if Y>=0 or Y<=0:
                #Si las cuatro son números le mostramos al usuario la Distancia:
                D=((((A*X)-(B*X))**2)+(((A*Y)-(B*Y))**2))**0.5
                print("Distancia:",D)
#Si alguna variable no pasa el filtro debería de brindar el mensaje de abajo:
else:
    print("Una variable brindada no es un número válido")