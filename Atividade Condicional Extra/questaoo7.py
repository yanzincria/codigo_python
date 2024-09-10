nota = float(input("Digite a nota final do aluno: "))
frequencia = float(input("Digite a frequência do aluno (em %): "))

if nota>=7 and frequencia>=75:
    print("O aluno está aprovado.")
else:
    print("O aluno está reprovado. ")