# BUCLES  - Sirven para que se repita algo hasta que indicamos que no se repita

numero = 0
while numero < 10:
    numero += 1
    print(numero)
    if numero ==5:
        print('es menor que 5')
        break
      
print('hola mundo')


lista= ['a','s','l']
for character in range(101):
    print(character) 
    if character ==5:
        print('es menor que 5')
        break


#bucles while

import math
numero= int(input("Digite un numero: "))

while numero<0:
    print("Error --> Deberia ser un numero positivo")
    numero= int(input("Digite un numero: "))


print(f"\nSu raiz cuadrada es: {round(math.sqrt(numero),1)}")
       