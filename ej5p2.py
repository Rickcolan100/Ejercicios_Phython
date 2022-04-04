print('Ingrese frase y palabra para ver que se repiten')
frase = input("Ingrese una frase: ")
palabra = input("Ingrese una palabra: ")
print(f"Resultados: {frase.lower().count(palabra.lower())}")