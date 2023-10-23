import os
import platform
import sys
import shutil
from money_bank import money_bank
from viktorina import viktorina
from function import *

while True:
    print('1. создать папку')
    print('2. удалить(файл/папку)')
    print('3. копировать(файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. Выход')
    print('13. Cохранить содержимое рабочей директории в файл')
    choice = input('Выберите пункт меню: ')
    if choice == '1':
        # print(os.getcwd())
        name_directory = str(input('Введите название директории для создания: '))
        os.mkdir(name_directory)
    elif choice == '2':
        name_to_delete = str(input('Введите название директории или файла для удаления: '))
        #if os.path.isfile(name_to_delete):
            #print('THIS IS FILE')
        try:
            os.remove(name_to_delete)
            print("Успешно удалено")
        except Exception as e:
                  print("Файл не существует")
                  print(e)
        #if os.path.isdir(name_to_delete):
            #print('THIS IS DIR')
        try:
            #if
             os.rmdir(name_to_delete)
             print("Успешно удалено")
        except Exception as e:
             print("Директория не обнаружена")
             print(e)
    elif choice == '3':
        name_what_copy = str(input('Введите название директории или файл который копируем: '))
        name_new_copy = str(input('Введите название для НОВОЙ директории или файла при копировании: '))
        copy_file_or_folder(name_what_copy, name_new_copy)
        # if os.path.isfile(name_what_copy):
        # shutil.copyfile(name_what_copy, name_new_copy)
        # if os.path.isdir(name_what_copy):
        # shutil.copytree(name_what_copy, name_new_copy)

    elif choice == '4':
        for root, dirs, files in os.walk(os.getcwd()):
            for filename in files:
                print(filename)
    elif choice == '5':
        folders = [e for e in os.listdir() if os.path.isdir(e)]
        print(folders)
    elif choice == '6':
        files_to_see = [e for e in os.listdir() if os.path.isfile(e)]
        print(files_to_see)
    elif choice == '7':
        print('У вас моя любимая Операционная система WINDOWS') if platform.system() == "Windows" else print("У вас какая-то неизвестная мне система ", platform.system())
    elif choice == '8':
        print('Creator: Bobovich Dmitry Aleksandrovich')
    elif choice == '9':
        money_bank()
    elif choice == '10':
        viktorina()
    elif choice == '11':
        name_new_cwd = str(input('Введите новую рабочую директорию: '))
        os.chdir(name_new_cwd)
        print(os.getcwd())
    elif choice == '13':
        files_to_file = ''
        dirs_to_files = ''
        for root, dirs, files in os.walk(os.getcwd()):
            for filename in files:
                # print(filename)
                files_to_file = str(files_to_file)  + ' , ' +  str(filename)
                # with open("listdir.txt", 'a+') as ff:
                # ff.write(f'{filename} ,  ')
            for directory in dirs:
                dirs_to_files = str(dirs_to_files) + ' , ' + str(directory)
                print(dirs_to_files)
                # with open("listdir.txt", 'a+') as ff:
                # ff.write(f'{directory} ,  ')
                # print(directory)
        with open("listdir.txt", 'w') as ff:
            ff.write(f' files: {files_to_file}\n')
            ff.write(f' directory: {dirs_to_files}')
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')
