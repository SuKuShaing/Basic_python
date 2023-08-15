if True:
  print('Deberia ejecutarse')

if False: 
  print('Nunca se ejecuta')



pet = input('¿Cuál es tu mascota favorita?: ')

if pet == 'perro':
  print('Genial, tienes mal gusto: ')
elif pet == 'gato':
  print('Genial, tienes buen gusto: ')
elif pet == 'pez':
  print('Genial, tienes buen gusto: ')
else:
  print('No tiene ninguna mascota entrete')


numero = int(input('¿Ingresa un número?: '))
if numero % 2 == 0:
  print('Tu número es par')
else:
  print('Tu número es impar')


'''
stock = int(input('Digita el stock => '))

if stock >= 100 and stock <= 1000:
  print('el stock es correcto')
else:
  print('el stock es incorrecto')
'''