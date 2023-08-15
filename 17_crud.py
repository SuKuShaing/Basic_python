#CRUD, Create, Read, Update & compile

numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10
print(numbers)

numbers.append(700) #se añade la final un elemento
print(numbers)

numbers.insert(3, 'Insertado') #Inserta (posicion, lo que se inserta)
print(numbers)

tasks = ['todo 1', 'todo 2', 'to do 3']
new_list = numbers + tasks
print(new_list)

print(new_list.index('todo 2'))
index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

new_list.remove(new_list[index]) #elimina el que se encuentre ahí
new_list.remove('todo 1') #elimina el que se llame así
print(new_list)

new_list.pop() #elimina el último
print(new_list)

new_list.pop(0) #elimina la posición que se le dé
print(new_list)

new_list.reverse() #da vuelta el array
print(new_list)

numbers_a = [1, 2, 1, 3, 4, 5, 6]
numbers_a.sort() #Ordena de menor a mayor
print(numbers_a)

string = ["Mochi", "a", "Hola", "Todos", "mochi"]
string.sort()
print(string)