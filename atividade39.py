






salario = 1200.00
conta1 = 200.00
conta2 = 120.00
multa = 0.02  # 2%


valor_c1 = conta1 + (conta1 * multa)
valor_c2 = conta2 + (conta2 * multa)


total_contas = valor_c1 + valor_c2

restante = salario - total_contas

print(f"Valor da conta 1 com multa: R$ {valor_c1:.2f}")
print(f"Valor da conta 2 com multa: R$ {valor_c2:.2f}")
print(f"Total a pagar: R$ {total_contas:.2f}")
print(f"Salário restante: R$ {restante:.2f}")