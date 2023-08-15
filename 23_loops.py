matriz = [
  [1, 2, 3,], 
  [4, 5, 6], 
  [7, 8, 9]
]

"""
print(matriz[0])
print(matriz[0][1])
"""

for row in matriz:
  print(row)
  for column in row: #el row debe ser el nombre de la lista del ciclo anterior
    print(column)