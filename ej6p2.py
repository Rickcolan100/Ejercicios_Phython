from collections import Counter

frase = """ Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
     automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
     reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
     un montón de archivos con fotos de una manera compleja. Tal vez quieras
     escribir alguna pequeña base de datos personalizada, o una aplicación
     especializada con interfaz gráfica, o UN juego simple."""


palabras_minusculas = frase.lower().split()
no_repetidas = dict(Counter(palabras_minusculas)).fromkeys(palabras_minusculas,1)
print(no_repetidas)

