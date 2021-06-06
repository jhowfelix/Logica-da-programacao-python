
soma = 0
contador = 0
i = 0
while i < 4: 
    i +=1
    idade = int(input("Digite sua idade: "))
    while idade < 50 or idade <0:
        print("Idade Inválida. Só aceitamos maiores de 50 anos.")
        idade = int(input("Digite sua idade: "))
    soma +=idade
    contador +=1
media = soma / contador

print(media)   
    
