a = float(input("Escreva o 1° Numero: "))
b = float(input("Escreva o 2° Numero: "))
c = float(input("Escreva o 3° Numero: "))

# Validação
if a == b and b == c and b == a and c == a and c == b and a == c:
    print("OS TRÊS NUMEROS DIGITADOS SÃO IGUAIS.")
# Processamento + saída
if a <= b and a <= c and b <= c:
    print(f"A ordem <crescente é \n {a} \n {b} \n {c}")
elif a <= b and a <=c and c <= b:
    print(f"A ordem <crescente é \n {a} \n {c} \n {b}")
elif b <= a and b <= c and a <= c:
    print(f"A ordem <crescente é \n {b} \n {a} \n {c}")
elif b <= a and b <= c and c <= a:
    print(f"A ordem <crescente é \n {b} \n {c} \n {a}")
elif c <= a and c <= b and a <=b:
    print(f"A ordem <crescente é \n {c} \n {a} \n {b}")
elif c <= a and c <= b and b <= a:
    print(f"A ordem <crescente é \n {c} \n {b} \n {a}") 
