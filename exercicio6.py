valorCasa=int(input("Digite o valor da casa que você quer comprar: "))
    salario=int(input("Digite seu salário: "))
    parcelas=int(input("Digite em quantos anos você quer pagar: "))
    sarlarioporc=(salario/100)*30
    parcelacasa=valorCasa/parcelas
if parcelacasa > sarlarioporc:
    print("Infelizmente não podemos aprovar o empréstimo, valor da parcela superior os 30% de seu  salário.")
else:
    print("Empréstimo aprovado! valor da parcela é R$",parcelacasa)
