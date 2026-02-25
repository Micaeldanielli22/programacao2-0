x1 = float(input("digite a cordenada x do primeiro ponto: "))
y1 = float(input("digite a cordenada y do primeiro ponto: "))
x2 = float(input("digite a cordenada x do segundo plano ponto: "))
y2 = float(input("digite a cordenada y do segundo plano ponto: "))

diferenca_x = x2 - x1
diferenca_y = y2 - y1

distancia = ((diferenca_x ** 2) + (diferenca_y ** 2)) **0.5


print("a distancia entre os pontos ({},{}) e ({},{})é {:.2f} unidades " .format(x1,y1,x2,y2, distancia))