"""
============================================ №5*
В наличии текстовый файл с набором русских слов(имена существительные, им.падеж)
Одна строка файла содержит одно слово.

Задание:
Написать программу которая выводит список слов,
каждый элемент списка которого - это новое слово,
которое состоит из двух сцепленных в одно, которые имеются в текстовом файле.
Порядок вывода слов НЕ имеет значения

Например, текстовый файл содержит слова:
ласты
стык
стыковка
баласт
кабала
карась

Пользователь вводмт первое слово: ласты
Программа выводит:
ластык
ластыковка

Пользователь вводмт первое слово: кабала
Программа выводит:
кабаласты
кабаласт

Пользователь вводмт первое слово: стыковка
Программа выводит:
стыковкабала
стыковкарась

"""


def find_concatenated_words(user_word: str, list_word: str):
    for num in range(1, len(user_word)):
        try:
            if user_word[-num:] == list_word[:num]:
                return num
        except IndexError:
            return False
    return False


def concatenate(user_word: str, list_word: str, num: int):
    return user_word[:-num] + list_word


def main():
    with open(r"your_path\words.txt", 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file]

    first_word = input('Enter first word: ')
    for item in words:
        result = find_concatenated_words(first_word, item)
        if result:
            print(concatenate(first_word, item, result))


main()
