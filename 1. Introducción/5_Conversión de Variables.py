##CONVERSIÓN IMPLÍCITA
x=4
y=5.9
z=x+y
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

##CONVERSIÓN EXPLÍCITA
#Convertir float a integer, sólo que al ser int se perderán los decimales. NO SE REDONDEA
a = 3.6
print(a)
print(type(a))
a = int(a)
print(a)
print(type(a))
print("")
#Convertir float a string
b = 42
print(b)
print(type(b))
b = str(b)
print(b)
print(type(b))
print("")
#Convertir float a string
c = 42
print(c)
print(type(c))
c = str(c)
print(c)
print(type(c))
print("")
#Convertir string a float
d = "37.5"
print(d)
print(type(d))
d = float(d)
print(d)
print(type(d))
print("")
#Convertir string a integer
e = "15"
print(e)
print(type(e))
e = int(e)
print(e)
print(type(e))
print("")
#Convertir string con decimal a integer, primero hay que convertirlo a float y luego a int
f = "89.3"
print(f)
print(type(f))
f = float(f)
print(f)
print(type(f))
f = int(f)
print(f)
print(type(f))