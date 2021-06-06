num1 = int(input("Digite o 1° numero: "))
num2 = int(input("Digite o 2° numero: "))

if num1 > num2:
    print(f"{num1} é maior")
elif num1 == num2:
    print("Numeros iguais.")
else:
    print(f"{num2} é maior")