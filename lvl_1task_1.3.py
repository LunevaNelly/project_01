# Задача 3
# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом
# Например,
    # Введите номер месяца: 3
# Вы ввели март. 31 дней
    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней
    # Введите номер месяца: 15
    # Такого месяца нет!



	

a = int(input('Введите номер месяца : '))

if (0 < a < 13):
    if a == 1:
        print('Вы ввели Январь. В нем 31 день')
    if a == 2:
        print('Вы ввели Февраль. В нем 28 или 29 дней')
    if a == 3:
        print('Вы ввели Март. В нем 31 день')
    if a == 4:
        print('Вы ввели Апрель. В нем 30 дней')
    if a == 5:
        print('Вы ввели Май. В нем 31 день')
    if a == 6:
        print('Вы ввели Июнь. В нем 30 дней')
    if a == 7:
        print('Вы ввели Июль. В нем 31 день')
    if a == 8:
        print('Вы ввели Август. В нем 31 день')
    if a == 9:
        print('Вы ввели Сентябрь. В нем 30 дней')
    if a == 10:
        print('Вы ввели Октябрь. В нем 31 день.')
    if a == 11:
        print('Вы ввели Ноябрь. В нем 30 дней')
    if a == 12:
        print('Вы ввели Декабрь. В нем 31 день')
else:
    print('Такого месяца нет!')

