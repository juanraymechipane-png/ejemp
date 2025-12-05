#Conjuntos      #no se repiten 

conjunto= set()        #esto es solo para informarle que es un conjunto vacio

conjunto={1,2,3,"Hola",4.560}

conjunto.add(5)                #add ingresa el dato- sin orden
conjunto.add("Adios")

conjunto.discard("Hola")   #discard elimina el valor


print(3 in conjunto)
#si 3 pertenece al conjunto



#conjuntos
a= {1,2,3}
b={3,4,5}

c= {1,2,3,4,5}

print(b.issubset(c))

