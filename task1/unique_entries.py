"""
============================================ №1
# имеется текстовый файл file.csv, в котром разделитель полей с данными: | (верт. черта)
# пример ниже содержит небольшую часть этого файла(начальные 3 строки, включая строку заголовков полей)


lastname|name|patronymic|date_of_birth|id
Фамилия1|Имя1|Отчество1 |21.11.1998   |312040348-3048
Фамилия2|Имя2|Отчество2 |11.01.1972   |457865234-3431
...


# Задание
# 1. Реализовать сбор уникальных записей
# 2. Случается, что под одиннаковым id присутствуют разные данные - собрать отдельно такие записи


"""

import pandas as pd

url = r"C:\Users\79832\Desktop\output.csv"

df = pd.read_csv(url, sep='|')

df = df.drop_duplicates()
duplicate_records = df[df.duplicated(subset='id', keep=False)]