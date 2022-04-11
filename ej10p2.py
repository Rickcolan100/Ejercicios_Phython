nombres = open('nombres_1.txt', 'r' , encoding='utf8')
evaluacion_1 = open('eval1.txt', 'r' , encoding='utf8')
evaluacion_2 = open('eval2.txt', 'r' , encoding='utf8')
lista ={}

#Guardar los datos en una estructura
for nombres,evaluacion_1,evaluacion_2 in zip(nombres,evaluacion_1,evaluacion_2):
     lista[nombres.strip('\n,\' ')] = int(evaluacion_1.strip('\n, ')) + int(evaluacion_2.strip('\n, '))

print('Lista de nombres de alumnos y sus notas sumadas de las evaluaciones: ')
print(lista)

#Promedio notas totales
prom= 0
cant = 0
for alumno in lista:
      cant += lista[alumno]

prom = cant / len(lista) 

print(f'El promedio de notas es: {prom}')

#Alumnos menores al promedio
print('Lista de alumnos con notas menores al promedio:')
for alumno in lista:
      if lista[alumno] < prom:
           print(alumno)