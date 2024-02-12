            # КОД АЛЕКСЕЯ ПЕТРЕНКО

#Константы 
FILE_NAME = 'phone_directory.txt'
ID = 'id'
LAST_NAME = 'Фамилия'
FIRST_NAME = 'Имя'
SECOND_NAME = 'Отчество'
PHONE = 'Телефон'
HEADERS = [ID, LAST_NAME, FIRST_NAME, SECOND_NAME, PHONE]

def load_directory(file_name=FILE_NAME):
    #Загрузка справочника вида list[dict[str, str]] из файла
    directory = []

    with open(file_name, 'r', encoding= 'utf-8') as file:
        # Альтернативный вариант с семинара
        for i, line in enumerate(file, start=1):
            row = [i] + line.strip().split()
            directory.append(dict(zip(HEADERS, row)))

    return directory

def print_all_directory(directory):
    # Вывод на экран всех записей справочника 
    for item in directory:
        print(*(f"{k}: {v<16}" for k, v in item.items()))

def add_contact(directory):
    #Добавление нового контакта в справочник без сохранения в файл
    row = input('Введите Ф.И.О. и телефон, разделенные пробелами: ').split()
    line = [len[directory]+1] + [item.strip().capitalize() for item in row]
    directory.append(dict(zip(HEADERS, line)))

def find_by_key(key: str, value: str, directory: list[dict[str, str]]):
    # Поиск совпадений значения в справочнике по столбцу key (ключ словаря)
    for item in directory:
        if item[key] == value:
            print(item)

def edit_by_id(number: str, directory):
    # Изменение строки справочника без сохранения в файл
    if number.isdigit() and (id_ := int(number)) <= len(directory):
        print(*(f"{k}: {v<16}" for k, v in directory[id_ -1].items()))
        row = input(
            'Введите исправленные Ф.И.О. и телефон, разделенные пробелами для замены: ').split()
        line = [id_] + [item.strip().capitalize() for item, in row]
        directory[id_ - 1] = dict(zip(HEADERS, line))
        print('Данные обновлены')
    else:
        print(f'Такой {ID} отсутствует в справочнике. Возврат в меню...')

        



def save_directory(directory: list[dict[str, str]], file_name=FILE_NAME):
    # Построчное сохранение справочника в тескстовый файл
    with open(file_name, 'w', encoding='utf-8') as file:
        for item in directory:
            file.write(' '.join(f'{value}' for key, value in item.items() if key != ID) + '\n')

def main(directory):
    # Цикл событий основного меню
    while True:
        print(f"""\n Выберите пункт меню:)
        1: Вывести все данные
        2: Записать новый контакт
        3: Найти контакт по полю '{LAST_NAME}'
        4: Найти контакт по полю '{FIRST_NAME}'
        5: Изменить контакт по полю '{ID}'
        6: Удалить контакт по полю '{ID}'
        7: Изменить поле '{LAST_NAME}'
        8: Удалить поле по имени '{FIRST_NAME}'
        9: Скопировать строку по '{ID}' в новый файл
        0: Сохранить и выйти""")
        x = input()

        if x == '1':
            print_all_directory(directory)
        elif x == '2':
            add_contact(directory)
        elif x == '3':
            find_by_key(key=LAST_NAME,
                        value=input(
                            f'{LAST_NAME.title()}: ').strip().capitalize(),
                        directory=directory)
        elif x == '4':
            find_by_key(key=FIRST_NAME,
                        value=input(
                            f'{FIRST_NAME.title()}: ').strip().capitalize(),
                        directory=directory)
        elif x == '5':
            edit_by_id(number=input(f'Введжите {ID}, который хотите изменить: '),
                       directory=directory)
        elif x == '6':
            delete_by_id(number=input(f'Введжите {ID}, который хотите удалить: '),
                       directory=directory)
        elif x == '7':
            edit_by_last_name(directory=directory)
        elif x == '8':
            delete_by_first_name(directory=directory)
        elif x == '9':
            copy_line(number=input(f'Введите {ID}, который хотите скопировать в отдельный файл: '),
                      directory=directory)
        elif x == '0':
            save_directory(directory)
            break
        else:
            print('Неверная команда!')




if __name__ == '__main__':
    main(load_directory()) 
