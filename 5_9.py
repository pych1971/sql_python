import sqlite3

"""Создание базы данных exchanger.db"""

db = sqlite3.connect('exchanger.db')
cur = db.cursor()

"""Создание таблицы users_balance и добавление пользователя c 100000 рублей, 1000 долларов, 1000 евро"""

cur.execute("""CREATE TABLE IF NOT EXISTS users_balance(
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Balance_RUB FLOAT NOT NULL,
    Balance_USD FLOAT NOT NULL,
    Balance_EUR FLOAT NOT NULL);
""")
cur.execute("""SELECT * FROM users_balance WHERE UserID = 1;""")
try:
    if cur.fetchone()[0] == 1:
        print('Пользователь уже существует')
except TypeError:
    cur.execute("""INSERT INTO users_balance(Balance_RUB , Balance_USD, Balance_EUR)
        VALUES(100000, 1000, 1000);
    """)
db.commit()

cur.execute("""SELECT * FROM users_balance""")
user_currencies = cur.fetchall()

"""Выводим приветствие с курсами валют"""

print("""\nДобро пожаловать в наш обменный пункт, курс валют следующий:\n
1 USD = 70 RUB
1 EUR = 80 RUB
1 USD = 0,87 EUR
1 EUR = 1,15 USD""")

rates = ((0, 1 / 70, 1 / 80), (70, 0, 0.87), (80, 1.15, 0))

"""Получаем название валюты, которую пользователь желает получить"""

while True:
    try:
        in_currency = int(input("""\nВведите какую валюту желаете получить:\n
1. RUB
2. USD
3. EUR\n"""))
        if 1 <= in_currency <= 3:
            break
        else:
            print('Необходимо ввести число от 1 до 3!')
            continue
    except ValueError:
        print('Необходимо ввести число от 1 до 3!')
        continue

"""Получаем сумму валюты, которую пользователь желает получить"""

while True:
    try:
        in_sum = int(input("""\nКакая сумма Вас интересует?\n"""))
        if type(in_sum) == int:
            break
        else:
            print('Необходимо ввести целое число!')
            continue
    except ValueError:
        print('Необходимо ввести целое число!')
        continue

"""Получаем название валюты, которую пользователь готов предложить взамен"""

while True:
    try:
        out_currency = int(input("""\nКакую валюту готовы предложить взамен?\n
1. RUB
2. USD
3. EUR\n"""))
        if out_currency == in_currency:
            print('Невозможно производить обмен двух одинаковых валют!')
            continue
        elif 1 <= out_currency <= 3:
            break
        else:
            print('Необходимо ввести число от 1 до 3!')
            continue
    except ValueError:
        print('Необходимо ввести число от 1 до 3!')
        continue

"""Переводим деньги между валютами и передаём новые данные в таблицу"""

user_currencies_new = list(user_currencies[0])

if in_sum * rates[in_currency - 1][out_currency - 1] > user_currencies[0][out_currency]:
    print('У вас недостаточно средств!')
else:
    user_currencies_new[in_currency] += in_sum
    user_currencies_new[out_currency] -= in_sum * rates[in_currency - 1][out_currency - 1]

cur.execute("""UPDATE users_balance SET Balance_RUB = ?, Balance_USD = ?, Balance_EUR = ? WHERE UserID = 1""",
            user_currencies_new[1:])
db.commit()
