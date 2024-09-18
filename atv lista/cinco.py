num = []
cont=1
while cont <=5:
    n = int(input("Informe um número: "))
    num.append(n)
    cont = cont+1

print(num)

for valor in num:
   if valor % 3 == 0:
       print(valor)

       