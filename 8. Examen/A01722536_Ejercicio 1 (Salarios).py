print("")
#Damos un mensaje de bienvenida
print("Bienvenid@ al SBM (Sistema de Bonificaciones de MgoCorp)")
#Pedimos las variables que usaremos
nombre=input("Favor de introducir su nombre completo: ")
salario=float(input("Favor de introducir su salario actual: "))
mensajito="""Favor de escribir si su rendimiento fue excelente, bueno, regular o malo
Nuestro sistema es muy exacto por lo que le pedimos escribir correctamente la palabra que describa mejor su rendimiento: """
rendimiento=input(mensajito)
#Calculamos el bono del usuario
if rendimiento.lower() == "excelente":
    bono=salario*1.2
elif rendimiento.lower() == "bueno":
    bono=salario*1.1
elif rendimiento.lower() == "regular":
    bono=salario*1.05
else:
    bono=salario
#Le exponemos al usuario si su salario obtuvo un bono
if bono>salario:
    print("Felicidades",nombre, "tu nuevo salario es de:",bono,"pesos.")
elif bono==salario:
    print("Lo sentimos",nombre, "tu salario sigue siendo el mismo de:",bono,"pesos.")