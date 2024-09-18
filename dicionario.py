#criando um  dicionário, é basicamente uma lista com indice textual

pessoa ={
    'Nome':'Maria',
    'Idade': 20,
    'Endereço': 'Avenida 23'
} 
print(pessoa)

#exibindo as chaves utilizando o comando keys()
print(pessoa.keys())

#exibindo os valores utilizando values()
print(pessoa.values())

#exibindo tanto a chave quanto o valor
print(pessoa.items())

for chave, valor in pessoa.items():
    print(f"{chave} : {valor}")
                                

#realizando operações
#adicionando dados
#forma 1
pessoa["Peso"] = 68
print(pessoa)

#Forma 2 usando update()
pessoa.update({"Profissão":"Diretora"})

#removendo dados do dicionario
#forma 1 - pop()
pessoa.pop("Peso")
print(pessoa)
#forma dois del()
del(pessoa["Endereço"])
print(pessoa)
