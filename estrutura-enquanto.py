#1ª forma de utilizar while - semelhante ao for
contador = 1
while contador<=5:
    print(contador)
    contador = contador+1 #é o mesmo que contador +=1
print("="*40)
#2ª forma de utilizar enquanto - loop condicional normal 

valor = 0

while valor >=0:
    valor = int(input("Informe um valor qualquer(digite um valor negativo para terminar: )"))

    print(f"Você digitou {valor}")

print("="*40)
#3ª forma de utilizar enquanto - semelhante a estrutura faça enquanto

while True:
    senha = input("Informe sua senha: ")

    if senha == "123":
        print*("parabens, senha correta")
        break #forma de encerrar o loop
    else:
        print("senhas não conferem, tente novamente")