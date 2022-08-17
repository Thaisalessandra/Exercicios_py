gasolina= 7.45
    alcool= 5.95
    dieselS10= 6.45
    dieselS500= 6.45
tipodeAuto=str(input("Digite o tipo de seu automóvel (Carro, Moto, Caminhonete, Caminhão, Ônibus):"))
if tipodeAuto == "Carro" or tipodeAuto == "carro" or tipodeAuto == "moto" or tipodeAuto == "Moto":
    combustivel_escolhido=str(input("Digite o combustivel que voce quer usar: "))
    if combustivel_escolhido != "alcool" and combustivel_escolhido != "gasolina":
        print("combustivel incompativel")
        combustivel_escolhido = str(input("Digite o combustivel que voce quer usar: "))
        if combustivel_escolhido == "alcool" or combustivel_escolhido == "gasolina":
            distancia = str(input("Digite a distancia a ser percorrida:"))
            consGasolina = int(input("Quantos KM seu Auto faz por Litro de gasolina?"))
            consAlcool = int(input("Quantos KM seu Auto faz por Litro de álcool?"))
            if consGasolina < consAlcool:
                print("Use Álcool!")
            else:
                print("Use gasolina!")
        else:
           print("combustivel incompativel")
           combustivel_escolhido = str(input("Digite o combustivel que voce quer usar: "))
           if combustivel_escolhido == "alcool" or combustivel_escolhido == "gasolina":
               distancia = str(input("Digite a distancia a ser percorrida:"))
               consGasolina = int(input("Quantos KM seu Auto faz por Litro de gasolina?"))
               consAlcool = int(input("Quantos KM seu Auto faz por Litro de álcool?"))
    elif combustivel_escolhido == "alcool" or combustivel_escolhido == "gasolina" and tipodeAuto == "carro" or tipodeAuto == "moto":
        distancia = str(input("Digite a distancia a ser percorrida:"))
        consGasolina = int(input("Quantos KM seu Auto faz por Litro de gasolina?"))
        consAlcool = int(input("Quantos KM seu Auto faz por Litro de álcool?"))
        if consGasolina < consAlcool:
                print("Use Álcool!")
        else:
                print("Use gasolina!")
elif tipodeAuto == "Caminhonete" or tipodeAuto == "caminhonete":
    consGasolina = int(input("Quantos KM seu Auto faz por Litro de gasolina?"))
    consumoS500 = int(input("Quantos KM seu Auto faz por Litro de álcool?"))
    if consGasolina < consumoS500:
        print("Use Diesel S500!")
    else:
        print("Use Gasolina")
elif tipodeAuto == "caminhão" or tipodeAuto == "Caminhão" or tipodeAuto == "onibus" or tipodeAuto == "Ônibus":
    consumoS500 = int(input("Quantos KM seu Auto faz por Litro Diesel S500 ?"))
    consumoS10 = int(input("Quantos KM seu Auto faz por Litro de diesel s10 ?"))
    if consumoS10 < consumoS500:
        print("Use Diesel S500!")
    else:
        print("Use Diesel S10")
