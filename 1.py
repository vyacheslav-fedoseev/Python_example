"""

Напишите программу, которая принимает на стандартный вход список игр футбольных команд с
результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.


Sample Input:

3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
Sample Output:

Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6

"""

from enum import Enum

n = int(input())
i = 0
lst = []
while i < n:
    temp = input().split(";")
    lst_temp = []
    for x in temp:
        if x.isdigit():
            lst_temp += [int(x)]
        else:
            lst_temp += [x]
    lst += [lst_temp]
    i += 1

set_of_teams = set()

for x in lst:
    for y in x:
        if not str(y).isdigit():
            set_of_teams.add(y)

dict_of_teams = dict()

for el in set_of_teams:
    dict_of_teams[el] = [0, 0, 0, 0, 0]


class Game(Enum):
    ALL_GAME = 0
    VICTORY = 1
    DRAW = 2
    DEFEAT = 3
    TOTAL_POINTS = 4


class GamePoints(Enum):
    VICTORY = 3
    DRAW = 1
    DEFEAT = 0


for x in lst:
    if x[1] > x[3]:
        dict_of_teams[x[0]][Game.VICTORY.value] += 1
        dict_of_teams[x[2]][Game.DEFEAT.value] += 1
        dict_of_teams[x[0]][Game.TOTAL_POINTS.value] += GamePoints.VICTORY.value
        dict_of_teams[x[2]][Game.TOTAL_POINTS.value] += GamePoints.DEFEAT.value
    elif x[1] < x[3]:
        dict_of_teams[x[2]][Game.VICTORY.value] += 1
        dict_of_teams[x[0]][Game.DEFEAT.value] += 1
        dict_of_teams[x[0]][Game.TOTAL_POINTS.value] += GamePoints.DEFEAT.value
        dict_of_teams[x[2]][Game.TOTAL_POINTS.value] += GamePoints.VICTORY.value
    else:
        dict_of_teams[x[2]][Game.DRAW.value] += 1
        dict_of_teams[x[0]][Game.DRAW.value] += 1
        dict_of_teams[x[0]][Game.TOTAL_POINTS.value] += GamePoints.DRAW.value
        dict_of_teams[x[2]][Game.TOTAL_POINTS.value] += GamePoints.DRAW.value
    dict_of_teams[x[0]][Game.ALL_GAME.value] += 1
    dict_of_teams[x[2]][Game.ALL_GAME.value] += 1

for x in dict_of_teams:
    print(x, end=":")
    for y in dict_of_teams[x]:
        print(y, end=" ")
    print()
