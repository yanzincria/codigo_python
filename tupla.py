objetos = ('Lápis', 'borracha', 'Caderno')
print(objetos[1]) #Irei exibir o item na posição 1, ou seja segunda posição, uma vez que toda coleção começa na posição zero.

print(type(objetos))# irá mostrar o tipo da variável.

print(objetos) #exi,bindo todos os intens de uma sá vez.

print("-"*50)
for item in range(0,3):
    print(objetos[item], end =",")# exibindo todos os itens da tupla!

# Exibindo todos os itens da tupla sem a função range!
print("")
print('-'*50)
for elementos in objetos:
    print(elementos)

# Iremos tenatr alterar o conteúdo da tupla
objetos[0] ="Caneta"