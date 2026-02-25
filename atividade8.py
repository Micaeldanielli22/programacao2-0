contador = 1
soma_notas = 0
while contador <=3:
    nota = float(input(f"insira a nota do {contador} aluno"))
    if nota < 0  or nota > 10:
        print("nota invalida . a nota dever estar entre 0 e 10")
        continue
    soma_notas  += nota
    contador +=1 
media = soma_notas/3
print("a media das 3 notas e: ",media)
