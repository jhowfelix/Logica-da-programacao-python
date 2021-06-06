notaLaboratorio = float(input("Digite a nota:")) 
notaAvaliacaoSemestreal  =  float(input("Digite a nota:"))
notaExameFinal = float(input("Digite a nota:"))

if notaLaboratorio < 0 or notaLaboratorio > 10:
    print("Numero 2inválido.")
elif notaAvaliacaoSemestreal < 0 or notaAvaliacaoSemestreal > 10:
    print("Numero inválido.")
elif notaExameFinal < 0 or notaExameFinal > 10:
    print("Numero inválido.")


media = (notaLaboratorio + notaAvaliacaoSemestreal + notaExameFinal) / 3


if media > 10 or media < 0:
    print("Nota inválida")
elif media > 8 and media <= 10.0:
    print("A")
elif media >= 7 and media <= 7.9:
    print("B")
elif media >= 6 and media <= 6.9:
    print("C")
elif media >= 5 and media <= 5.9:
    print("D")
elif media >= 0 and media <= 4.9:
    print("0.0")
