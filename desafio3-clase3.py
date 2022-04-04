def ordeno1(cadena="ss"):
     """ Implementación usando sort"""
     lista = cadena.split()
     lista.sort(key=str.lower)
     #lista.sort()    
     return lista
     
print(ordeno1("Hoy puede ser un gran día. "))

def ordeno2(cadena):
     """ Implementación usando sorted"""
     lista = cadena.split()
     return sorted(lista, key=str.lower)

print(ordeno2("Hoy puede ser un gran día. "))

def ordeno3(usuarios):
     """ Usamos sorted con una expresión lambda"""
     return sorted(usuarios, key=lambda usuario: usuario[0])

usuarios = [('JonY BoY', 'Nivel3', 15),('1962', 'Nivel1', 12),('caike', 'Nivel2', 1020),('Straka^', 'Nivel2', 1020),]
print(ordeno3(usuarios))