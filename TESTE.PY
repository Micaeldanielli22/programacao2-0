import random

class Fazenda:
    def __init__(self):
        self.dinheiro = 50
        self.dia = 1
        self.tamanho = 9
        self.terreno = [" "] * self.tamanho

    def mostrar_fazenda(self):
        print("\n🌾 FAZENDA - Dia", self.dia)
        print("💰 Dinheiro:", self.dinheiro)
        print("-----------------")
        for i in range(0, self.tamanho, 3):
            print("|", self.terreno[i], "|", self.terreno[i+1], "|", self.terreno[i+2], "|")
        print("-----------------")

    def plantar(self, pos):
        if self.terreno[pos] == " ":
            if self.dinheiro >= 5:
                self.terreno[pos] = "🌱"
                self.dinheiro -= 5
                print("Você plantou uma semente!")
            else:
                print("Dinheiro insuficiente!")
        else:
            print("Terreno já ocupado!")

    def regar(self, pos):
        if self.terreno[pos] == "🌱":
            self.terreno[pos] = "🌿"
            print("A planta está crescendo!")
        else:
            print("Nada para regar aqui!")

    def colher(self, pos):
        if self.terreno[pos] == "🌿":
            self.terreno[pos] = " "
            ganho = random.randint(10, 20)
            self.dinheiro += ganho
            print(f"Você colheu e ganhou 💰 {ganho}!")
        else:
            print("Nada para colher aqui!")

    def passar_dia(self):
        self.dia += 1
        print("🌞 Um novo dia começou!")

def menu():
    print("\n1 - Plantar (5💰)")
    print("2 - Regar")
    print("3 - Colher")
    print("4 - Passar dia")
    print("0 - Sair")

def main():
    jogo = Fazenda()

    while True:
        jogo.mostrar_fazenda()
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            print("Obrigado por jogar! 🌾")
            break

        elif escolha in ["1", "2", "3"]:
            try:
                pos = int(input("Escolha posição (0-8): "))
                if pos < 0 or pos > 8:
                    print("Posição inválida!")
                    continue
            except:
                print("Entrada inválida!")
                continue

            if escolha == "1":
                jogo.plantar(pos)
            elif escolha == "2":
                jogo.regar(pos)
            elif escolha == "3":
                jogo.colher(pos)

        elif escolha == "4":
            jogo.passar_dia()

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()