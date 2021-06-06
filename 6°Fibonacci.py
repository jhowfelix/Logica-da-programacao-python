termo = int(input("Digite o primeiro termo: "))
cont = 0
i = 0
proximoTermo = 0
termoAtual = 0
while cont < termo:
    cont += 1
    termoAntecedente = termo - 1
    termoAtual += termo + termoAntecedente
    proximoTermo = termoAtual + termoAntecedente
    # while proximoTermo < 21:
    #     proximoTermo = termoAtual + termoAntecedente
print(termoAntecedente, termoAtual, proximoTermo, proximoTermo, proximoTermo)
