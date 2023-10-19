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
import pickle
import os
balance = 0


def money_bank():
    money_count = 0
    balance = 0
    history_buy = []
    if os.path.exists("orders_pickle"):
        with open("orders_pickle", 'rb') as f:
            history_buy = pickle.load(f)

    if os.path.exists("balance.txt"):
        with open("balance.txt", 'r') as f:
            balance = int(f.read())
    #print(history_buy)

    def history_pokuppok(cash, item_to_buy):
        history_buy.append((cash, item_to_buy))
        # my_file = open("orders.txt", "a")
        # my_file.write(f"{cash} {item_to_buy}\n")
        # my_file.close()
        return history_buy

    def buy_item(cash, balance):
        if cash > balance:
            print("Денег не хватает")
        else:
            item_to_buy = str(input("Введите название покупки: "))
            # my_file = open("orders.txt", "w+")
            # my_file.write(orders_to_file)
            # my_file.close()
            # history_buy.append(item_to_buy, balance)
            # print(history_buy)
            balance = (balance - cash)
            order = (cash, item_to_buy)
            history_buy.append(order)
            return balance

    while True:
        print("Ваш баланс: ", balance)
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            cash = int(input("Введите сумму для пополнения: "))
            balance = add_money(cash, balance)
        elif choice == '2':
            cash = int(input("Введите сумму покупки: "))
            name_pokupki = str(input("Введите название покупки: "))
            order = (cash, name_pokupki)
            history_buy.append(order)
            balance = balance - cash
        elif choice == '3':
            # 3my_file = open("orders.txt", "w")
            # print(history_buy)
            for history_buy_item in history_buy:
                # print(history_buy_item)
                print(f"Покупка: {history_buy_item[1]} сумма {history_buy_item[0]}")
                # my_file.write(f"{history_buy_item[1]}  {history_buy_item[0]}\n")
            # my_file.close()
        elif choice == '4':
            with open("orders_pickle", 'wb') as f:
                pickle.dump(history_buy, f)
            with open("balance.txt", 'w+') as ff:
                ff.write(str(balance))

            break
        else:
            print('Неверный пункт меню')


if __name__ == "__main__":
    money_bank()
