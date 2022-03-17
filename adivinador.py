import random
num_random = random.randrange(100)
ok = False
print("Ingresa 5 numeros entre 0 y 99")
intento = 1
while intento < 6 and not ok:
    num_ing = int(input('Ingresa tu numero: '))
    if num_ing == num_random:
         print('Adivinaste el numero y necesitaste {} intentos'.format(intento))
         ok = True
    else:
         print('Numero equivocado,intente de nuevo')
         intento += 1
if not ok:
    print('\n Todos los intentos fallaron \n El numero es: {}'.format(num_random))

