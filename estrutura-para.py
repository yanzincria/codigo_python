'''
Este código é uma representação do que acontece na maioria das linguagens deprogramação

for(contador=1; contador<=5; contador++){

}
'''

#1ª forma de operação do for
for contador in range(1,6):
    print(contador)

print("-"*40)
#2ª forma de operação do for
for contador in range(1,11,2):# o 3ª parâmetro indica como os valores serão incrementados(alteraçãp de valor)
    print(contador)


print('-'*40)
#3ª forma de operação do for
for contador in range(10,0,-1):
    print(contador,end=" ")# a função end informa como os valores serão exibidos ao final, por padrão é dado um enter(\n)

