num = []
cont=1
while cont <=6:
    n = int(input("Informe um número: "))
    num.append(n)
    cont = cont+1

print(num)
jj=1
while jj<=2:
    escolha = int(input("informe; "))
    print(num[escolha])
    jj=jj+1

    soma=num[escolha]+num[escolha]
    dif =num[escolha]-num[escolha]
    div =num[escolha]/num[escolha]
    mult= num[escolha]*num[escolha]
    exp=num[escolha]**num[escolha]

print (f"A soma {soma}\n A multi{mult}\n A div {div} A dif {dif} A exp{exp} dos dois")




