"""7. Ingresa el precio de lista de un producto,
luego calcula el monto de igv (18%). Muestra en pantalla el monto de igv y el importe a pagar (precio de lista + monto de igv).
"""
precio_lista= float(input("Ingrese el precio de lista del producto: "))

igv_producto= round(precio_lista*18/100,1)
total_pagar= round(precio_lista*18/100+precio_lista,1)

print(f"El igv del producto es: S/{igv_producto}")
print(f"El total a pagar es: S/{total_pagar}")