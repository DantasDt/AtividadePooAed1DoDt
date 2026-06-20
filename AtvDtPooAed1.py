# Atividade 1
n1 = str(input("Informe o primeiro nome: "))
n2 = str(input("Informe o sobrenome: "))
print(n1, n2)

# Atividade 2
frase = input("Frase: ").count(" ")
print(frase)

# Atividade 3
frase = input("Frase: ")
for letra in range(len(frase) + 1):
    print(frase[:letra])

# Atividade 4
n = input("numero: ")
num = []
num.append(n)
if len(n) == 8:
    n = "9" + n
num = []
num.append(n)
if n[5] != "-":
    n = n[:5] + "-" + n[5:]

print(n)

# Atividade 5
frase = input("Frase: ").lower()
quant = 0

for letra in range(len(frase)):
    if frase[letra] in "aeiou":
        quant += 1
        print(frase[letra], letra)

print(quant)
