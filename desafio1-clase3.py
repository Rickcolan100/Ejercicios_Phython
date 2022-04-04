def imprimo_datos1(**args): #metodo 1 con tupla - * es el numero de argumentos
     for valor in args:
         print(f"{valor} es de tipo {type(valor)}")

def imprimo_datos2(*kwargs): #metodo 2 con kwargs como diccionario - ** todos los argumentos
     for clave,valor in kwargs.items():
         print(f"{clave} es de tipo {type(valor)}")

d = 1.5
g = 2
f = False
print('PRUEBA 1')
imprimo_datos1(d)
lista = (1 , 'algo')
print('PRUEBA 2')
imprimo_datos2(lista)

