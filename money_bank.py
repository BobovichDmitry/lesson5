"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
from function import *
balance = 0
def money_bank():
    money_count = 0
    balance = 0
    history_buy = []

    def history_pokuppok(cash, item_to_buy):
        history_buy.append((cash, item_to_buy))
        return history_buy
    #history_pokuppok(100, "eda")
    #history_pokuppok(200, "edasda")
    #print(history_buy)

    def buy_item(cash, balance):
        if cash > balance:
            print("Денег не хватает")
        else:
            item_to_buy = str(input("Введите название покупки: "))
            history_pokuppok(cash, item_to_buy)
            balance = (balance - cash)
            # history_buy.append(item_to_buy, balance)
            #print(history_buy)
            return balance

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            cash = int(input("Введите сумму для пополнения: "))
            balance = add_money(cash, balance)
            print("Ваш баланс: ", balance)
        elif choice == '2':
            cash = int(input("Введите сумму покупки: "))
            balance = buy_item(cash, balance)
        elif choice == '3':
            for history_buy_item in history_buy:
                print(f"Покупка: {history_buy_item[1]} на сумму, {history_buy_item[0]} ")
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

if __name__ == "__main__":
    money_bank()
