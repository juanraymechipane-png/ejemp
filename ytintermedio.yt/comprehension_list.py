# COMPREHENSION LIST

normal_list = [1,2,3,4,5,6,7,]
print(normal_list)

def sum_number(number):
    number += 10
    return number 

comprehension_list= [sum_number(i) for i in range (8)]
print(comprehension_list)


comprehension_list= [i *2 for i in range (8)]   # i es para guardar, el *2 es para multipli. cada numero
print(comprehension_list)

my_string= 'hola mundo'
comprehension_list= [i for i in my_string]
print(comprehension_list)
