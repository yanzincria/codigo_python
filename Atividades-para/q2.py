quantidade_negativos = 0
soma_positivos = 0

for contador in range(8):
    numero = int(input(f"Digite o {contador+1}° número: "))
    if numero < 0:
        quantidade_negativos += 1
    else:
        soma_positivos += numero

print(f"Quantidade de números negativos: {quantidade_negativos}")
print(f"Soma dos números positivos: {soma_positivos}")