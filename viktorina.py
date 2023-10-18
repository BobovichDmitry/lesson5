
def viktorina():

    import random

    birth_data = ['Pushkin 01.01.1984', 'Lenin 02.08.1988', 'Stalin 03.11.1954', 'Pushkin2 01.12.1984', 'Lenin2 02.03.1988',
                  'Stalin2 03.02.1954']
    n = 4
    # n - количество случайных элементов
    repeat=''
    while repeat != 'N':
        result = random.sample(birth_data, n)
        count = 0
        for i in range(n):
            stroka = result[i].split()
            vvod_dati = input(('Введите Дату рождения ' + stroka[0] + ':'))
            if vvod_dati == (str(stroka[1])):
                print('Ответ правильный! Поздравляем!')
                count += 1
            else:
                print('Правильная дата:', stroka[1])
                data_date = stroka[1][0:2]
                data_month = stroka[1][3:5]
                data_year = stroka[1][6:10]
                #print(data_date)
                #print(data_month)
                if data_date == '01':
                    data_date_text = "первое"
                if data_date == '02':
                    data_date_text = "второе"
                if data_date == '03':
                    data_date_text = "третье"
                if data_date == '04':
                    data_date_text = "четвертое"
                if data_date == '05':
                    data_date_text = "пятое"
                if data_date == '06':
                    data_date_text = "шестое"
                if data_date == '07':
                    data_date_text = "седьмое"
                if data_date == '08':
                    data_date_text = "восьмое"
                if data_date == '09':
                    data_date_text = "девятое"
                if data_date == '10':
                    data_date_text = "десяток"
                if data_date == '11':
                    data_date_text = "одиннадцатое"
                if data_date == '12':
                    data_date_text = "двенадцатое"
                if data_date == '13':
                    data_date_text = "тринадцатое"
                if data_date == '14':
                    data_date_text = "четырнадцатое"
                if data_date == '15':
                    data_date_text = "пятнадцатое"
                if data_date == '16':
                    data_date_text = "шестнадцатое"
                if data_date == '17':
                    data_date_text = "семнадцатое"
                if data_date == '18':
                    data_date_text = "восемьнадцатое"
                if data_date == '19':
                    data_date_text = "девятнадцатое"
                if data_date == '20':
                    data_date_text = "двадцатое"
                if data_date == '21':
                    data_date_text = "двадцать первое"
                if data_date == '22':
                    data_date_text = "двадцать второе"
                if data_date == '23':
                    data_date_text = "двадцать третье"
                if data_date == '24':
                    data_date_text = "двадцать четвертое"
                if data_date == '25':
                    data_date_text = "двадцать пятое"
                if data_date == '26':
                    data_date_text = "двадцать шестое"
                if data_date == '27':
                    data_date_text = "двадцать седьмое"
                if data_date == '28':
                    data_date_text = "двадцать восьмое"
                if data_date == '29':
                    data_date_text = "двадцать девятое"
                if data_date == '30':
                    data_date_text = "тридцатое"
                if data_date == '31':
                    data_date_text = "традцать первое"
                if data_month == '01':
                    data_month_text = 'января'
                if data_month == '02':
                    data_month_text = 'февраля'
                if data_month == '03':
                    data_month_text = 'марта'
                if data_month == '04':
                    data_month_text = 'апреля'
                if data_month == '05':
                    data_month_text = 'май'
                if data_month == '06':
                    data_month_text = 'июня'
                if data_month == '07':
                    data_month_text = 'июля'
                if data_month == '08':
                    data_month_text = 'августа'
                if data_month == '09':
                    data_month_text = 'сентября'
                if data_month == '10':
                    data_month_text = 'октября'
                if data_month == '11':
                    data_month_text = 'ноября'
                if data_month == '12':
                    data_month_text = 'декабря'
                print(f"Правильная дата: {data_date_text} {data_month_text} {data_year}")
        print('Количество правильных ответов: ', count)
        print('Количество НЕправильных ответов: ', n-count)
        repeat = input('Повторим? Y/N: ').upper()
if __name__ == "__main__":
    viktorina()