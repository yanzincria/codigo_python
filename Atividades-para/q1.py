for cont in range(1, 51):
    # Verifica se o número é múltiplo de 3 e 5
    if cont % 3 == 0 and cont % 5 == 0:
        print("FizzBuzz")
    # Verifica se o número é múltiplo de 3
    elif cont % 3 == 0:
        print("Fizz")
    # Verifica se o número é múltiplo de 5
    elif cont % 5 == 0:
        print("Buzz")
    # Se não for múltiplo de 3 nem de 5, imprime o próprio número
    else:
        print(cont)