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

# Atividade 3
d1 = {"a" : 1, "b" : 5, "c": 3}
d2 = {"a" : 2, "q" : 4, "d" : 12}
d3 = {}
def mesclar(d1, d2):
    for componente in d1:
        for comp2 in d2:
            if componente == comp2:
                if d1[componente] > d2[comp2]:
                    d3[componente] = d1[componente]
                else:
                    d3[componente] = d2[comp2]
            else:
                d3[componente] = d1[componente]
                d3[comp2] = d2[comp2]

mesclar(d1, d2)
print(f"\nDicionário final\n{d3}")

# Atividade 4
dados = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
chaves_filtradas = ['a', 'c', 'e']
completo = {}
def filtrar_dicionario(dados, chaves_filtradas):
    for componente in dados:
        if componente in chaves_filtradas:
            completo[componente] = dados[componente]

filtrar_dicionario(dados, chaves_filtradas)
print(f"\nCompleto\n{completo}")
