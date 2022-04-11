nombres_1 = list(open('nombres_1.txt', 'r' , encoding='utf8'))
nombres_2 = list(open('nombres_2.txt', 'r' , encoding='utf8'))
notas_1 = list(open('eval1.txt', 'r' , encoding='utf8'))
notas_2 = list(open('eval2.txt', 'r' , encoding='utf8'))
lista = {}

#Nombres de estudiantes que se encuentran en las dos listas
for i in range(0,len(nombres_1)):
     nombres_1[i] = nombres_1[i].strip('\'\n, ')
     
for j in range(0,len(nombres_2)):     
     nombres_2[j] = nombres_2[j].strip('\'\n, ')

lista_nueva = [nom1 for nom1 in nombres_1 if nom1 in nombres_2]

print('Lista de nombres en ambas listas: ')
for nom in lista_nueva:
      print(nom)

#Lista de estudiantes con notas de las dos evaluaciones y las totales
for i in range(0,len(notas_1)):
     notas_1[i] = notas_1[i].strip('\'\n, ')
notas_1 = map(int, notas_1)     

for i in range(0,len(notas_2)):
     notas_2[i] = notas_2[i].strip('\'\n, ')
notas_2 = map(int,notas_2) 

for nombres_1,notas_1,notas_2 in zip(nombres_1,notas_1,notas_2):
      lista[nombres_1] = notas_1,notas_2,notas_1 + notas_2


print('   Nombre  Eval1  Eval2  Total')
i=0
for nombre in lista:
      print(f'{i}  {nombre}  {lista[nombre][0]:^3}    {lista[nombre][1]:^3}    {lista[nombre][2]:^3} ')
      i+=1