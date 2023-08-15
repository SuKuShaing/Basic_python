text = "Ella sabe Python"
'''
print(text[0])
print(text[1])
print(len(text))
print(text[len(text)-1])
print(text[-1])
'''
# slicing
print(text[0:4]) #se coloca en la casilla 0 y de ahí cuenta 4 casillas
print(text[10:16])
print(text[:10]) # por defecto parte en 0
print(text[5:-1]) # llega al final menos el último caracter
print(text[5:]) #por defecto llega al final
print(text[:]) #desde inicio al final
print(text[10:16:1]) #va de una en una casilla, lo que hace normalmente
print(text[10:16:2]) #Salta de 2 en dos, es decir quedda una casilla entremedio sin seleccionar
print(text[::-1]) #para obtener la oración al revez