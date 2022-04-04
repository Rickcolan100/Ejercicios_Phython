from ntpath import join
from xml.etree.ElementTree import tostring


def encripto(Palabra):
      valores = [ord(c) for c in Palabra]
      encriptando = list(map(lambda x : x + 4, valores))
      palabra =  "".join(map(chr, encriptando))
      return print(f'La palabra {Palabra} encriptada es: {palabra}')

palabra = input("Ingrese una palabra a encriptar: ")
encripto(palabra)
