print("")
cuota=0
cuenta=0
mensajito="""TAQUERÍA EL MEGÓN
Guisos:
1. Cabeza-$18 c/u
2. Barbacoa-$15 c/u
3. Chicharrón-$16 c/u
4. Ver total de la cuenta
5. Finalizar cuenta"""
#Creamos un bucle general
while True:
    print(mensajito)
    orden=input("Selecciona la opción que deseas ordenar: ")
    if orden!="1" and orden!="2" and orden!="3" and orden!="4" and orden!="5":
        print("Opción no disponible.")
        orden=input("Favor de seleccionar una opción del 1-5 y únicamente el número:")
        orden=int(orden)
        cantidad=int(input("¿Cuántos taquitos le ponemos?: "))
        if orden==1:
            cuota=cantidad*18
            cuenta=+cuota
            print(mensajito)
            orden=input("Selecciona la opción que deseas ordenar ahora: ")
        elif orden==2:
            cuota=cantidad*15
            cuenta=+cuota
            print(mensajito)
            orden=input("Selecciona la opción que deseas ordenar ahora: ")
        elif orden==3:
            cuota=cantidad*16
            cuenta=+cuota
            print(mensajito)
            orden=input("Selecciona la opción que deseas ordenar ahora: ")
        elif orden==4:
            print("Su cuenta hasta ahora es de:",cuenta,"pesos")
            print(mensajito)
            orden=input("Selecciona la opción que deseas ordenar ahora: ")
        if orden==5:
            break
    print("Cuenta finalizada")
    print("Monto total:",cuenta,"pesos")