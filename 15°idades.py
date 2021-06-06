tem18 = 0
maior18 = 0
menor18 = 0
soma = 0
media = 0
maior = 0
menor = 0
maioresIdades = 0
menoresIdades = 0
numeroIdade = int(input("Digite a quantidade de idades que deseja ler: "))
for i in range(0,numeroIdade):
    idade = int(input("Digite a idade?"))
    if idade == 18:
        tem18 +=1
    elif idade < 18:
        menor18 +=1
    elif idade > 18:
        maior18 +=1
    soma +=idade
    media = soma / numeroIdade
    if idade > idade:
        maior = idade
        maioresIdades +=1
    elif idade < idade:
        menor = idade
        menoresIdades +=1
print(f'{tem18} pessoas têm 18 anos\n{menor18} Pessoas são menores de 18 anos.\n{maior18} Pessoas são maiores de 18 anos.\nA SOMA das idades é {soma} e a média das idades é {media}\nMaior idade: {maior} e {maioresIdades} pessoas têm essa idade') 

