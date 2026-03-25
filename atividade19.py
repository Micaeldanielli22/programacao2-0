
quantidade_de_frangos = int(input("Digite a quantidade de frangos: "))


preço_anel_chip_frango = 4.00
preço_anel_alimento_frango = 7.00
CUSTO_POR_FRANGO = preço_anel_chip_frango + (2 * preço_anel_alimento_frango)
    
CUSTO_TOTAL = quantidade_de_frangos * CUSTO_POR_FRANGO

print(f"Quantidade de frangos: {quantidade_de_frangos}")
print(f"Custo por frango: R$ {CUSTO_POR_FRANGO:.2f}")
print(f"Gasto total da granja: R$ {CUSTO_TOTAL:.2f}")
        
  
