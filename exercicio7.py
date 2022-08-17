tipodeEstabelecimento=str(input("Digite qual é o tipo de estabelecimento(Residência-indústria-Comércio)"))
    quantKlw=int(input("Digite quantos kWh foram consumidos: "))
    if tipodeEstabelecimento == "Comércio" or tipodeEstabelecimento == "C" or tipodeEstabelecimento=="comercio" or tipodeEstabelecimento == "comércio":
        if quantKlw <= 1000:
            total=0.55*quantKlw
            print("Tipo comercial valor a ser pago R$ ", total)
        else:
            total=0.60*quantKlw
        print("Tipo comercial valor a ser pago R$ ",total)
    elif tipodeEstabelecimento == "Casa" or tipodeEstabelecimento == "R" or tipodeEstabelecimento == "Residêncial" or tipodeEstabelecimento == "residencial"or tipodeEstabelecimento == "Residencial" or tipodeEstabelecimento == "c" or tipodeEstabelecimento == "C":
        if quantKlw <= 500:
            total=0.40*quantKlw
            print("Tipo residêncial valor a ser pago R$ ", total)
        else:
            total=0.65*quantKlw
            print("Tipo residêncial valor a ser pago R$ ", total)
    elif tipodeEstabelecimento == "industria" or tipodeEstabelecimento == "indústria" or tipodeEstabelecimento == "Indústria" or tipodeEstabelecimento =="I":
        if quantKlw <= 5000 :
            total=0.55*quantKlw
            print("Tipo indústrial valor a ser pago R$ ", total)
        else:
            total=0.60*quantKlw
            print("Tipo indústrial valor a ser pago R$ ", total)
