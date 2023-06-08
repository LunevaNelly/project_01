# Задача 2
# Задача 1.2.
# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
import random
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
random_index=random.randrange(len(my_favorite_songs))
sum_sound_time = 0
sum_sound_time += my_favorite_songs[random_index][1]
random_index=random.randrange(len(my_favorite_songs))
sum_sound_time += my_favorite_songs[random_index][1]
random_index=random.randrange(len(my_favorite_songs))
sum_sound_time += my_favorite_songs[random_index][1]

print ('три песни звучат ', round(sum_sound_time, 2), 'минут')
 


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.
import random
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
sum_sound_time = 0

random_index=random.choice(list(my_favorite_songs_dict))
sum_sound_time += my_favorite_songs_dict[random_index]
random_index=random.choice(list(my_favorite_songs_dict))
sum_sound_time += my_favorite_songs_dict[random_index]
random_index=random.choice(list(my_favorite_songs_dict))
sum_sound_time += my_favorite_songs_dict[random_index]

print ('три песни звучат ', round(sum_sound_time, 2), 'минут')


# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
import random
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
random_index=random.choice(list(my_favorite_songs_dict))
print(random_index)

# import random
# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime

from datetime import datetime
import random
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
random_index=random.randrange(len(my_favorite_songs))
t = my_favorite_songs[random_index][1]
t = str(round(t,2))
timeObj = datetime.strptime(str(t), "%M.%S")

print("Песня :",my_favorite_songs[random_index])
print("Минуты:", timeObj.minute)
print("Секунды:", timeObj.second)


