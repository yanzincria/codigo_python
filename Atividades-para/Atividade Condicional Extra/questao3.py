valor = int(input("Digite a sua idade: "))

if valor<12:
    print(f"Você é uma criança \n")
elif valor>=12 and valor <18:
    print(f"Você é um(a) adolescente \n")
elif valor>=18 and valor <60:
    print(f"Você é um(a) adulto(a) \n")
if valor>60:
    print(f"Você é um(a) idoso(a) \n")
