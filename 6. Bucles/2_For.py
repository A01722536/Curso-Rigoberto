lista=["u","d","t"]
print(lista)
for i in lista:
    print(i)
tupla = (1,2,3,4,5)
for j in tupla:
    print(j)

for j in range(1,10,2): #range(inicio, fin, multiplo)
    print(j)

carac="mimimimi"
for letr in carac:
    print(letr)

for s in range(1,11):
    print(s)
    if s==5:
        break

for t in range(1,11):
    if t==6:
        continue
    print(t)