import sqlite3

"""Подключение к существующей базе данных"""

db = sqlite3.connect(r'c:\Users\Oleg\YandexDisk\Programming\SQL\sql_join.db')  # Подключение к базе данных
print('Подключились к базе данных')
cur = db.cursor()  # Переменная для управления базой данных
#
# cur.execute("""SELECT * FROM Persons;""")  # Запрос для получения содержимого таблицы Students
# result = cur.fetchall()  # Результат запроса
# print(result)

"""Объеднинение таблиц INNER JOIN"""
cur.execute("""SELECT PersonsID, First_name, Position
FROM Persons
INNER JOIN Positions ON PositionID = Position_ref""")
result_all = cur.fetchall()
for result in result_all:
    print(result)
print('*' * 50)

"""Объеднинение таблиц LEFT JOIN"""
cur.execute("""SELECT PersonsID, First_name, Position
FROM Persons
LEFT JOIN Positions ON PositionID = Position_ref""")
result_all = cur.fetchall()
for result in result_all:
    print(result)
print('*' * 50)

"""Объеднинение таблиц RIGHT JOIN"""
cur.execute("""SELECT PersonsID, First_name, Position
FROM Positions
LEFT JOIN Persons ON PositionID = Position_ref""")
result_all = cur.fetchall()
for result in result_all:
    print(result)
print('*' * 50)

"""Объеднинение таблиц FULL (UNION) JOIN"""
cur.execute("""SELECT PersonsID, First_name, Position
FROM Persons
LEFT JOIN Positions ON PositionID = Position_ref
UNION
SELECT PersonsID, First_name, Position
FROM Positions
LEFT JOIN Persons ON PositionID = Position_ref""")
result_all = cur.fetchall()
for result in result_all:
    print(result)
print('*' * 50)

"""Разница между таблицами"""
cur.execute("""SELECT PersonsID, First_name, Position
FROM Persons
LEFT JOIN Positions ON PositionID = Position_ref
WHERE PositionID IS NULL
UNION
SELECT PersonsID, First_name, Position
FROM Positions
LEFT JOIN Persons ON PositionID = Position_ref
WHERE Position_ref IS NULL
""")
result_all = cur.fetchall()
for result in result_all:
    print(result)
print('*' * 50)