print("Bem vindo a companhia 1TDSJ, a MELHOR de todas!")


print("NOSSAS OPÇÕES SÃO: ")

print("\nNorte\nNordeste\nCentro-Oeste")  
print("Opcão A: Norte SOMENTE ida R$ 280")
print("Opção B: Norte ida e volta R$ 400 \n")
print("Opção C: Nordeste SOMENTE ida R$ 380")
print("Opção D: Nordeste ida e volta R$ 628 \n")
print("Opção E: Centro-Oeste SOMENTE ida R$ 620" )
print("Opção F: Centro-Oeste ida e volta R$ 1100")

escolhaDoCliente = input("Por favor, selecione a passagem que queira comprar: ").upper()


if(escolhaDoCliente == 'A'):
    print("Parabéns, você acaba de comprar uma passagem (SOMENTE de ida) para o Norte.") 
elif (escolhaDoCliente == 'B'):
    print("Parabéns, você acaba de comprar uma passagem  (de ida e volta) para o Norte.")
elif (escolhaDoCliente == 'C'):
    print("Parabéns, você acaba de comprar uma passagem (SOMENTE de ida) para o Nordeste.")
elif(escolhaDoCliente == 'D'):
    print("Parabéns, você acaba de comprar uma passagem (ida e volta) para o Nordeste.")
elif(escolhaDoCliente == 'E'):
    print("Parabéns, você acaba de comprar uma passagem (SOMENTE de ida) para o Centro-Oeste.")
elif (escolhaDoCliente == 'F'):
    print("Parabéns, você acabou de comprar uma passagem (de ida e volta) para o Centro-Oeste.")
else:
    print("Nem temos essa opção oh zé")