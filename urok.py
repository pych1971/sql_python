import sqlite3

"""Подключение к существующей базе данных"""
db = sqlite3.connect(r'c:\Users\Oleg\YandexDisk\Programming\SQL\qa_testing.db')  # Подключение к базе данных
print('Подключились к базе данных')
cur = db.cursor()  # Переменная для управления базой данных
cur.execute("""SELECT * FROM Students;""")  # Запрос для получения содержимого таблицы Students
result = cur.fetchall()  # Результат запроса
print(result)
print(type(result))
