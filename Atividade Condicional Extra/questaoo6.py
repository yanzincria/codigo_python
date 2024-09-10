valor = float(input("Informe o valor da compra R$: "))
parcela = float(input("\nInforme a quantidade de parcelas: \n Até 24 parcelas "))
valorP= valor/parcela 
if parcela>12:
    valor = valor*0.015
    valorP= valorP+6
    print(f"o valor final da compra foi de R$: {valor} \n Em parcelas de R$: {valorP :.2f}")
else:
    print(f"o valor final da compra foi de R$: {valor} \n Em parcelas de R$: {valorP :.2f}")
