print('Конвертер Секунд')
try:
    duration = int(input('Введите число секунд: '))
except ValueError:
    duration = int(input('Введите целое число секунд или 0 для выхода: '))

days = 0
hours = 0
mins = 0
sec = 0
while duration > 0:
    if duration < 60:
        sec = duration
        index = 1
    elif duration < 3600:
        mins = duration // 60
        sec = duration % 60
        index = 2
    elif duration < 86400:
        hours = duration // 3600
        mins = (duration % 3600) // 60
        sec = (duration % 3600) % 60
        index = 3
    else:
        days = duration // 86400
        hours = (duration % 86400) // 3600
        mins = ((duration % 86400) % 3600) // 60
        sec = ((duration % 86400) % 3600) % 60
        index = 4

    list_of_prints = {'1': f'{sec} с',
                      '2': f'{mins} м {sec} с',
                      '3': f'{hours} ч {mins} м {sec} с',
                      '4': f'{days} дн {hours} ч {mins} м {sec} с'
                      }

    print(list_of_prints[f'{index}'])
    try:
        duration = int(input('Введите число секунд: '))
    except ValueError:
        duration = int(input('Введите целое число секунд или 0 для выхода: '))

print('Good bye!')