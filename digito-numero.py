"""Faça uma função que informe a quantidade de dígitos de um determinado
número inteiro informado."""

def quantidade_digitos(numero):
    numero = abs(numero)
    return len(str(numero))