'''
while True:
  print('Se ejecuto')
'''

'''
counter = 0

while counter < 10: 
  counter += 1
  print(counter)
'''

'''
counter = 0

while counter < 20: 
  counter += 1
  print(counter)
  if counter == 15:
    break #Termina el ciclo anticipadamente
'''



counter = 0

while counter < 20: 
  counter += 1
  if counter < 15:
    continue #Salta al siguiente ciclo sin continuar leyendo la siguiente linea
  print(counter)