"""

Многие криптографические алгоритмы работают только с целыми числами, что не вызывает проблем, если надо выполнить
сложение, вычитание или умножение. Однако с делением – так просто.
Допустим, множество чисел, с которыми вы можете работать – это остатки от деления на некоторое натуральное число p.
Такое множество будем обозначать Zp. И Zp = {0,1,2,…,p-1}.
Арифметические операции в Zp реализуются как обычно, только результат заменяется его остатком от деления на p.
Здесь a, b принадлежат Zp:
(a+b) в Zp = (a+b) mod p
(a-b) в Zp = (a-b) mod p
(a*b) в Zp = (a*b) mod p
С делением ситуация несколько сложней, потому что результат деления a / b тоже должен принадлежать Zp. Поэтому
(a / b) в Zp = (a * b^{-1}) mod p,
где b^{-1} – число, обратное к b в Zp. Иными словами (b * b^{-1}) mod p = 1
Причем число b^{-1} существует, если числа p и b – взаимно простые, т.е. НОД(b,p) = 1.
Здесь НОД – наибольший общий делитель.
Если же числа p и b – не взаимно простые, то b^{-1} не существует, и вычислить значение выражения не возможно.

Вам необходимо вычислить значение выражения в Zp. Выражение представляет собой строку, содержащую целые десятичные
числа и знаки операций «+», «*» и «/». В конце строки символ «=». Других символов в строке нет.

Формат входных данных
В первой строке – число P. P < 10^{10}.
Во второй строке – строка, содержащая арифметическое выражение, состоящее из целых десятичных чисел и знаков операций
«+», «*» и «/». В конце строки символ «=». Других символов в строке нет.
Длина строки – не больше 1000 символов. Числа, которые используются в выражении, не больше 10^{10}.

Формат выходных данных
В первой строке – целое десятичное число, равное значению введенного выражения. Либо символ «@»,
если вычислить значение выражения не удалось.
Примеры
стандартный ввод	стандартный вывод
7
1=
                            1
7
1*10+12/5=
                            4
8
1*10+12/6*4+98+5/7/7/7/7=
                            @

"""


def findModInverse(a, n):
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, n

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % n


mod_num = int(input())


class MyInteger(int):  # наследуемся от класса int, чтобы переопределить некоторые операции, которые нужно для Zp
    def __add__(self, num):
        return MyInteger((self.real + int(num)) % mod_num)

    def __sub__(self, num):
        return MyInteger((self.real - int(num)) % mod_num)

    def __mul__(self, num):
        return MyInteger((self.real * int(num)) % mod_num)

    def __truediv__(self, num):
        from math import gcd
        if gcd(int(num), mod_num) != 1:
            print("@")
            from sys import exit
            exit()
        else:
            return MyInteger(self.real * int(findModInverse(int(num), mod_num)) % mod_num)


def to_MyInteger(num):
    return MyInteger(num) if num in "0123456789" else num


def from_digit_to_number(lst: list) -> list:
    temp_lst = []
    i = 0
    while i < len(lst):
        if not isinstance(lst[i], str):
            temp_lst.append(lst[i])
            i += 1
            while i < len(lst) and not isinstance(lst[i], str):
                temp_lst[-1] = MyInteger(str(temp_lst[-1]) + str(lst[i]))
                i += 1
        else:
            i += 1
    return temp_lst


s = input()[:-1]

lst_of_elements = list(map(to_MyInteger, s))  # получаем список цифр и операций
lst_of_numbers = list(set(from_digit_to_number(lst_of_elements)))  # цифры объединяются в числа и убираются одинаковые

k = 65  # код ASCII буквы А
dictionary = {}
for x in lst_of_numbers:
    dictionary[chr(k)] = x  # заносим в словарь буквы и их соответствия числам
    k += 1

dictionary2 = {}
for x in dictionary:
    dictionary2[str(dictionary[x])] = x  # словарь, в котором ключ и значения поменялись друг с другом

lst_of_numbers = [str(x) for x in lst_of_numbers]
lst_of_numbers.sort(key=lambda x: int(x), reverse=True)  # ключи располагаются от наибольшего к наименьшему значению

s_chars = s
for key in lst_of_numbers:
    s_chars = s_chars.replace(key, dictionary2[key])  # заменяем числа на буквы согласно словарю

print(eval(s_chars, dictionary) % mod_num)
