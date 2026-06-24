import os
os.system("cls")
dic = {}
# Atvidade 1
frase = str(input("Informe a frase: "))
def conta(frase):
    l = list(frase)
    for letra in l:
        if letra != " ":
            if letra in dic:
                dic[letra] += 1
            else:
                dic[letra] = 1
conta(frase)
print(f"\nDicionário\n{dic}")

# Atividade 2
dicionario = {}
script = str(input("Informe o script: ")).lower()
script = script.split()
for palavra in script:
    if palavra != " ":
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
print(f"\nDicionário\n{dicionario}")
