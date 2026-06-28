import os
os.system("Cls")

# Atividade 1
def Calcula(dimensao):
    area = dimensao[0] * dimensao[1]
    perimetro = 2 * (dimensao[0]) + (2 * (dimensao[1]))
    return area, perimetro

largura = int(input("Informe a largura: "))
comprimento = int(input("Informe o comprimento: "))
dimensao = (largura, comprimento)
print(Calcula(dimensao))

# Atividade 2
frase = str(input("Informe a frase: "))
for indice, letra in enumerate(frase):
    print(indice, letra)

# Atividade 3
n = int(input("Informe o numero de alunos: "))
alunos = []
for aluno in range(n):
    nome = input("Informe o nome: ")
    nota = float(input("Informe a nota: "))
    alunos.append((nome, nota))

print(sorted(alunos, key=lambda aluno: aluno[1], reverse=True))

# Atividade 4
resultado = {} 
def comprimir(tuplasOri):
    for tupla in tuplasOri:
        if tupla[0] in resultado:
            resultado[tupla] += tupla[1]
        else:
            resultado = tupla

tuplasOri = [('maçã', 3), ('banana', 2), ('maçã', 5), ('laranja', 1), ('banana', 3)]
comprimir(tuplasOri)
print(resultado)

# A finalizar
