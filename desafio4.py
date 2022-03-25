listado = {}

def cargar_diccionario():
     nombre = input("Ingresa un nombre: (<FIN> para finalizar) ")
     while nombre != "FIN":
         nota = int(input(f"Ingresa la nota de {nombre}: "))
         listado[nombre] = nota
         nombre = input("Ingresa un nombre: (<FIN> para finalizar) ")
  
def calcular_promedio():
     total = 0
     for nota in listado.values():
          total += nota
          prom = total / len(listado)
     return prom

print('PROGRAMA PRINCIPAL')
cargar_diccionario()
print('lista de alumnos: ')
print(listado)
calculo = calcular_promedio()
print(f'promedio de notas: {calculo}')
print('alumnos debajo del promedio: ')
for nombre,nota in listado.items():
     if nota < calculo:
         print(nombre)    
print('PROGRAMA TERMINADO')