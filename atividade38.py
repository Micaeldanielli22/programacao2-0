ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade_anos = ano_atual - ano_nascimento

idade_meses = idade_anos * 12
idade_semanas = idade_anos * 52
idade_dias = idade_anos * 365

print("\nIdade da pessoa:")
print(f"Em anos: {idade_anos}")
print(f"Em meses: {idade_meses}")
print(f"Em semanas: {idade_semanas}")
print(f"Em dias: {idade_dias}")