def ano_bissexto(ano):
    return (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0)


def days_in_month(mes, ano):

    if mes in ['Setembro', 'Abril', 'Junho', 'Novembro']:
        print(30)

    elif mes in ['Janeiro', 'Março', 'Maio', 'Julho', 'Agosto', 'Outubro', 'Dezembro']:
        print(31)

    elif mes == 'Fevereiro' and ano_bissexto(ano) == True:
        print(29)

    elif mes == 'Fevereiro' and ano_bissexto(ano) == False:
        print(28)

    else:
        return None