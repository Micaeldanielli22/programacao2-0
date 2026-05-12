from datetime import datetime

# ===== SISTEMA DE GERENCIAMENTO DE RESERVAS =====

# Preços base
precos = {
    "padrao": 20,
    "vip": 30,
    "camarote": 40
}

# Assentos disponíveis
assentos = {
    "padrao": ["P1", "P2", "P3", "P4", "P5"],
    "vip": ["V1", "V2", "V3"],
    "camarote": ["C1", "C2"]
}

# ===== INÍCIO DO SISTEMA =====

print("====================================")
print(" SISTEMA DE RESERVAS DO CINEMA ")
print("====================================\n")

# Nome do usuário
nome = input("Digite seu nome: ")

# Mensagem de boas-vindas
print(f"\nBem-vindo, {nome}!\n")

# Menu de tipos
print("Tipos de assento disponíveis:")
print("1 - Padrão")
print("2 - VIP")
print("3 - Camarote")

opcao = input("\nEscolha o tipo de assento: ")

# Verificação do tipo
if opcao == "1":
    tipo = "padrao"

elif opcao == "2":
    tipo = "vip"

elif opcao == "3":
    tipo = "camarote"

else:
    print("❌ Opção inválida!")
    exit()

# Solicitar data da reserva
data_str = input("\nDigite a data da reserva (DD/MM/AAAA): ")

try:
    data = datetime.strptime(data_str, "%d/%m/%Y")

except:
    print("❌ Data inválida!")
    exit()

# Descobrir dia da semana
dia_semana = data.weekday()
# 0 = segunda | 6 = domingo

# Preço inicial
preco = precos[tipo]

# Aumento de 20% de sexta a domingo
if dia_semana >= 4:
    preco *= 1.20

# Exibir assentos disponíveis
print(f"\nAssentos disponíveis para {tipo.upper()}:")

for assento in assentos[tipo]:
    print("-", assento)

# Escolha do assento
escolha_assento = input("\nEscolha seu assento: ").upper()

if escolha_assento not in assentos[tipo]:
    print("❌ Assento inválido!")
    exit()

# Perguntar se é estudante
estudante = input("\nVocê é estudante? (s/n): ").lower()

desconto = 0

if estudante == "s":

    # Solicitar credencial
    carteira = input("Digite o número da carteirinha estudantil: ")

    if carteira.strip() == "":
        print("❌ Carteirinha inválida!")
        exit()

    # Descontos
    if tipo == "padrao":
        desconto = 0.10

    elif tipo == "vip":
        desconto = 0.15

    elif tipo == "camarote":
        desconto = 0.20

# Aplicar desconto
valor_desconto = preco * desconto
preco_final = preco - valor_desconto

# ===== RESULTADO =====

print("\n====================================")
print(" RESERVA REALIZADA COM SUCESSO ")
print("====================================")

print(f"Cliente: {nome}")
print(f"Tipo de assento: {tipo.upper()}")
print(f"Assento escolhido: {escolha_assento}")
print(f"Data da reserva: {data_str}")

# Mostrar dia da semana
dias = [
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo"
]

print(f"Dia da semana: {dias[dia_semana]}")

print(f"\nPreço base: R$ {precos[tipo]:.2f}")

if dia_semana >= 4:
    print("Acréscimo fim de semana: 20%")

if desconto > 0:
    print(f"Desconto estudante: {int(desconto * 100)}%")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")

print(f"\n💰 PREÇO FINAL: R$ {preco_final:.2f}")

print("\nObrigado por utilizar nosso sistema!")