''' Crie uma lista com 5 valores digitados pelo usuário e imprima a lista em ordem inversa.'''
lista = []
for i in range(5):
    valor = int (input(f'Digite o {i+1} valor:]'))
    lista.append(valor)
lista.reverse()
print(lista)