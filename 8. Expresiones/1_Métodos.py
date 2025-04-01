import re

print("word: \n\n")
#r es raw, para que el print se muestre tal y como está
print(r"word: \n\n")
str = "mimimimimsisidmi"
palabra="mimi"
match=re.search(palabra,str)
print(type(match))
print(match)
if match:
    print("Found:",palabra)
else:
    print("Not found.")

print(match.start()) #Posición donde empieza la coincidencia
print(str[5])
print(match.start()) #Posición donde termina la coincidencia
print(match.span()) #Tupla con posiciones de la coincidencia
print(match.string) #Muestra todo el texto original de la coincidencia