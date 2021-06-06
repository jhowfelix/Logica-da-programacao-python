nomes_pares = []
nomes_impares = []
notas_pares = []
notas_impares = []
alunos_impares = 1
alunos_pares = 2
for i in range(0,3):
    print("VOCE ESTÁ DIGITANDO A NOTA DOS ALUNOS IMPARES")
    nomes_impares.append(input("Digite o nome do aluno: "))
    print("POR FAVOR, INSIRA A NOTA DO ALUNO NÚMERO ",alunos_impares)
    notas_impares.append(float(input("NOTA --->")))    
    alunos_impares +=2
    if notas_impares[i] < 0 or notas_pares[i] > 10:
        print("NOTA INVÁLIDA!")
        print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES. DIGITE A NOTA NOVAMENTE: ",alunos_impares)
        notas_impares.append((float(input("NOTA --->"))))

for i in range(0,3):
    print("VOCE ESTÁ DIGITANDO A NOTA DOS ALUNOS PARES: ")
    nomes_impares.append(input("Digite o nome do aluno: "))
    print("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO ",alunos_pares)
    notas_impares.append(float(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES. DIGITE A NOTA: ",alunos_pares)))
    if notas_pares[i] < 0 or notas_pares > 10:
        print("NOTA INVÁLIDA!")
        notas_impares.append(float(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES. DIGITE A NOTA NOVAMENTE: ",alunos_pares)))

media_pares = sum(notas_pares) / len(notas_pares)
media_impares = sum(notas_impares) / len(notas_impares)

for i in range(0,3):
    if notas_impares[i] > 9 or notas_pares[i] > 9:
        print(f'{nomes_pares[i]}, {nomes_impares[i]} ficaram com notas acima de 9')
    elif notas_impares[i] < 6 or notas_impares[i] < 6:
        cont = 0
        cont +=1
print(f'{cont} ficaram com notas abaixo de 6.')
if media_pares > media_impares:
    print("Alunos pares possuem média maior.")
elif media_impares > media_pares:
    print("Alunos impares possuem média maior.")
elif media_impares == media_pares or media_pares == media_impares:
    print("A média de ambas as turmas são a mesma.")