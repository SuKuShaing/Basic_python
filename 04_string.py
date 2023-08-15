name = 'Seba'
last_name = 'Sanhueza'
print(name)
print(last_name)

my_age = 30

full_name = name + ' ' + last_name
print(full_name)

big_text = """
Hola madafakas
que pasa
todas las larvar
"""
print(big_text)

quote = "I'm Seba"
print(quote)

# format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print(template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print('V2')
print(template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('V3')
print(template)

template = f"Hola, mi nombre es {name} {last_name} y mi edad es de {my_age} años"
print('V4')
print(template)
