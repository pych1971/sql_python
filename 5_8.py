import sqlite3

"""Создание базы данных registration.db"""

db = sqlite3.connect('registration.db')
cur = db.cursor()

"""Создание таблицы users_data и добавление пользователя Ivan"""

cur.execute("""CREATE TABLE IF NOT EXISTS users_data(
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Login TEXT NOT NULL,
    Password TEXT NOT NULL,
    Code INTEGER NOT NULL);
""")
cur.execute("""SELECT * FROM users_data WHERE UserID = 1;""")
try:
    if cur.fetchone()[1] == 'Ivan':
        print('Пользователь Ivan уже существует')
except TypeError:
    cur.execute("""INSERT INTO users_data(Login , Password, Code)
        VALUES('Ivan', 'qwer1234', '1234');
    """)

db.commit()

"""Вывод меню и выбор действия"""

print('Ваши действия?\n')
print('1. Регистрация нового пользователя')
print('2. Авторизация в системе')
print('3. Восстановление пароля по коду\n')

"""Добиваемся, чтобы пользователь выбрал число от 1 до 3"""

while True:
    try:
        decision = int(input('Введите число от 1 до 3:'))
        if 1 <= decision <= 3:
            break
        else:
            print('Необходимо ввести число от 1 до 3!')
            continue
    except ValueError:
        print('Необходимо ввести число от 1 до 3!')
        continue
cur.execute("""SELECT * FROM users_data""")
user_all = cur.fetchall()
if decision == 1:  # Регистрация нового пользователя
    print('\nРегистрация нового пользователя\n')
    j = True
    while j:
        user = input('Введите имя пользователя:')
        j = False
        if user == '':
            j = True
            print('Имя пользователя не может быть пустым!')
        for i in range(len(user_all)):
            if user == user_all[i][1]:
                print('Такой пользователь уже существует')
                j = True
                break
    while True:
        password = input('Введите пароль:')
        if password != '':
            break
        else:
            print('Пароль не может быть пустым!')
            continue
    while True:
        try:
            code = int(input('Введите код для проверки (целое число):'))
            break
        except ValueError:
            print('Код должен быть целым числом!')
            continue
    new_user = (user, password, code)
    cur.execute(f"""INSERT INTO users_data(Login , Password, Code)
        VALUES(?, ?, ?);""", new_user)
    db.commit()
    print('Пользователь создан')
elif decision == 2:  # Авторизация в системе
    print('\nАвторизация в системе\n')
    user = input('Введите имя пользователя:')
    password = input('Введите пароль:')
    j = False
    for i in range(len(user_all)):
        if user == user_all[i][1] and password == user_all[i][2]:
            print('\nАвторизация прошла успешно\n')
            j = True
    if j == False:
        print('\nОшибка авторизации\n')
elif decision == 3:  # Восстановление пароля по коду
    print('\nВосстановление пароля по коду\n')
    user = input('Введите имя пользователя:')
    code = int(input('Введите код:'))
    j = False
    for i in range(len(user_all)):
        if user == user_all[i][1] and code == user_all[i][3]:
            password = input('Введите новый пароль:')
            update_params = (password, user)
            cur.execute("""UPDATE users_data SET Password = ? WHERE Login = ?""", update_params)
            db.commit()
            print('\nПароль успешно изменён\n')
            j = True
    if j == False:
        print('\nВведены неверные данные\n')
