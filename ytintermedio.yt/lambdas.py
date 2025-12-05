#LAMBDAS

my_lambda = lambda num1 , num2 : num1+ num2 *2
print(my_lambda(5,4))

def def_lambdas(value):
    return lambda number : 2* value + number
print (def_lambdas(5)(8))