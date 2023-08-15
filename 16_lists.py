numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['Leer', 'Comer', 'Garchar', 'Divertirme', True]
print(tasks)
print(type(tasks))

print(numbers[0])
print(tasks[0])

"""
text = 'Hola'
text[0] = 'W' #Esto da un ERROR, los strings, son inmutables
"""

tasks[0] = 'Trabajar'
print(tasks)

tasks[0] = 'Descansar' # se puede modificar infinitas veces
print(tasks)

print(numbers[:3])
print(True in tasks)
print('Descansar' in tasks)
print('Leer' in tasks)
print('Garchar' in tasks) #True
