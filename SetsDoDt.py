import os
os.system("cls")

# Atividade 1

frase = str(input("Informe a frase: ")).lower()
print(sorted(set(frase)))

# Atividade 2
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6, 7]
def compara(l1, l2):
    for elemento in range(len(l2)):
        if l2[elemento] in l1[0:len(l1)]:
            return True
        else:
            return False
print(compara(l1, l2))

# Atividade 3
turmas = [{'ações comunitárias', 'futebol', 'música', 'rugby'},
     {'ações comunitárias', 'música', 'rugby', 'teatro'},
     {'música', 'rugby', 'teatro', 'vôlei'},
     {'música', 'vôlei', 'rugby'},
     {'ações comunitárias', 'futebol', 'rugby', 'teatro', 'vôlei'},
     {'ações comunitárias', 'futebol', 'rugby'},
     {'ações comunitárias', 'rugby', 'teatro', 'vôlei'},
     {'ações comunitárias', 'rugby', 'teatro', 'vôlei'},
     {'ações comunitárias', 'rugby', 'vôlei'}]

atividade = turmas[0]
for turma in turmas[1:len(turmas)]:
    atividade = atividade.intersection(atividade)
print(atividade)

# Atividade 4

A = [1, 4, 5, 7, 9]
B = [4, 5, 7, 9, 10]

for elemento in range(len(A)):
    if A[elemento] not in B[0:len(B)]:
        print(A[elemento], "Lista B")
for elemento in range(len(A)):
    if B[elemento] not in A[0:len(A)]:
            print(B[elemento], "Lista A")

# Atividade 5
alfabeto = set("abcdefghijklmnopqrstuvwxyz")
frase2 = str(input("Informe a str: ")).lower()
letras = set()
def checa(frase2):
    for i in range(len(frase2)):
        if frase2[i] in alfabeto:
            letras.add(frase2[i])
    if letras == alfabeto:
        print("Panagrama")
    else:
        print("Não é Panagrama")
checa(frase2)
