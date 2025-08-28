''' Conte quantas vezes o número 5 aparece em uma lista de 10 números aleatórios entre 1 e 10. '''
import random

lista = [random.randint(1, 10) for _ in range(10)]
contador = lista.count(5)
print(f'O número 5 aparece {contador} vezes na lista aleatória: {lista}')