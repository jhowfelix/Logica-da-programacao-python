salarioBruto = float(input("Digite o salário bruto: "))
prestacao = float
porcentualsalario  = 30 * salarioBruto / 100

if salarioBruto > 0:
    if(prestacao <=  porcentualsalario):
        prestacao = float(input("Digite o valor da prestação: "))
        print("Aceitar")
    else:
        print("Não aceitar")
else:
    print("salário inválido:")
