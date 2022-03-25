print('--------------------ingrese nombres y notas------------------------')
nombre = input("Ingresa un nombre: (<FIN> para finalizar) ")
listado = {}
while nombre != "FIN":
       nota = int(input(f"Ingresa la nota de {nombre}: "))
       listado[nombre] = nota
       nombre = input("Ingresa un nombre: (<FIN> para finalizar) ")
print('listado de alumnos y notas: ')
print(listado)
total = 0
for nota in listado.values():
      total += nota
prom = total / len(listado)    
print(f'promedio de notas: {prom}')
print('estudiantes debajo del promedio: ')
for nombre,nota in listado.items():
      if nota < prom:
             print(nombre)
print('---------------------------------------------------------------------')
