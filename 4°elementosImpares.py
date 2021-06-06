num1 = int(input("Digite o 1° numero: "))
num2 = int(input("Digite o 2° numero: "))
impares = 0
for i in range(num1, num2):
    if i % 2 != 0:
        impares +=1
print(impares)