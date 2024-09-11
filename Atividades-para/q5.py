import random
contagem = [0, 0, 0, 0, 0, 0]
for _ in range(10):
    lancamento = random.randint(1, 6)
    contagem[lancamento - 1] += 1
for num in range(6):
    print(f"Valor {num + 1}: {contagem[num]} vez(es)")