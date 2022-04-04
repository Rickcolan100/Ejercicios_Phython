texto = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""

contador = [("Titulo", False) , ("Facil" , 0) , ("Medio" , 0) , ("Dificil" , 0) , ("Muy dificil" , 0)]

#verifica si el tamaño del doctring con __len__ si es menor a 11 en la linea 1
contador["Titulo"] = len(texto.splitlines()[0].split("titulo: ")) <= 11 

#recorre el resumen y suma el contador
for elem in texto.split('resumen: ')[1].split('.'):
     print(elem)
     if len(elem.split()) <= 12:
         contador['Facil'] += 1
     elif len(elem.split()) <= 17:
         contador['Medio'] += 1
     elif len(elem.split()) <= 25:
         contador['Dificil'] += 1
     else:
         contador['Muy dificil'] += 1

if contador['Titulo:']:
     print('El titulo del texto esta bien')
else:
     print('El titulo del texto es demasiado largo')

print(f"""Cantidad de oraciones de oraciones: 
          - Faciles de leer: {contador['Facil']} , 
          - Media de leer: {contador['Medio']}, 
          - Dificil de leer: {contador['Dificil']} , 
          - Muy dificl de leer: {contador ['Muy dificil']}""")    


