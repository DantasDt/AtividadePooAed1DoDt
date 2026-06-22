import os
os.system("cls")
from random import *
# Atv1
pares = []
impares = []
p = int(input("Informe a quantidade de numeros: "))
if p < 0 or p < 4:
    print("Valor inválido!")
else:
    lista = []
    for i in range(0, p):
        num = int(input("Numero: "))
        lista.append(num)

    print(f"Lista completa\n{lista}")
    print(f"\nTrês primeiros\n{lista[0], lista[1], lista[2]}")
    print(f"2 ultimos\n{lista[p - 2], lista[p - 1]}")
    lista.reverse()
    print(f"Lista Invertida\n{lista}")

for i in range(0, p):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])
    print(f"Pares\n{pares}")
    print(f"Impares\n{impares}")    

# Atv 2
q = int(input("Informe a quantidade de urls: "))
urls = []
urlsC = []
for i in range(0, q):
    u = str(input("Informe a url: "))
    urls.append(u)
    urlsC.append(f"www.{u}.com")
print(urls)
print(urlsC)

# Atv 3

numeros = []
soma = 0
media = 0
for i in range(100):
    num = randint(-100, 100)
    numeros.append(num)
    soma += num
media = soma / 100
ord = sorted(numeros)
print(f"Lista original\n{ord}")
print(f"Lista Normal\n{numeros}")
print(f"Indice maior {numeros.index(max(numeros))}")
print(f"Indice menor {numeros.index(min(numeros))}")
print(f"Soma {soma}")
print(f"Média {media}")