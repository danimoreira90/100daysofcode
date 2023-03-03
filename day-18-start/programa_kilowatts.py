def leap_year(year):
    '''
    Checks if a year is a regular year or a leap year.

    :parameter year: str: year to be checked
    :return: boolean: True if year is a leap year.
    '''
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def date_selector(parameter, date):
    '''
    Selects a parameter (day, month or year) from a date in the DD/MM/YYYY format.

    :param parameter: str: the pararemeter you want to obtain from the date, possible values -> d (day), m (month) and y(year)
    :param date: str: the date you want to obtain the parameter
    :return: integer: the date parameter that can be the day, month or year
    '''
    if parameter == 'd':
        date_object = date.split('/')[0]
    elif parameter == 'm':
        date_object = date.split('/')[1]
    elif parameter == 'y':
        date_object = date.split('/')[2]

    return int(date_object)


def days_in_year(date):
    '''
    Counts the days, in the same year, between 01/01 and a date informed.
    :param date: str: date to count the number of days from 01/01
    :return: total_days: number of days from 01/01 to the date informed as a parameter.
    '''
    total_days = 0

    # calculando dias percorridos até o mês anterior à data

    months_regular_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # checks if calendar is from a regular year or leap year
    if leap_year(date_selector('y', date)):
        days_month = months_leap_year
    else:
        days_month = months_regular_year

    for days in days_month[0:int(date_selector('m', date)) - 1]:
        total_days += days

    # calculando dias no mês de referência

    total_days += date_selector('d', date)

    return total_days


# Receiving inputs

number_dates = int(input('Favor inserir o número de registros primeiro e os registros em seguida:\n'))
database = []

for i in range(number_dates):
    consumption = input()
    database.append(consumption.split())

# Checking for Consecutive Days and Adding Consumption

agg_consump = 0
number_days = 0

# Calculates the consumption for consecutive days for all cases but one (31/12 -> 01/01)
for i in range(len(database) - 1):
    if (date_selector('y', database[i + 1][0])) == (date_selector('y', database[i][0])):
        if days_in_year(database[i + 1][0]) - days_in_year(database[i][0]) == 1:
            agg_consump += int(database[i + 1][1]) - int(database[i][1])
            number_days += 1

    # Calculates consumption for the case of 31/12 -> 01/01

    else:
        if ((date_selector('y', database[i + 1][0])) - (date_selector('y', database[i][0])) == 1) and date_selector('m',
                                                                                                                    database[
                                                                                                                        i + 1][
                                                                                                                        0]) == 1 and date_selector(
                'm', database[i][0]) == 12 and date_selector('d', database[i + 1][0]) == 1 and date_selector('d',
                                                                                                             database[
                                                                                                                 i][
                                                                                                                 0]) == 31:
            agg_consump += int(database[i + 1][1]) - int(database[i][1])
            number_days += 1

# Outputs
print(f'{number_days} dia(s)')
print(f'{agg_consump} KWh')
