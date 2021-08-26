"""

Дана строка, содержащая сообщение, и её расшифровка. Написать алгоритм, который бы расшифровывал любое сообщение
заданной кодировкой.

"""

"""
s_input = "QPMQBES MU UMTLG ZB G JFOGXZIMYIS MEGO ZB OB EMPMHS"
s_ouput = "PROPADU OT TOSKI YA I LENIWYHOZHU ODIN YA NA DOROGU"

dictionary = {}
for x in range(len(s_input)):
    dictionary[s_input[x]] = s_ouput[x]

# print("".join([dictionary[x] for x in input()]))
import string

for x in string.ascii_uppercase:
    if x not in dictionary:
        dictionary[x] = "-"

lst = sorted(dictionary.items())

print("".join([lst[x][0] for x in range(len(dictionary))]))        #ABC|DEF|GHI|JKL|MNO|PQR|STU|V|WX|YZ
print("".join([lst[x][1] for x in range(len(dictionary))]))        #-A-|-DE|IGH|L-K|O-N|RP-|UST|-|-W|ZY
                                                                   #CAB|FDE|IGH|LJK|OMN|RPQ|UST|V|XW|ZY
"""

s_input = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
s_ouput = "CABFDEIGHLJKOMNRPQUSTVXWZY "

dictionary = {}
for x in range(len(s_input)):
    dictionary[s_input[x]] = s_ouput[x]

print("".join([dictionary[x] for x in input()]))
