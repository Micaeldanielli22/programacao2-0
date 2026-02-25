#insira a altura de uma pessoa 
# sexo desta pessoa(M ou F )
# M peso ideal 72,7
# F 
h = float(input("digite a altura em centimetros"))
       
sexo = (input("digite o seu sexo (sexo(m ou f)")) 
if sexo == "M":
    peso_ideal = (72.7*h) - 58
    print("para homens o peso ideal e ",peso_ideal)   
elif sexo == "F": 
    peso_ideal=(62.1*h) - 44.7
    print("para mulheres o peso ideal e ",peso_ideal)   
else:
    print("sexo invalido por favor insira M")