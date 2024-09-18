num = []
cont=1
while cont <=6:
    n = int(input("Informe um número: "))
    num.append(n)
    cont = cont+1

print(num)
jj=1

escolha = int(input("informe: "))
escolha2 = int(input("informe: "))
    #print(num[escolha])


soma=num[escolha]+num[escolha2]
dif =num[escolha]-num[escolha2]
div =num[escolha]/num[escolha2]
mult= num[escolha]*num[escolha2]
exp=num[escolha]**num[escolha2]

print (f"A soma {soma}\n A multi{mult}\n A div {div} A dif {dif} A exp{exp} dos dois")




