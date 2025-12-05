# En una 'lista' de números, retorna el segundo número más grande.
#
# Ejemplo: {5,7,2,7,9,4,8}

lista = [5,7,2,7,9,4,8]

lista.sort()
print(lista[-2])  #aca hay una observacion, si el numero se repite no cumpliria






# Crea una función que reciba días, horas, minutos y segundos 
# (como 'list') y retorne su resultado en milisegundos

def militime(day = 0,hour = 0 , minute=0, second=0 ):
    final_time=0
    hour += day * 24
    minute += hour*60
    second += minute*60
    final_time += second * 1000
    print(final_time)
militime(1,1,0,0)

#Escribe una función que muestre por consola los números
# de 1 a 100 (ambos incluidos y con un salto de línea ente
# cada impresión), sustituyendo los siguientes:
#- Múltiplos de 3 por la palabra 'fizz'.
#- Múltiplos de 5 por la palabra 'buzz'.
#- Múltiplos de 3 y de 5 a la vez por la palabra 'fizzbuzz'.

def fizzbuzz():
    for a in range(1,101):
        if a % 3 ==0 and a % 5 ==0:
            print('fizzbuzz')
        elif a % 3 ==0:
            print('fizz')
        elif a % 5 == 0: 
           print('buzz')
        else:
            print(a)
fizzbuzz()

#chatgpt
lista=[12, 4, 7, 4, 15, 9, 3]

lista.sort()
print(lista[1])

def minute(day=0, hour=0,minute=0,second=0):
    final_time= day*24*60 + hour*60 +minute + second/60
    print(final_time)

minute(1,5,120)



def pingpong():
    for a in range(1,51):
        if a % 4 == 0 and a %6 == 0:
            print('pingpong')
        elif a % 4==0:
            print('ping')
        elif a % 6==0 :
            print('pong')
        else:
            print(a)
pingpong()



[18, 7, 21, 7, 9, 30, 12, 30, 5]
lista=[18, 7, 21, 7, 9, 30, 12, 30, 5]
lista.sort()
print(lista[-3])

def to_seconds(day=0, hour= 0, minute=0, second=0):
    final_time= day*24*60*60 + hour*60*60 +minute*60 + second
    print(final_time)

to_seconds(0,2,1,30)

def fizzpop():
    for a in range(1,41):
         if a %2==0  and a %7==0:
             print('fizz')
         elif a % 2==0:
             print('pop')
         elif a %  7==0:
             print('fizzpop')
         else:
             print(a)
fizzpop()
               



nombres = ["Ana", "Luis", "Carlos", "Ana", "Maria", "Luis", "Pedro"]

sin_repetidos= sorted(set(nombres))
print(sin_repetidos)

def contar_palabras(palabra):
    vocales ='aeiouAEIOU'
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador+= 1
    return contador
palabra= 'hola'
print(contar_palabras(palabra))

def es_palindromo(palabra):
    palabra= palabra.lower().replace('','')
    return palabra == palabra[::-1]

print(es_palindromo('radar'))