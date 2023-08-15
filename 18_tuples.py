#Tuplas, son inmutalbes, solo son lectura

numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi', 'nico')
print(numbers)
print('0 =>',numbers[0])
print('-1 =>',numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

print(strings)
print(strings.index('zule')) #entrega la posición
print(strings.count('nico')) #Cuenta la cantidad que hay en la tupla

my_list = list(strings) #Pasamos de tupla a lista 
print(my_list)
print(type(my_list))

my_list[1] = 'juli' #Como lista se puede editar, las listas son mutables
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))