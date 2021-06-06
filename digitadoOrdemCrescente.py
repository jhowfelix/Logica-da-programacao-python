a= int(input("Digite 1° numero: "))
b= int(input("Digite 2° numero: "))
c= int(input("Digite 3° numero: "))

if a <= b and a <= c and b <= c:
    print(f"Foi digitado em ordem crescente \n {a} \n {b} \n {c}")
elif a <= b and a <=c and c <= b:
    print(f"Foi digitado em ordem crescente \n {a} \n {c} \n {b}")
elif b <= a and b <= c and a <= c:
    print(f"Foi digitado em ordem crescente \n {b} \n {a} \n {c}")
elif b <= a and b <= c and c <= a:
    print(f"Foi digitado em ordem crescente \n {b} \n {c} \n {a}")
elif c <= a and c <= b and a <=b:
    print(f"Foi digitado em ordem crescente \n {c} \n {a} \n {b}")
elif c <= a and c <= b and b <= a:
    print(f"Foi digitado em ordem crescente \n {c} \n {b} \n {a}")
else:
    print("Não foi digitado em ordem crescente") 
