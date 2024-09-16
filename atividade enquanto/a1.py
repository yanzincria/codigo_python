num = 0
num = int(input("informe um número: "))
while num>=1:
    
    if 100>=num>10  :
        print(num*num)
        print(num*num*num)
        num = int(input("informe um número: "))   
    elif 10>=num>5:
        print(num*num*num)
        num = int(input("informe um número: "))
    elif num>100:
        print("limite excedido")
        num = int(input("informe um número: "))
    else: 
        num = int(input("informe um número: "))
        print("codigo encerrado")