'''
for element in range(5, 21):
  print(element)

'''

my_list = [23, 45, 67, 89, 43]
for element in my_list:
  print(element)


my_tuple = ('nico', 'juli', 'santi', 'seba', 'diego')
for element in my_tuple:
  print(element)


product = {
  'name': 'Camisa',
  'price': 100,
  'stock': 89
}
for element in product:
  print(element, ': ', product[element])


for key, value in product.items():
  print(key, '=>', value)


print('***************')
people = [
  {
    'name': 'nico',
    'age': 34
  },
  {
    'name': 'zule',
    'age': 45
  },
  {
    'name': 'santi',
    'age': 4
  },
  {
    'name': 'zule',
    'age': 45
  }
]

for person in people:
  print('name => ', person['name'])