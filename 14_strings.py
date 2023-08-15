text = 'Ella sabe programar en Python'

'''
print('JavaScript' in text)
print('Python' in text)

if 'Python' in text:
  print('Elegiste bien!!')
else:
  print('Tambie elegiste bien!!')
'''

size = len(text)
print(size)

print(text)
print(text.upper())
print(text.lower())
print(text.count('a')) #Cuanta la cantidad de 'a'

print(text.swapcase()) #voltea mayusculas en miniculas y viceversa
print(text.startswith('Ella')) #True, verifica sí empieza con esos caracteres
print(text.endswith('Rust')) #False, verifica sí termina con esos caracteres
print(text.replace('Python', 'Go')) #Cambia un texto por otro

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize()) #ponde en mayuscula el primer caracter del parrafo
print(text_2.title()) #ponde en mayuscula la primera letra de cada palabra
print(text_2.isdigit()) #True | verifica que es un digito

print('398'.isdigit()) #True