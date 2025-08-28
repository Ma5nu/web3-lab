''' Crie uma lista de números de 1 a 10 e filtre os múltiplos de 3.'''
lista_numero = [1,2,3,4,5,6,7,8,9,10]
lista_filtro = []

for numero in lista_numero:
    if numero % 3 == 0:
        lista_filtro.append(numero)
print(lista_filtro)