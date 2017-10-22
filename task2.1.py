"""

Вариант 2

Списки №6
Даны имена и средняя успеваемость учеников класса.
Необходимо вывести имена одного или нескольких учеников,
находящихся на предпоследнем месте по успеваемости.

Формат входных данных: Набор студентов представлен списком длиной N, то есть
количество учеников в классе, каждый элемент которого представлен в виде
вложенного списка из двух элементов: Имя, оценка.

Например,
students = [ [Петя, 4.5], [Вася, 4.3], [Коля, 3.5], [Никита, 4.8], [Катя, 4.3] ]

Формат выходных данных: Вывести только имена учеников, чьи оценки предпоследние с конца.
В нашем примере наименьшаяоценка из учеников 3.5, следующая по возрастанию 4.3.
Присутствуют 2 ученика с такой оценкой: Вася и Катя.

"""


def entering_list():

    students = list()
    name = str()
    print("Начните ввод данных (имя и оценка через клавишу enter). Для окончания введите '-1':")
    while name != '-1':
        name = input()
        if name == '-1':
            break
        mark = float(input())
        en_lst = list()
        en_lst.append(name)
        en_lst.append(mark)
        students.append(en_lst)
        print(students)
    return students


def sort_by_mark(students):

    sorting_list = []
    for item in students:
        sorting_list.append(item[1])
    sorting_list.sort()  # Сортируем по оценкам
    min = sorting_list[0]
    for item in sorting_list:  # Находим предпоследнюю по успеваемости оценку
        if item != min:
            sec_min = item
            break
    print(sorting_list)
    print(sec_min)
    for item in students:  # Найденные ученики, предпоследние по усеваемости
        if item[1] == sec_min:
            print(item[0])

sort_by_mark(entering_list())

