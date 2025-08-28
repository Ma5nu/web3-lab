'''Tente remover um item de uma tupla e explique o erro.'''
tupla = (1, 2, 3, 4)

try:
    #esse código vai gerar um erro 
    tupla.remove(3) 
    print(tupla)
except AttributeError as e:
    print(f'Erro: {e}')
    print("Tuplas são imutaveis e não suportam o método remove() ou nenhum outro tipo de alteração.")

