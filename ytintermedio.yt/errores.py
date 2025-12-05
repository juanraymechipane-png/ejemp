# TIPOS DE ERRORES

SyntaxError
print ('Hola mundo') # sin la ()


#name error
variable = 5    # si la variable no tienen significado
print(variable)


#IndexError
list_variable= [4,5,7,9,6]
print(list_variable[0])
print(list_variable[3])
print(list_variable[2])
print(list_variable[-1])
print(list_variable[-5])


#No module named 'matth' 
import math


#AttributeError: module 'math' has no attribute '
print(math.pi)


#KeyError: 'apodoo'
variable_dict = {'nombre':'Nicolas',
                 'apodo':'Nikorasu'}
print(variable_dict['apodoo'])
