moedas_1_centavos = int(input("digite a quntidadede moedas de 1 centavo"))
moedas_5_centavos = int(input("digite a quntidadede moedas de 5 centavo"))
moedas_10_centavos = int(input("digite a quntidadede moedas de 10 centavo"))
moedas_25_centavos = int(input("digite a quntidadede moedas de 25 centavo"))
moedas_50_centavos = int(input("digite a quntidadede moedas de 50 centavo"))
moedas_1_real = int(input("digite a quntidadede moedas de 1 real"))
tatais_reais = (moedas_1_centavos * 0.01 ) + \
    (moedas_5_centavos * 0.05 ) + \
    (moedas_10_centavos * 0.10 ) + \
    (moedas_5_centavos * 0.25)  + \
    (moedas_10_centavos * 0.50 ) + moedas_1_real
print("o valor total em reais e",tatais_reais)