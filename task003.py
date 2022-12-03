# Вводим с клаиватуры строку. Необходимо вывести строку,
# где развернём подстроку между первой и последней буквой "о"
# из исходной строки. Если она только одна или её нет - то сообщить,
# что буква "о" - одна или не встречается.


count = 0
s = input(str('Enter the line '))
print(s)
a = s.find('o')
b = s.rfind('o')
sNew = s[b-1: a: -1]
print(sNew)

if s.count('o') == 0:
    print('The letter "o" does not occur')
if s.count('o') == 1:
    print('The letter "o" occurs once')