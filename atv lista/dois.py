temp = []
mes = 1
meses =[]
mesex=[]
ext = ""
soma=0
while mes<=12:
    ext= input("informe o mês: ")
    mesex.append(ext)
    tmed= float(input(f"informe a temperatura média do mês {mes}: "))
    temp.append(tmed)
    mes= mes+1
    soma =  soma+tmed
   

media = soma/12
cont=0
print(temp)
for cont in range(0,11):
    if temp[cont]>media:
        print(f"a média do mês {mesex[cont]} foi de {temp[cont]}")
    else:
        print("NEnhuma")


   


