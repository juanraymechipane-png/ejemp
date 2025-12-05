n1= float(input("Digite un numero: "))
n2= float(input("Digite un numero: "))

operacion = input("Digite la operacion: ").lower()

if operacion=="s":
    suma= n1 + n2
    print(f"\nLa suma es: {suma}")

elif operacion=="r":
    resta = n1 - n2
    print(f"\nLa resta es: {resta}")
elif operacion== "m":
    multi= n1*n2
    print(f"\nLa multiplicacion es: {multi}")
elif operacion=="d":
    divi=n1/n2
    print(f"\nLa division es: {divi}")
else:
    print("\nSe equivoco de operacion: ")



