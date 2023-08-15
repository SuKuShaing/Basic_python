"""
print('hello world')

#cometario entre lineas

print('Hola, soy seba y tengo 30 años')

print('12+5 = ', 12+5)

#Esto es un comentario
'''
Hola a todes
'''

Hola a todes
"""
import random
from os import system

#system("clear")  #Para sistemas Linux
#system("cls") #Para sistemas windows

options = ('1', '2', '3')
election = ('a', 'b', 'c')
volver_a_jugar = True

while volver_a_jugar:

  cantidad_de_juegos = 0
  usuario_wins = 0
  computer_wins = 0
  ronda = 0

  user_election = input(
    'Escoja su opción: "A la Primera"(a), "Al mejor de 3"(b), "Al mejor de 5"(c) => ')
  system("clear")  #Para sistemas Linux
  
  if not user_election in election:
    print(f'"{user_election}" <= Esa opción no es valida!!!!!')
    print('Seleccione una de las 3 formas!!!!!')
    continue

  if user_election == 'a':
    cantidad_de_juegos = 1
  elif user_election == 'b':
    cantidad_de_juegos = 3
  else:
    cantidad_de_juegos = 5

  while True:
    user_option = input(
      'Escoge el número de tu opción: (1)Piedra, (2)Papel o (3)Tijeras => ')
    system("clear")  #Para sistemas Linux
    computer_option = random.choice(options)

    if not user_option in options:
      print('Esa opción no es valida!!!!!')

    print(' ')
    print('*' * 50)
    print(' ')

    ronda += 1
    print(f'RONDA N°: {ronda}')
    
    print(' ')
    print('*' * 50)
    print(' ')

    if user_option == '1':
      print('Usuario elige: Piedra')
    if user_option == '2':
      print('Usuario elige: Papel')
    if user_option == '3':
      print('Usuario elige: Tijeras')

    if computer_option == '1':
      print('La computadora escoje: Piedra')
    if computer_option == '2':
      print('La computadora escoje: Papel')
    if computer_option == '3':
      print('La computadora escoje: Tijeras')

    print(' ')
    print('*' * 50)
    print(' ')

    if user_option == computer_option:
      print('Empate!')

    elif user_option == '1':
      if computer_option == '3':
        print('Piedra gana a tijeras')
        print('Gana el Usuario')
        usuario_wins += 1
      else:
        print('Papel gana a piedra')
        print('Gana la computadora')
        computer_wins += 1

    elif user_option == '2':
      if computer_option == '1':
        print('Papel gana a piedra')
        print('Gana el Usuario')
        usuario_wins += 1
      else:
        print('Tijeras le gana a papel')
        print('Gana la computadora')
        computer_wins += 1

    elif user_option == '3':
      if computer_option == '2':
        print('Tijeras le gana a papel')
        print('Gana el Usuario')
        usuario_wins += 1
      else:
        print('Piedra gana a tijeras')
        print('Gana la computadora')
        computer_wins += 1

    print(' ')
    print('*' * 50)
    print('*' * 50)
    print(' ')
    print(f'Compuradora => {computer_wins} VS {usuario_wins} <= Tu')
    print(' ')
    print('*' * 50)
    print('*' * 50)
    print(' ')

    
    if usuario_wins / cantidad_de_juegos > 0.5:
      print('TU Ganaste!!!!')
      break
    if computer_wins / cantidad_de_juegos > 0.5:
      print('TU Pierdes U,U El Computador Gana')
      break

  print(' ')
  againg = input('Desea volver a jugar: Si(s) o No(n) => ')
  system("clear")  #Para sistemas Linux

  if againg == 'n':
    volver_a_jugar = False
    print('Adios')
