imprimir = []
palabra = input('Ingresa una palabra: ')
while palabra != 'fin':
     if palabra[-1] == palabra[0]:
           imprimir.append(palabra)
           palabra = input('Ingresa una palabra: ')
print('lista de palabras')         
for i in imprimir:
      print(i)