# Diccionario

my_list = {'a', 'b'}

print(type(my_list))

my_dict= {'Nombre': 'Nicolas',
          'Apellido': 'Gonzales',
          'Apodo': 'Nikorasaau'}

print(type(my_dict))

del (print(my_dict['Apellido']))    #para eliminar apellido y su significado del diccionario


print(my_dict.keys())
print(my_dict.values())

my_dict= list(my_dict)
print(my_dict)

my_dict= set( my_dict)
print(my_dict)