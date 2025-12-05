# 1. Ingresa una cantidad en dólares, luego calcula y muestra el equivalente en soles.

cant_dolares = float(input("Ingresa la cantidad de dolares: "))

conver_soles= round( cant_dolares * 3.48,1)

print(f"La conversion a soles es: {conver_soles} soles")


# 2. Elabora un programa que permita calcular y mostrar el área de un círculo de cualquier radio. (área = π*r**2).

radio_cir= float(input("Ingrese la radio del circulo: "))
import math
area_cir= round(math.pi*radio_cir**2,1)

print(f"El area del circulo es: {area_cir} metros cuadrados")


# 3. Ingresa 2 números enteros (a y b), luego calcula y muestra el resultado de a/b.

num_a=int(input("Ingrese el primer numero: "))
num_b=int(input("Ingrese el segundo numero: "))

resultado= round(num_a/num_b,1)

print(f"El resultado es: {resultado}")


# 4. Ingresa un número que tenga parte entera y parte decimal. Luego muestra sólo la parte entera de dicho número.

num= float(input("Ingrese un número que tenga parte entera y parte decimal: "))

resulta= round(num //1)
print(f"La parte entera es: {resulta}")

'''
5. Un supermercado va a realizar un sorteo navideño. 
Por cada S/.50 en compras el cliente recibe un cupón para participar en el sorteo. Elabora un programa que permita ingresar el monto de la compra, 
luego determine y muestre la cantidad de cupones que debe recibir.
'''

cant_compra = float(input("Ingrese el total de su compra: "))
cupones= round(cant_compra/50)

print(f"La cantidad de cupon que tiene usted es: {cupones}")

# 6. Ingresa la cantidad de alumnas y alumnos de un salón de clase. Luego muestra el porcentaje de varones y el porcentaje de mujeres.

cant_var=int(input("Ingrese la cantidad de alumnos: "))
cant_muj=int(input("Ingrese la cantidad de alumnas: "))

por_var = cant_var/(cant_muj+ cant_var) * 100
por_muj= cant_muj/(cant_muj + cant_var) * 100

print(f"El porcentaje de mujeres es: {por_var}")
print(f"El porcentaje de varones es: {por_muj}")








