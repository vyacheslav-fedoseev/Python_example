"""

Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество dd известных нам слов, после чего на d строках указываются эти
слова. Затем передаётся количество l строк текста для проверки, после чего l строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:

stepic
champignons
the

"""

lst_without_fault = [input().lower() for i in range(int(input()))]
lst = [input().lower() for i in range(int(input()))]
lst_one = []
for x in lst:
    lst_one += x.split(" ")

for x in set(lst_one):
    if x not in lst_without_fault:
        print(x)
