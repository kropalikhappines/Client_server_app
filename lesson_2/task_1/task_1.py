"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.
"""
import csv

from chardet import detect


files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
name_cols = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']

file_result = 'data_report.csv'


def get_date():
    """

    Считывание из txt
    """
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    cols_data = []
    for file in files:
        with open(file, 'rb') as doc:
            words = doc.read()
        ENCODING = detect(words)['encoding']
        with open(file, encoding=ENCODING) as doc:
            for string_name in doc:
                for col in name_cols:
                    if col in string_name:
                        if col in name_cols[0]:
                            lst_name = string_name.split(' ')
                            name = lst_name[-1].rstrip('\n')
                            # ' '.join([lst_name[0], lst_name[1]])
                            os_prod_list.append(name)
                            cols_data.append(' '.join(lst_name[:2]))
                        elif col in name_cols[1]:
                            string_name = string_name.rstrip('\n').rstrip(' ')
                            # print(string_name)
                            lst_name = string_name.split(' ')
                            name = ' '.join(lst_name[-4:])
                            # ' '.join([lst_name[0], lst_name[1]])
                            os_name_list.append(name)
                            cols_data.append(' '.join(lst_name[:2]))
                        elif col in name_cols[2]:
                            lst_name = string_name.split(' ')
                            name = lst_name[-1].rstrip('\n')
                            os_code_list.append(name)
                            cols_data.append(' '.join(lst_name[:2]))
                        elif col in name_cols[3]:
                            string_name = string_name.rstrip('\n')
                            lst_name = string_name.split(' ')
                            name = ' '.join(lst_name[-2:])
                            os_type_list.append(name)
                            cols_data.append(' '.join(lst_name[:2]))
    """
    Я может не правильно понял дз, но в каждый список я сохранил по названиям,
    т.е. ['lenovo', 'acer'], ['win7', 'win10']
    поэтому поменял все местами кодом ниже и выше не стал менять
    """
    el = cols_data.pop(2)
    cols_data.insert(0, el)
    cols_data = cols_data[:4]
    test = [os_prod_list, os_name_list, os_code_list, os_type_list]
    for lst in test:
        lst_name_1 = lst.pop(0)
        lst_name_2 = lst.pop(0)
        lst_name_3 = lst.pop(0)
        test[0].append(lst_name_1)
        test[1].append(lst_name_2)
        test[2].append(lst_name_3)

    test.append(cols_data)
    pops = test.pop(-1)
    test.insert(0, pops)
    main_data = test[:-1]
    return main_data


def write_to_csv(file_result):
    """
        запись в файл
    """
    main_data = get_date()
    with open(file_result, 'w', encoding='utf-8') as file:
        WRITER = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)

        for row in main_data:
            WRITER.writerow(row)


write_to_csv(file_result)
