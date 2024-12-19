#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

time_halo = round(violator_songs_list[3][1], 2)  # 'Halo'
time_enjoy = round(violator_songs_list[5][1], 2)  # 'Enjoy the Silence'
time_clean = round(violator_songs_list[8][1], 2)  # 'Clean'
total_time_1 = round(time_halo + time_enjoy + time_clean, 2)

print(f'Три песни звучат {total_time_1} минут')


# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

# Вычисляем общее время звучания трех песен из словаря
time_sweet = round(violator_songs_list[1][1], 2)  # 'Sweetest perfection'
time_policy = round(violator_songs_list[6][1], 2)  # 'Policy of Truth'
time_dress = round(violator_songs_list[7][1], 2)  # 'Blue Dress'
total_time_2 = round(time_sweet  + time_policy + time_dress, 2)

print(f'А другие три песни звучат  {total_time_2} минут')
