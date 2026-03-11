total = float(input("Digite o valor total da conta: "))

valor_por_pessoa = total / 3

carlos = int(valor_por_pessoa)
andre = int(valor_por_pessoa)
felipe = valor_por_pessoa - (carlos +andre)
print (f"Carlos deve pagar: R${carlos:.2f}")
print (f"André deve pagar: R${andre:.2f}")
print (f"Felipe deve pagar: R${felipe:.2f}")

