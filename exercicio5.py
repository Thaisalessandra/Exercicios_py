numb1=int(input("Digite o primeiro número: "))
    numb2=int(input("Digite o segundo número: "))
operacao=str(input("Digite a operação que deseja fazer: "))
if operacao == "-":
    conta=numb1-numb2
    print("resultado da subtração é ",conta)
elif operacao == "+":
    conta=numb1+numb2
    print("resultado da soma é ", conta)
elif operacao == "/" :
    conta=numb1/numb2
    print("resultado da divisão é ", conta)
elif operacao == "*" :
    conta=numb1*numb2
    print("resultado da multiplicação é ", conta)
