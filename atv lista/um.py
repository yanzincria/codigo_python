lista =[]
finalizar =0

while finalizar >=0:
   valor= int(input("informe um valor: "))
   if valor>=0:
      lista.append(valor)
   elif valor<0:
      finalizar= -1
      print("programa finalizado")
print(lista)
for valor in lista:
   if valor % 2 == 0:
      lista.remove(valor)
      print(lista)
   else:
      print(lista)
    
   