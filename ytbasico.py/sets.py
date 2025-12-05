# SETS 

my_set = {}
print(type(my_set))

my_set={'Python','JavaScript', 'C++'}
print(type(my_set))

# print(my_set[0]) TypeError: 'set' object is not subscriptable
 
my_set.add('C++')   # no agrega repetidos como C++
print(my_set)

my_set.add('C#')
print(my_set)

my_set_0={'Python','JavaScript', 'C++'}

my_set.difference_update(my_set_0)
print(my_set)