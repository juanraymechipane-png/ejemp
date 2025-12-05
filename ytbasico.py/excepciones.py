# EXCEPCIONES


try:
    print(dasas)
except NameError as error:
    print('error de tipo NameError')
    print(error)
    
except TypeError:
    print('error de tipo TypeError')
else:
    print('Hola mundo')
finally:
    print('final')

