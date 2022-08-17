def verificaLista(L):   
    if (len(L) == 0):
        return "Lista Vazia"
    else:
        maior = 0
        for a in L:
            if a > maior:
                maior = a
        return maior

lista = [25, 35, 18, 50, 10]
print(verificaLista(lista))

a = [100, 200, 5000, 20, 10000]
resultado =  verificaLista(a)
print("Resultado: ",resultado)

b = [10.8, 20.35, 40.12]
resultado2 = verificaLista(b)
print("Resultado double: ", resultado2)
