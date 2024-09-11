maior_numero = None

for contador in range(5):
    numero = int(input(f"Digite o {contador+1}° número inteiro: "))

    if maior_numero is None or numero > maior_numero:
        maior_numero = numero

print(f"O maior número informado é: {maior_numero}")
