import os
import shutil


def add_decor(f):
    def inner(*args, **kwargs):
        # поведение до вызова
        print('*' * 30)
        result = f(*args, **kwargs)
        print('*' * 30)
        # поведение после вызова
        return result

    return inner


@add_decor
def copy_file_or_folder(name_what_copy, name_new_copy):
    if os.path.isfile(name_what_copy):
        shutil.copyfile(name_what_copy, name_new_copy)
    if os.path.isdir(name_what_copy):
        shutil.copytree(name_what_copy, name_new_copy)


@add_decor
def add_money(cash, balance):
    balance = cash + balance
    return balance


@add_decor
def vivod_balance(balance):
    print('Ваш балланс:', balance)


@add_decor
def buy_item(cash, balance):
    if cash > balance:
        print("Денег не хватает")
    else:
        # item_to_buy = str(input("Введите название покупки: "))
        # history_pokuppok(cash, item_to_buy)
        balance = (balance - cash)
        # history_buy.append(item_to_buy, balance)
        # print(history_buy)
        return balance
