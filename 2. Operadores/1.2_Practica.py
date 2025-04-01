payaso_g=112
muñeca_g=223
cantidad_payaso=input("¿Cuántos payasos desea comprar?")
cantidad_payaso = int(cantidad_payaso)
cantidad_muñeca=input("¿Y cuántas muñecas quiere comprar?")
cantidad_muñeca = int(cantidad_muñeca)
cantidad_kg=((payaso_g*cantidad_payaso)+(muñeca_g*cantidad_muñeca))/1000
print("Su peso total sería de",cantidad_kg,"kilos")