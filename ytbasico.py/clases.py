# CLASES

class unHumano:
    def __init__(self, altura, edad, peso):
        self.altura= altura
        self.edad= edad
        self.peso= peso

    def comer(self):
        print(f'el humano de {self.edad}')

humano_1= unHumano(1.80,23,87)
print(f'el humano 1 mide {humano_1.altura}, pesa {humano_1.peso}kg y tiene {humano_1.edad}años')


print(humano_1.altura)