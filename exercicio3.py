  distancia=int(input("Digite a distancia que pretende viajar:"))
if distancia <= 200:
    preco=0.50*distancia
    print("Valor da passagem de curta distancia é R$","%3.2F"%preco)
else:
    preco=0.45*distancia
    print("Valor da passagem de longa distância é R$","%3.2F"%preco)
