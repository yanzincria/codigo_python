acima = 0
abaixo = 0
igual = 0

temperaturas = [0]*7

for contador in range(7):
    temperaturas[contador] = float(input(f"Digite a temperatura {contador+1}: "))

media = 33.5
for temp in temperaturas:
    if temp > media:
        acima += 1
    elif temp < media:
        abaixo += 1
    else:
        igual += 1

print(f"Temperaturas acima da média: {acima}")
print(f"Temperaturas abaixo da média: {abaixo}")
print(f"Temperaturas iguais à média: {igual}")