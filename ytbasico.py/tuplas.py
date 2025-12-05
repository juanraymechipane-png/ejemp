# TUPLAS

my_tupla= (53, 'Perro', 7.8 , True)
print(type(my_tupla))

print(my_tupla[1])
print(my_tupla.count(53))
print(my_tupla.index(7.8))

my_tupla = list(my_tupla)
print(type(my_tupla))

my_tupla.pop()
print(my_tupla)

my_tupla = tuple(my_tupla)
print(type(my_tupla))
print(my_tupla)
