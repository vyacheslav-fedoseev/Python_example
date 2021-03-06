"""

При написании текста курсовой работы студент по ошибке неверно оформил ссылки на цитируемые источники.
Примером такой ошибки может быть строка:
" ... этот метод активно обсуждался в работах. [1,12,19-23] ..."
которую надо переделать в
" ... этот метод активно обсуждался в работах [1,12,19-23]. ..."
Используя регулярные выражения, выполните замену ошибочного оформления на правильное.

"""

import re

s = input()
reg = r'\.\s\[[^.]+\]\s'

for el in re.findall(reg, s):
    s = re.sub(reg, " " + el[2:-1] + ". ", s, 1)

print(s)



"""

Найти все правильные адреса электронной почты, содержащиеся в строке.
Адреса формируются согласно требованиям стандарта RFC 5322. Имя почтового ящика содержит не более 3 слов,
разделенных символом ".". Доменное имя - от двух до трех уровней.
P.s. решение не очень хорошее :)

"""


for el in re.split(r' ', input()):
    string = re.search(r'^[a-zA-Z0-9_+-]+(?:\.[a-zA-Z0-9_+-]+){,2}@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+){1,2}$', el)
    if string:
        print(string.string)