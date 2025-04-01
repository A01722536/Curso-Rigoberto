import re

productos= "Producto A: 123, Producto B: 4567, Producto C: 789, Producto D: 43"

#Patrón para encontrar códigos de 3 dígitos exactos

patron_d = r"\b\d{3}"

coin=re.findall(patron_d, productos)
print("Códigos aceptados:",coin)

texto_w="Cliente: Juan123, Cliente: Maria_45, Cliente: Pedro88, Cliente: Luisa!"
patron_w=r"\w+"
coincidencias_w=re.findall(patron_w,texto_w)
print(coincidencias_w)

texto_s="Tarjeta de Crédito, Seguro de Vida, Cuenta corriente, Inversión a plazo"
#\s es exactamente lo mismo que un espacio
patron_s=r"\w+\s\w+"
coincidencias_s=re.findall(patron_s,texto_s)
print(coincidencias_s)