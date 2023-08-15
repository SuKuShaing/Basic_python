person = {
  'name': 'nico',
  'last_name': 'molina',
  'langs': ['python', 'javascript'],
  'age': 50
}

print(person)
person['name'] = "Santi"
print(person)

person['age'] += 1
print(person)

person['langs'].append('rust')
print(person)

del person['last_name']
print(person)

person.pop('age') #Elimina ese par de valores, Se debe enviar algo o se arruina el codigo
print(person)


print('items')
print(person.items())
print(list(person.items()))

print('keys')
print(person.keys())
print(list(person.keys()))

print('values')
print(person.values())
print(list(person.values())) # lo convierte en un arreglo