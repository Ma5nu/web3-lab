#Informe se a sequência de número está como decrescente ou crescente

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 < num2 and num2 < num3:
    print("A sequência está em ordem crescente")
else:
    print("A sequência não está em ordem crescente")