def a_segundos(h, m, s):
    return h * 3600 + m * 60 + s

def de_segundos(s):
    h = s // 3600
    m = (s % 3600) // 60
    s = s % 60
    return h, m, s

def menu():
    while True:
        print("1. A segundos")
        print("2. H-M-S")
        print("3. Salir")
        op = input("Opcion: ")
        
        if op == "1":
            h = int(input("Horas: "))
            m = int(input("Minutos: "))
            s = int(input("Segundos: "))
            print("Total segundos:", a_segundos(h, m, s))
            
        elif op == "2":
            s = int(input("Segundos: "))
            h, m, s = de_segundos(s)
            print(h, "horas", m, "minutos", s, "segundos")
            
        elif op == "3":
            break