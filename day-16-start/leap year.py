ano = int(input("Insira o ano a ser analisado: "))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("Ano bissexto.")
        else:
            print("Ano natural.")
    else:
        print("Ano bissexto.")
else:
    print("Ano natural.")