num = []
cont=0

while cont <=9:
    n = int(input("Informe um número: "))
    num.append(n)
    cont = cont+1
   

    

jj=0
for jj in range(0,9):
    if num[jj] == 3:
        print(jj)
    