#DATES

from datetime import datetime
fecha= datetime(2025,3,16,4,2,5)       #para poner una fecha y hora
print(fecha)
print(fecha.second)              # esto solo es imprime el segundo


now = datetime.now()         # te pone la fecha exacta a la actual
print(now)
print(now.minute)            # del actual pero solo imprime el minuto

from datetime import time 
my_time = time(3,4)
print(my_time.minute)       # importar solo el tiempo

from datetime import date
my_date = date.today()        # solo te da el dia actual
print(my_date.day)
                            

new_year = datetime(2026,4,5)
print(new_year-now)        # resta el año que pusimos 2026 menos el actual, y te dice cuanto falta
