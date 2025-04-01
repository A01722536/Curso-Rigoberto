cuenta_final=0
print("Bienvenid@ al registro de compras")
print("Ingrese todos los montos del cliente:")
registro=int(input('Para finalizar escriba el número "0":'))
while registro<0:
    print("Los montos negativos no son válidos")
    registro=int(input("Favor de intentar nuevamente:"))
while registro>0:
    cuenta_final=cuenta_final+registro
    registro=int(input('Ingrese el siguiente monto o escriba el número "0":'))

if registro==0:
    print("")
    print("Registro Finalizado")
    if cuenta_final<1000:
        print("Monto total recibido:",cuenta_final)
    elif cuenta_final>1000:
        cuenta_final=cuenta_final-(cuenta_final*0.1)
        print("Descuento por monto mayor a $1000 aplicado")
        print("Monto total recibido:",cuenta_final)