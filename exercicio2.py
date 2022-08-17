 velocidade=int(input("digite a velocidade do carro:"))
if velocidade > 80:
        multa=5*(velocidade-80)
        print("Velocidade acima do permitido valor da multa R$",multa )
else:
    print("Velocidade dentro do permitido não está sujeito a multa!")
