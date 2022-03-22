# Функция получения списка, отсортированного по количеству слов и,
# в случае равенства слов, по алфавиту
def get_final_list(data):
    # Создание списка из полученной на вход строки
    input_split = data.split()

    # Создание двух списков. Первый со словами, второй с их количеством
    list_first = []
    list_second = []
    count = 0
    for i in input_split:
        if count % 2 == 1:
            list_first.append(i)
        else:
            list_second.append(i)
        count += 1

    # Создание из двух списков словаря, состоящего из строк
    str_dict = dict(zip(list_second, list_first))

    # Создание словаря из строк и чисел
    str_int_dict = dict([y, int(x)] for y, x in str_dict.items())

    # Объединение слов, с одинаковым колличеством
    # внутри словаря, в отдельные списки
    dict_of_lists = {}
    for key, value in str_int_dict.items():
        dict_of_lists.setdefault(value, [])
        dict_of_lists[value].append(key)

    # Сортировка слов внутри списков по алфавиту
    for i in dict_of_lists.values():
        i.sort()

    # Создание списка из кортежей со словами в списках и количеством слов,
    # отсортированный в порядке убывания количества слов
    sorted_list = sorted(dict_of_lists.items(), reverse=True)

    # Создание отсортированного словаря из списка sorted_list
    sorted_dict = {k: v for k, v in sorted_list}

    # Создание финального списка со словами отсортированными
    # по количеству слов, а в случае равенства количества слов, по алфавиту
    final_list = [k for v in sorted_dict.values() for k in v]
    return final_list


# Функция поиска интересующих слов
def get_result(data, list):
    # Переменные limit и index введены для ограничения вывода десятью словами
    limit = 10
    index = 0
    # Проход циклом по финальному списку для получения интересующих слов
    for i in list:
        if i.startswith(data):
            print(i)
            index += 1
        if index == limit:
            break


if __name__ == "__main__":
    # Ввод слов с их количеством
    input_first = input('Введите слова и их количество: ')

    # Ввод начала интересующих слов
    input_second = input('Введите начало интересующих слов: ')

    # Вызов функции для получения результата
    get_result(input_second, get_final_list(input_first))
