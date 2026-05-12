preco = float(input("Digite o preço do produto: R$ "))
desconto = preco * 0.10
novo_preco = preco - desconto
print(f"Preço original: R$ {preco}")
print(f"Desconto (10%): R$ {desconto}")
print(f"Novo preço: R$ {novo_preco}")