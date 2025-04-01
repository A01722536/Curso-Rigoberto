mensaje= """Teléfono:
1. Lista
2. Agregar/Modificar
3. Eliminar
¿Qué desea hacer?: """
accion=(input(mensaje))
while accion!="1" and accion!="2" and accion!="3":
    accion=input("Favor de sólo seleccionar un número existente (Sin letras ni puntos): ")

lista="""
Lista de contactos:
Ángel
Alejandra
Camila
Emily
Iván
Luisa
Marcelo
Mariana
Natalia
Roberto"""
an="Ángel"
al="Alejandra"
ca="Camila"
em="Emily"
iv="Iván"
lu="Luisa"
mc="Marcelo"
mr="Mariana"
na="Natalia"
ro="Roberto"
agr_o_mod="""
Agregar o Modificar:
Favor de ser específico con los acentos y mayúsculas.
De lo contrario, se reconocerá como un número nuevo.
Escriba el contacto que desee modificar o agregar: """
eliminar="""
Eliminar:
Favor de ser específico con los acentos y mayúsculas.
De lo contrario, no se reconocerá el número.
Escriba el contacto que desee eliminar: """
num=8128242622

if accion=="1":
    print(lista)
elif accion=="2":
    nombre=input(agr_o_mod)
    if nombre==an or nombre==al or nombre==ca or nombre==em or nombre==iv or nombre==lu or nombre==mc or nombre==mr or nombre==na or nombre==ro:
        print("Contacto:",nombre)
        print("Número:",num)
        mod=input("Desea modificar el contacto(1) o el número(2):")
        while mod!= "1" and mod!="2":
            print("Favor de sólo seleccionar un número existente (Sin letras ni puntos).")
            mod=input("Desea modificar el contacto(1) o el número(2):")
        if mod=="1":
            nombre=input("Favor de introducir el nuevo contacto que se asociará con este número: ")
            print("Contacto:",nombre)
            print("Número:",num)
            print("El cambio se ha guardado exitósamente.")
        elif mod=="2":
            num=input("Favor de introducir el nuevo número que se asociará con este contacto: ")
            print("Contacto:",nombre)
            print("Número:",num)
            print("El cambio se ha guardado exitósamente.")
            
    else:
        numnu=input("Favor de introducir el número que se asociará con este contacto: ")
        print("El contacto:",nombre)
        print("Con el número:",numnu)
        print("Se ha guardado exitósamente.")
elif accion=="3":
    nombre=input(eliminar)
    while nombre!=an and nombre!=al and nombre!=ca and nombre!=em and nombre!=iv and nombre!=lu and nombre!=mc and nombre!=mr and nombre!=na and nombre!=ro:
         nombre=input("El contacto no fue reconocido, favor de intentar nuevamente: ")
    print("""
          ¿Seguro que deseas eliminar el contato de:""",nombre)
    s_n=input("¿Sí o No?: ")
    if s_n.lower() == "si" or s_n.lower() == "sí":
        print("El contacto ha sido eliminado.")
    elif s_n.lower() == "no":
        print("El contacto NO ha sido eliminado.")