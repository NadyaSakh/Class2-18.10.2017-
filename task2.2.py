"""

Вариант 2 Функции №2

Дано действительное положительное число а и целое число n. Вычислите а в степени n.
Решение оформите в виде функции power(a, n).
Стандартной функцией возведения в степень польоваться нельзя.

"""
import sys

a = None
power = None


def in_power(a, power):
    if a is None or power is None: #когда введены некорректные данные
        print("Некорректная степень")
        return
    pow_a = 1
    if power > 0:
        while power > 0:
            pow_a *= a
            power -= 1
    elif power < 0:
        pow_a = 1/power(a, -1 * power)
    print(pow_a)


def input_function(a, power):
    try:
        a = float(input("Введите число, которое желаете возвести в степень:\n"))
    except ValueError:
        print("Вы должны ввести число")
        sys.exit() #   Как правильно делать выход из программы при обработке исключения?
    except TypeError:
        print("Введены некорректные данные")
        sys.exit()
    try:
        power = int(input("Введите степень числа а:\n"))
        sys.exit()
    except ValueError:
        print("Вы должны ввести целое число")
        sys.exit()
    except TypeError:
        print("Введены некорректные данные")
        sys.exit()
    return a, power

a, power = input_function(a, power)
in_power(a, power)
