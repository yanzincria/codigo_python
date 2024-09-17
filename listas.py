animais = ["Cachorro","Gato","Ovelha"]
print(type(animais))#exbindo o tipo da variável

print(animais)

#Exibindo todos os itens da lista
print("+"*50)
for itens in animais:
    print(itens)

#1ª Etapa: Atualizar dados
print("-"*50)
animais[0] = 'Coelho'
print(animais)

#2ª Etapa: Inserir dados
print('-'*50)

#Forma 1 - Usando append
animais.append("Cavalo")#irá inserir um novo item no final da lista
print(animais)

#Forma 2 - Usando Insert
animais.insert(1, "Carcará")# O inpert precisa de 2 valores, o 1° será o índice que desejo inserir o valor. O 2º é o conteudo que quero inserir na lista
print(animais)

#3ª Etapa: Excluir dados 
print("-"*50)
#Forma 1 - usando pop()
animais.pop()#Remove o último item da lista
print(animais)
#forma 2 - usando pop() com indice
animais.pop(0)#Aqui iremos escolher qual indice da lista será excluido 
print(animais)
#forma 3 - usando remove
animais.remove("Ovelha")# irá remover o item pelo seu conteúdo
print(animais)