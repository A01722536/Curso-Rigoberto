#Le preguntamos al usuario la información que ocupamos:
precio=float(input("¿Cuánto cuesta su aparato? (Sin IVA): "))
huawei=input("¿Su aparato es HUAWEI? (Sí o no): ")
#Revisamos si le aplicamos el descuento por el precio al aparato:
if precio >= 2000:
    precio_final=precio-(precio*0.1)
elif precio < 2000:
    precio_final=precio
else:
    print("Ese precio no es válido")
#Revisamos si aplicamos el descuento por ser HUAWEI al aparato:
if huawei.lower() == "si" or huawei.lower() == "sí":
    precio_final=precio_final-(precio_final*0.05)
elif huawei.lower() == "no":
    precio_final=precio_final
else:
    print("Respuesta no válida")
#Le mostramos al usuario el precio final con IVA incluido
precio_final=precio_final+(precio_final*0.16)
print("Tu precio final (con IVA) es de: ${}". format(precio_final))