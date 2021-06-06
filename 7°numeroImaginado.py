chances = 0
numero = 50
chuteNumero = int(input("Chute numero: "))
while chuteNumero != numero:
    chances +=1
    if chuteNumero < numero:
        print("*** CHUTOU BAIXO ***")
        chuteNumero = int(input("Chute numero: "))
    elif chuteNumero > numero:
        print("*** CHUTOU ALTO ***")
        chuteNumero = int(input("Chute numero: "))
print(f'*** ACERTOU! PARABÉNS! VOCÊ PRECISOU DE {chances} CHANCES ***')

    