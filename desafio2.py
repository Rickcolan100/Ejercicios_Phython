notas = []
cant = 0
print('-----------INGRESE NOTAS-----------------------')
nota = int(input('ingrese una nota:'))
while nota != -1:
      notas.append(nota)
      nota = int(input('ingrese una nota:'))
print('cantida de notas:')
for i in notas:
     print(i)
prom = sum(notas) / len(notas)
print(f'el promedio es de {prom}')
for i in range(len(notas)):
     if notas[i] < prom:
           cant += 1  
print(f'la cantidad de notas menor al promedio es: {cant}')         
print('-------------------------------------------------')
