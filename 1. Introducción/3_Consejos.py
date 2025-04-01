#Cómo saber qué palabras son reservadas, aunque no son todas
import keyword
print(keyword.kwlist)

#NO pueden ser variables las palabras reservadas
print = 43

#NO se inicia con un número
43 = "Camila"
3erlugar = "Eufracio"

#NO se usan caracteres especiales
Niñ@s = "Tito"

#NO se utilizan espacios ni tmp guiones
edad jóvenes = 10
edad-jóvenes = 11
#Los espacios se reemplazan con las siguientes alternativas:
#Guión Bajo
edad_jóvenes = 12
#Notación Camello
edadJóvenes = 13
#Notación Serpiente
EdadJóvenes = 14

