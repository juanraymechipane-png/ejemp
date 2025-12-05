#expresion algoritmica

a = float(input("Digite un numero: "))
b = float(input("Digite un numero: "))
c = float(input("Digite un numero: "))

resultado = (a**3)*(b**2 - 2*a*c)/(2*b)

print(f"El resultado es: {resultado}")




a = float(input("a -> "))
b = float(input("b -> "))

resultado= (3+5*8)<3 and ((-6*4/3)+2<2) or (a>b)

print(f"El resultado es: {resultado}")


a = float(input("a -> "))
b = float(input("b -> "))

a , b = b , a
print(f"El nuevo valor de a es: {a} ")
print(f"El nuevo valor de b es: {b} ")


r = float(input("r -> "))

area = 3.14*r**2
longitud = 2*3.14*r

print(f"El area es: {area:.3f}")
print(f"La longitud es: {longitud:.3f}")


'''    :.3f es para que los decimales sean 3
'''
precio_compra= float(input("Total de la compra:"))

descuento=  precio_compra - precio_compra* 15/100
print(f"El precipo final es de {descuento}")
