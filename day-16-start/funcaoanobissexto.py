from datetime import date


def calcular_idade(nascimento):
    hoje = date.today()
    try:
        aniversario = nascimento.replace(year=hoje.year)

    # Se a data de nascimento for 29/02
    # E o ano atual não for ano bissexto
    except ValueError:
        aniversario = nascimento.replace(year=hoje.year,
                                      month=nascimento.month + 1, day=1)

    if aniversario > hoje:
        return hoje.year - nascimento.year - 1
    else:
        return hoje.year - nascimento.year

print(calcular_idade(date(1997, 2, 3)), "anos")