horas_normais = float(input("Digite a quantidade de horas normais: "))
horas_extras = float(input("Digite a quantidade de horas extras: "))

valor_hora_normal = 10.00
valor_hora_extra  = 15.00
porcentual_inposto = 0.10

salario_bruto = (horas_normais * valor_hora_normal) + (horas_extras * valor_hora_extra)
salario_inposto = salario_bruto * porcentual_inposto
salario_liquido = salario_bruto - salario_inposto

print("Salário bruto: R$", salario_bruto)
print("Valor do imposto: R$", salario_inposto)
print("Salário líquido: R$", salario_liquido)       