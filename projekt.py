class MoveError(Exception):
    """Исключение вылетающее при попытке хода в занятую клетку"""
    pass


stat = {'win_x': 0, 'win_o': 0, 'draw': 0}
"""Статистика игр"""

player = ""
"""Текущий игрок X или O"""

win = False
"""Флаговая переменная окончания текущей игры"""



def first_move(x):
    """
    Устанавливает игрока, который делает первый ход
    И здесь же выкидывает ошибки если что-то не так

    :param x: 1 - крестики, 2 - нолики, stop - выход
    :type x: str

    :returns: строка с текстом о том, кто ходит первым
    :rtype: str

    :raises ValueError: если введено другое значение (не 1 и не 2)
    :raises SystemExit: если введено stop
    :raises KeyboardInterrupt: Если введено Ctrl+C
    """
    global player

    if x == 'stop':
        raise SystemExit

    if x not in ['1', '2']:
        raise ValueError

    x = int(x)
    if x == 1:
        player = 'X'
        return "Первый ход делают Крестики"
    if x == 2:
        player = 'O'
        return "Первый ход делают Нолики"

def first_move_checker():
    """
    Запрашивает у пользователя, кто делает первый ход и ловит ошибку в случае чего
    (использует в работе first_move)
    """
    print("Выберите кто ходит первым")
    print("Нажми 1 если крестики, нажми 2 если нолики. (введи stop - если хочешь выйти)")
    while True:
        try:
            s = input()
            print(first_move(s))
            break
        except SystemExit:
            exit()
        except KeyboardInterrupt:
            exit()
        except ValueError:
            print("Ошибка: Введите 1 или 2")
    print_field(field)


def make_move(field, x):
    """
    Выполняет ход текущего игрока по указанным координатам и проверяет их корректность
    Тут она тоже выкидывает ошибки чтобы мы уже в чекере их поймали

    :param field: игровое поле
    :type field: list[list[str]]
    :param  x: координаты хода в формате str - row, col либо stop
    :type x: str

    :raises ValueError: если формат ввода неверный или координаты не подходят
    :raises MoveError: если выбранная клетка занята
    :raises SystemExit: если введено stop
    :raises KeyboardInterrupt: если пользователь ввёл Ctrl+C

    :returns: обновлённое поле
    :rtype: list[list[str]]
    """
    
    global player

    if x == 'stop':
        raise SystemExit

    row, col = x.split()
    if row not in ['0', '1', '2'] or col not in ['0', '1', '2']:
        raise ValueError

    row = int(row)
    col = int(col)
    if field[row][col] != '_':
        raise MoveError
    field[row][col] = player
    return field


def make_move_checker(field):
    """
    Запрашивает координаты хода (ловя ошибки которые могут возникнуть
    в make_move)
    Она использует в работе make_move

    Формат ввода: два числа от 0 до 2 через пробел
    
    :param field: текущее игровое поле
    :type field: list[list[str]]

    :returns: поле после корректного хода
    :rtype: list[list[str]]

    """
    while True:
        try:
            s = input()
            make_move(field, s)
            return field
        except SystemExit:
            exit()
        except KeyboardInterrupt:
            exit()
        except MoveError:
            print("Ошибка: Клетка занята")
        except ValueError:
            print("Ошибка: Неверные корды")





def is_win(field):
    """
    Проверяет состояние поля - победа, ничья или продолжение игры
    Ещё тут она переключает игрока

    :param field: текущее игровое поле 3 на 3
    :type field: list[list[str]]

    :returns: текстовое сообщение с ситуацией в игре - ничья, победа или чей ход
    :rtype: str
    """
    global player
    global win

    # Проверка победы крестиков
    if (field[0][0] == "X" and field[1][0] == "X" and field[2][0] == "X") or \
        (field[0][1] == "X" and field[1][1] == "X" and field[2][1] == "X") or \
        (field[0][2] == "X" and field[1][2] == "X" and field[2][2] == "X") or \
        (field[0][0] == "X" and field[0][1] == "X" and field[0][2] == "X") or \
        (field[1][0] == "X" and field[1][1] == "X" and field[1][2] == "X") or \
        (field[2][0] == "X" and field[2][1] == "X" and field[2][2] == "X") or \
        (field[0][0] == "X" and field[1][1] == "X" and field[2][2] == "X") or \
        (field[0][2] == "X" and field[1][1] == "X" and field[2][0] == "X"):
        stat['win_x'] += 1
        win = True
        return "Выиграли крестики!!!"

    # Проверка победы ноликов
    if (field[0][0] == "O" and field[1][0] == "O" and field[2][0] == "O") or \
        (field[0][1] == "O" and field[1][1] == "O" and field[2][1] == "O") or \
        (field[0][2] == "O" and field[1][2] == "O" and field[2][2] == "O") or \
        (field[0][0] == "O" and field[0][1] == "O" and field[0][2] == "O") or \
        (field[1][0] == "O" and field[1][1] == "O" and field[1][2] == "O") or \
        (field[2][0] == "O" and field[2][1] == "O" and field[2][2] == "O") or \
        (field[0][0] == "O" and field[1][1] == "O" and field[2][2] == "O") or \
        (field[0][2] == "O" and field[1][1] == "O" and field[2][0] == "O"):
        stat['win_o'] += 1
        win = True
        return "Выиграли нолики!!!"

    # Проверка ничьей
    count = sum(1 for i in range(3) for j in range(3) if field[i][j] != "_")
    if count == 9:
        stat['draw'] += 1
        win = True
        return "Ничья ):"

    # Переключение игрока
    if player == 'O':
        player = 'X'
        return 'Ход крестиков'
    else:
        player = 'O'
        return 'Ход ноликов'


def print_field(field):
    """
    Печатает игровое поле

    :param field: текущее игровое поле
    :type field: list[list[str]]
    """
    print('    0 1 2')
    print('  *********')
    for i in range(0, 3):
        print(i, '*', *field[i], '*')
    print('  *********')




def game(field):
    """
    Запускает одну игру «Крестики-нолики»
    Она ничего не возвращает но сделана для удобного повтора игры через меню
    
    :param field: игровое поле (внутри функции инициализируется заново)
    :type field: list[list[str]]
    """
    global win

    first_move_checker()
    win = False
    field = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    
    print("Введите координаты в формате строка столбец Например - 0 2. (введи stop, если хочешь выйти)")
    while win is False:
        field = make_move_checker(field)
        print_field(field)
        res = is_win(field)
        print(res)


# Основная программа
if __name__ == '__main__':

    print("Добро пожаловать в игру Крестики Нолики!")
#Это поле берёт first_move_checker
    field = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
        ]

    game(field)

    # Меню
    while True:
        print("Хотите сыграть ещё?")
        print("1 - Посмотреть статистику")
        print("2 - Начать новую игру")
        print("3 - Выйти")

        try:
            choice = int(input())
            """Выбор для меню 1 - Статистика 2 - Новая игра 3 - Выход из игры"""
            if choice not in [1, 2, 3]:
                raise ValueError
            if choice == 1:
                print("\nСтатистика игр:")
                print(f"Побед крестиков: {stat['win_x']}")
                print(f"Побед ноликов: {stat['win_o']}")
                print(f"Ничьих: {stat['draw']}")
                # После показа статистики продолжаем цикл, чтобы снова показать меню
            elif choice == 2:
                game(field)
            elif choice == 3:
                print("Спасибо за игру!")
                exit()
        except KeyboardInterrupt:
            exit()
        except ValueError:
            print("Ошибка: Введите 1, 2 или 3")
