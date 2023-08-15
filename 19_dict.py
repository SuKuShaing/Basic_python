my_dict = {}
print(type(my_dict))
p = type(my_dict)
print(type(p))

my_dict = {
  'avion': 'tiene alas',
  "name": "Pepe",
  'last_name': 'Molina',
  'fabricacion': 'Tu maima'
}

print(my_dict)
print(len(my_dict)) #muestra la cantida de pares

print(my_dict['name'])
print(my_dict['last_name'])
#print(my_dict['unvalor']) #al no estar la llave se crachea le programa
print(my_dict.get('unvalor')) #arroja un None y se puede manejar

print('avion' in my_dict)
print('otropotro' in my_dict)