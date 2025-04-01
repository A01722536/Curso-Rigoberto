num=int(input("Dame un número: "))
contador=0
mult=0

while contador <= 10:
    print(mult)
    mult+=num
    contador+=1

num1=int(input("Dame un primer número: "))
num2=int(input("Dame un segundo número: "))
while num1>=num2:
    print("El primer número debe ser menor que el segundo")
    num1=int(input("Dame un primer número: "))
    num2=int(input("Dame un segundo número: "))
for n in range(num1,num2):
    if n%2 == 0:
        continue
    print(n)