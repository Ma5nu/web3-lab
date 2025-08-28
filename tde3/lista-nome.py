''' Crie uma lista de 4 nomes e verifique se "Maria" está na lista.'''
lista_nomes = ['Bia', 'Julia', 'Bianca', 'Maria']

for elemento in lista_nomes:
    if elemento == 'Maria':
        print('Maria está na lista!')
        break
else:
        print('Maria não está na lista!')
        
