numero = int(input("Digite a tabuada que deseja ver: "))
# VALIDAÇÃO
while numero <=0:
    numero = int(input("Tabuada inválida. Digite outra acima de 0: "))

for i in range(0,11):
    mult = numero * i
    print(f'{numero} X {i}: {mult}')
ch = input("Deseja continuar ou encerrar?").lower()
while ch == "continuar":
    numero = int(input("Qual tabuada deseja ver dessa vez? "))
    for i in range(0,11):
        mult = numero * i
        print(f'{numero} X {i}: {mult}')
    ch = input("Deseja continuar ou encessar?").lower()
else:
    print("OK, PROGRAMA FINALIZADO!")