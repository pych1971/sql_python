import sqlite3

# """Подключение к существующей базе данных"""
#
# db = sqlite3.connect(r'c:\Users\Oleg\YandexDisk\Programming\SQL\qa_testing.db')  # Подключение к базе данных
# print('Подключились к базе данных')
# cur = db.cursor()  # Переменная для управления базой данных
# cur.execute("""SELECT * FROM Students;""")  # Запрос для получения содержимого таблицы Students
# result = cur.fetchall()  # Результат запроса
# print(result)
# print(type(result))
#
# """Создание новой базы данных"""
#
# db = sqlite3.connect('test_sql.db')  # Создание базы данных
# print('Подключились к базе данных')
# cur = db.cursor()  # Переменная для управления базой данных
#
# """Создание таблицы"""
#
# cur.execute("""CREATE TABLE IF NOT EXISTS Students(
#     StudentsID INTEGER PRIMARY KEY,
#     First_name TEXT NOT NULL,
#     Last_name TEXT NOT NULL);
# """)
# db.commit()  # Сохренение запроса
# print('Создание таблицы Students')
# """Заполнение таблицы Students"""
# cur.execute("""INSERT INTO Students(First_name, Last_name)
#     VALUES('Petr', 'Petrov');""")
# db.commit()
#
# cur.execute("""CREATE TABLE IF NOT EXISTS Students1(
#     StudentsID INTEGER PRIMARY KEY AUTOINCREMENT,
#     First_name TEXT NOT NULL,
#     Last_name TEXT NOT NULL);
# """)
# db.commit()  # Сохренение запроса
# print('Создание таблицы Students')
#
# """НЕБЕЗОПАСНЫЙ СПОСОБ - Заполнение таблицы Students"""
#
# cur.execute("""INSERT INTO Students1(First_name, Last_name)
#     VALUES('Petr', 'Petrov');""")
# db.commit()
#
# """БЕЗОПАСНЫЙ СПОСОБ - Заполнение таблицы Students"""
#
# date_students = ('Semen', 'Semenov')
# date_students = [('Alex', 'Aleksandrov'), ('Olga', 'Olgina')]
# cur.executemany("""INSERT INTO Students1(First_name, Last_name)
#     VALUES(?, ?);""", date_students)
# db.commit()
# print('Добавление новых данных в таблицу')
#
# """Отправка нескольких запросов"""
#
# cur.executescript("""CREATE TABLE IF NOT EXISTS Students2(
#     StudentsID INTEGER PRIMARY KEY AUTOINCREMENT,
#     First_name TEXT NOT NULL,
#     Last_name TEXT NOT NULL);
#     INSERT INTO Students2(First_name, Last_name)
#     VALUES('Petr', 'Petrov');
# """)
# db.commit()  # Сохренение запроса
# print('Создание таблицы Students')
#
# """Изменение данных в таблице"""
#
# update_params = ('Sokolova', 4)
# cur.execute("""UPDATE Students1 SET Last_name = ? WHERE StudentsID = ?""", update_params)
# # cur.execute("""UPDATE Students1 SET Last_name = 'Orlova' WHERE StudentsID = 4""")
# db.commit()  # Сохренение запроса
# print('Изменение данных в таблице')
#
# """Удаление данных в таблице"""
#
# delete_params = '3'
# cur.execute("""DELETE FROM Students1 Where StudentsID = ?;""", delete_params)
# # cur.execute("""DELETE FROM Students1 Where StudentsID = 4""")
# db.commit()  # Сохренение запроса
# print('Удаление данных в таблице')
#
# """Удаление таблицы"""
#
# cur.execute("""DROP TABLE Students2""")
# db.commit()  # Сохренение запроса
# print('Удаление таблицы')

"""Подключение к существующей базе данных"""

db = sqlite3.connect(r'c:\Users\Oleg\YandexDisk\Programming\SQL\qa_testing.db')  # Подключение к базе данных
print('Подключились к базе данных')
cur = db.cursor()  # Переменная для управления базой данных

# cur.execute("""SELECT * FROM Students;""")  # Запрос для получения содержимого таблицы Students
cur.execute("""SELECT * FROM Students WHERE StudentsID = 1;""")
# result_one = cur.fetchone()  # Одно значение
# result_many = cur.fetchmany(2)  # Несколько значений
result_all = cur.fetchall()  # Все значения
# r = result_one[1]
# print(result_one)
# print(result_many)
print(result_all)
