"""Escreva um programa em Python que receba uma string como entrada e conte o
número de ocorrências de cada palavra na string. O programa deve imprimir um
dicionário onde as chaves são as palavras e os valores são o número de vezes que
cada palavra ocorre na string."""

def contar_ocorrencias(frase):
    frase = frase.strip().lower()
    
    palavras = frase.split()
    
    contagem = {}
    
    for palavra in palavras:
        palavra = palavra.strip(".,!?;:")
        
        contagem[palavra] = contagem.get(palavra, 0) + 1
    
    return contagem

entrada = input("Digite uma frase: ")
resultado = contar_ocorrencias(entrada)
print(resultado)