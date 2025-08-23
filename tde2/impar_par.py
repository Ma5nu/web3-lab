num = int(input("Digite um número> "))

impar = 0
par = 0

for i in range(1, num):
    if i % 2 == 0:
        par +=1
    else:
        impar +=1   

    print(f"Entre 1 e {num}, há {impar} números ímpares e {par} números pares.")
 