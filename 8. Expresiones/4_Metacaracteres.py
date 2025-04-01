import re
patron_punto=r"A.B"
transacciones = "A1B A@B A-B A B"
coincidencias_punto=re.findall(patron_punto, transacciones)
print(coincidencias_punto)

#Asterisco (*)
#Con tal de que coincida todo menos lo que va antes del asterisco
patron_asterisco = r"PRX*C"
productos="PRC PRXC PRXXC PRXXXC PRX"
coincidencias_asterisco=re.findall(patron_asterisco, productos)
print(coincidencias_asterisco)

#Más (+)
#Coincide con una o más repeticiones del patrón anterior
patron_mas = r"F\d+C"
facturas="F1C F2C F12C FC"
coincidencias_mas=re.findall(patron_mas, facturas)
print(coincidencias_mas)

#Signo de interrogación (?)
#Coincide con cero o una ocurrencia del patrón anterior
patron_interrogacion = r"US?\$"
monedas="USD US$ $ U$D"
coincidencias_interrogacion=re.findall(patron_interrogacion, monedas)
print(coincidencias_interrogacion)

#Diseñar patrón para verificar una fecha válida
print("Fecha{dd-mm-yyyy}",re.search(r"\d{2}-\d{2}-\d{4}","11-03-2025"))

patron_fecha = r"(0[0-9]|1[0-9]|2[0-9]|3[0-1])-(0[0-9]|1[0-2])-\d{4}"
fecha_valida="11-03-2025"
fecha_invalida="41-23-2025"
coincidencias_fecha=re.search(patron_fecha, fecha_valida)
print(coincidencias_fecha)

print (coincidencias_fecha.group(0))
print (coincidencias_fecha.group(1))
if coincidencias_fecha:
    print("Fecha encontrada:", coincidencias_fecha.group())
else:
    print("No se encontró fecha.")

print("Tres dígitos:", re.search(r"\d{1,3}","189 22 1"))
print("Cuatro dígitos:", re.findall(r"\d{3,4}","2145 236 58965 22"))