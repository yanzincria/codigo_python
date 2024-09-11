a = int(input("Digite o primeiro número inteiro positivo (a): "))
b = int(input("Digite o segundo número inteiro positivo (b): "))

contador = 0

if a>b:
    a, b = b, a

for numero in range (a,b + 1):
    if numero % 7 == 0 and numero % 12 == 0:
        contador += 1

print(f"O total de números entre {a} e {b} que são múltiplos de 7 e 12 simultaneamente é: {contador}")