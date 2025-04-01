import re
print(re.findall(r"[Pp]ython", "mimimimi momomo Python, python mumumumu memem"))

texto = "abc123 DEF456"
patron1=r"[a-z0-9]"
print(re.findall(patron1,texto))
patron2=r"[A-Z0-9]"
print(re.findall(patron2,texto))
patron3=r"[A-Za-z0-9]"
print(re.findall(patron3,texto))

#Busca en toda la cadena la primera coincidencia
print(re.search(r"\bBitcoin\b","Bitcoin bitcoin"))
print(re.search(r"\bBitcoin\b","bitcoin Bitcoin"))
print(re.search(r"\bBitcoin\b","BitcoinBitcoin"))

#Checa si la cadena inicia con tal
print(re.search(r"^La","Labiskskstcoin"))

#Checa si la cadena termina con tal
print(re.search(r"LOL$"," mimim msossodo dokdojdlo jdoLOL"))