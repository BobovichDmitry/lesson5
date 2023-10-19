import os
import shutil


def copy_file_or_folder(name_what_copy, name_new_copy):
    if os.path.isfile(name_what_copy):
        shutil.copyfile(name_what_copy, name_new_copy)
    if os.path.isdir(name_what_copy):
        shutil.copytree(name_what_copy, name_new_copy)



def add_money(cash, balance):
    balance = cash + balance
    return balance


def buy_item(cash, balance):
    if cash > balance:
        print("Денег не хватает")
    else:
        #item_to_buy = str(input("Введите название покупки: "))
        #history_pokuppok(cash, item_to_buy)
        balance = (balance - cash)
        # history_buy.append(item_to_buy, balance)
        # print(history_buy)
        return balance
