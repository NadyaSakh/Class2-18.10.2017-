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


students = []
marks = []


def input_data(marks, students):
    imp_str = ''
    print("Введите имена и оценки через пробел. \
Напишите end для выхода\n")
    while imp_str != 'end':
        imp_str = input()
        if imp_str != 'end':
            tmp_list = imp_str.split(" ")
            try:
                mark = float(tmp_list[1])
            except ValueError:
                print("Оценка должна быть числом")
                break
            except IndexError:
                print("Вы не ввели имя")
                break
            if mark > 5 or mark <= 0 or mark is None:
                print("Оценка должна быть числом от 0 до 5")
                break
            if not tmp_list:
                break
            students.append(tmp_list)
            marks.append(tmp_list[1])
        print(students)
        print(marks)


def sort_by_mark(marks, students):
    if not students or not marks:
        print("Пустой список")
        return
    if len(marks) != len(students):
        print("Недостаточно данных")
        return
    marks = set(marks)
    marks = sorted(marks)
    try:
        second_min = marks[1]
    except IndexError:
        print('Слишком мало студентов')
        return
    for student in students:
        if student[1] == second_min:
            print(student[0])

input_data(marks, students)
sort_by_mark(marks, students)