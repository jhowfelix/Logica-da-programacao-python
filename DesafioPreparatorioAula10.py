# notasPares = int(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DA TURMA PARES: POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x"))
# notasImpares = int(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DA TURMA IMPARES: POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x"))


TURMAPares = []
for i in range(4):
    notasPares = float(input(f"VOCÊ ESTÁ DIGITANDO AS NOTAS DA TURMA PARES: POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO:{i}"))
    TURMAPares.append(notasPares)
    
    
soma = sum(TURMAPares)
quantia = len(TURMAPares)
media = soma / quantia
print(media)
# TURMAImpares = []
# for i in range(25):
#     notasImpar = int(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DA TURMA IMPARES: POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x"))
#     TURMAPares.append(TURMAImpares)
#     print(TURMAPares)


