 categoria=int(input("Digite a categoria do produto para saber o valor:"))
if categoria == 1:
    print("Valor do produto é R$100,00")
elif categoria ==2:
    subcategoria=int(input("Digite a subcategoria:"))
    if subcategoria ==3 :
        print("Valor do produto é R$ 50,00")
    elif subcategoria == 4:
        print("Valor do produto é R$ 25,00")
    else:
        print("Subcategoria inválida!")
        subcategoria=int(input("Digite uma subcategoria válida(3 ou 4): "))
        if subcategoria == 3:
            print("Valor do produto é R$ 50,00")
        elif subcategoria == 4:
            print("Valor do produto é R$ 25,00")
elif categoria == 5:
    subcategoria=int(input("Digite subcategoria:"))
    if subcategoria == 6 :
        print("Valor do produto é R$ 500,00")
    elif subcategoria == 7:
        print("Valor é R$ 800,00")
    else:
        print("subcategoria inválida!")
        subcategoria=int(input("Digite uma subcategoria válida(6 ou 7):"))
        if subcategoria == 6:
            print("Valor do produto é R$ 500,00")
        elif subcategoria == 7:
            print("Valor é R$ 800,00")
elif categoria != 1 or categoria != 2 or categoria != 5 :
    print("Categoria inválida!")
    categoria=int(input("Digite uma categoria válida: "))
    if categoria == 1:
        print("Valor do produto é R$100,00")
    elif categoria == 2:
        subcategoria = int(input("Digite a subcategoria:"))
        if subcategoria == 3:
            print("Valor do produto é R$ 50,00")
        elif subcategoria == 4:
            print("Valor do produto é R$ 25,00")
        else:
            print("Subcategoria inválida!")
            subcategoria = int(input("Digite uma subcategoria válida(3 ou 4): "))
            if subcategoria == 3:
                print("Valor do produto é R$ 50,00")
            elif subcategoria == 4:
                print("Valor do produto é R$ 25,00")
    elif categoria == 5:
        subcategoria = int(input("Digite subcategoria:"))
        if subcategoria == 6:
            print("Valor do produto é R$ 500,00")
        elif subcategoria == 7:
            print("Valor é R$ 800,00")
        else:
            print("subcategoria inválida!")
            subcategoria = int(input("Digite uma subcategoria válida(6 ou 7):"))
            if subcategoria == 6:
                print("Valor do produto é R$ 500,00")
            elif subcategoria == 7:
                print("Valor é R$ 800,00")
