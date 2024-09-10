hora = float(input("Informe a carga horária do funcionário: "))
valorH= float(input("Informe o valor hora: "))

if hora>40:
    extra = hora-40
    valorEx = (extra*0.50)+(valorH*hora)
    print(f"O salário do funcionário é de R$: {valorEx}")
else:
    valorEx= hora*valorH
    print(f"O salário do funcionário é de R$: {valorEx}")