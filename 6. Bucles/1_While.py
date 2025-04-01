i=0
o=0
# i+=1 es lo mismo que i=i+1
while i < 4:
    i+=1
    print(i)

while o < 4:
    print(o)
    o+=1

num=64
con=0
while num>=1:
    num/=2
    con+=1
print(con)

while True: #Ciclo infinito
    op=int(input("Elija un num(1,2,3): "))
    if op==1:
        print("mimi")
    elif op==2:
        print("mumu")
    elif op==3:
        print("meme")
        break
    else:
        print("Ñao ñao")