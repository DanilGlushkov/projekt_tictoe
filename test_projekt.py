import pytest
#from unittest.mock import patch

import projekt as m


def reset_globals():
    m.stat.clear()
    m.stat.update({'win_x': 0, 'win_o': 0, 'draw': 0})
    m.player = ""
    m.win = False


def empty_field():
    return [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]


def test_first_move_x():
    reset_globals()
    msg = m.first_move('1')
    assert msg == "Первый ход делают Крестики"
    assert m.player == "X"

def test_first_move_o():
    reset_globals()
    msg = m.first_move('2')
    assert msg == "Первый ход делают Нолики"
    assert m.player == "O"
    

'''
убираем, так как переделали first_move() и теперь тестируем ее

def test_first_move_checker_x():
    reset_globals()
    msg = m.first_move('1')
    assert msg == "Первый ход делают Крестики"
    assert m.player == "X"


def test_first_move_checker_o():
    reset_globals()
    msg = m.first_move('2')
    assert msg == "Первый ход делают Нолики"
    assert m.player == "O"
'''

def test_first_move_wrong_value1():
    reset_globals()
    with pytest.raises(ValueError):
        rez = m.first_move("123")

def test_first_move_wrong_value2():
    reset_globals()
    with pytest.raises(ValueError):
        rez = m.first_move("start")

def test_first_move_wrong_value3():
    reset_globals()
    with pytest.raises(SystemExit):
        rez = m.first_move("stop")

#добавить когда стоп

def test_make_move_ok():
    reset_globals()
    f = empty_field()
    m.player = "X"
    res = m.make_move(f, '1 1')
    f = [
        ["_", "_", "_"],
        ["_", "X", "_"],
        ["_", "_", "_"],
    ]
    assert res == f


def test_make_move_out_of_range1():
    reset_globals()
    f = empty_field()
    m.player = "X"
    with pytest.raises(ValueError):
        res = m.make_move(f, '5 0')

def test_make_move_out_of_range2():
    reset_globals()
    f = empty_field()
    m.player = "X"
    with pytest.raises(ValueError):
        res = m.make_move(f, 'S KJLBDSFZKJH')


def test_make_move_cell_busy():
    reset_globals()
    f = empty_field()
    f[0][0] = "O"
    m.player = "X"
    with pytest.raises(m.MoveError):
        res = m.make_move(f, '0 0')

def test_make_move_stop():
    reset_globals()
    f = empty_field()
    with pytest.raises(SystemExit):
        res = m.make_move(f, 'stop')


#Проверка выигрыша по горизонталям
def test_is_win_pobeda1():
    reset_globals()
    f = [["O", "_", "_"], ["X", "X", "X"], ["_", "_", "O"]]
    m.player = "X"
    msg = m.is_win(f)

    assert msg == "Выиграли крестики!!!"
    assert m.win is True
    assert m.stat["win_x"] == 1

def test_is_win_pobeda2():
    reset_globals()
    f = [["O", "O", "O"], ["_", "X", "X"], ["_", "_", "_"]]
    m.player = "O"
    msg = m.is_win(f)

    assert msg == "Выиграли нолики!!!"
    assert m.win is True
    assert m.stat["win_o"] == 1

def test_is_win_pobeda3():
    reset_globals()
    f = [["O", "_", "_"], ["O", "_", "O"], ["X", "X", "X"]]
    m.player = "X"
    msg = m.is_win(f)

    assert msg == "Выиграли крестики!!!"
    assert m.win is True
    assert m.stat["win_x"] == 1

#Проверка выигрыша по вертикалям
def test_is_win_pobeda4():
    reset_globals()
    f = [["O", "_", "_"], ["O", "X", "_"], ["O", "X", "_"]]
    m.player = "O"
    msg = m.is_win(f)
    assert msg == "Выиграли нолики!!!"
    assert m.win is True
    assert m.stat["win_o"] == 1

def test_is_win_pobeda5():
    reset_globals()
    f = [["_", "X", "_"], ["O", "X", "_"], ["O", "X", "_"]]
    m.player = "X"
    msg = m.is_win(f)
    assert msg == "Выиграли крестики!!!"
    assert m.win is True
    assert m.stat["win_x"] == 1

def test_is_win_pobeda6():
    reset_globals()
    f = [["_", "X", "O"], ["_", "_", "O"], ["_", "X", "O"]]
    m.player = "O"
    msg = m.is_win(f)
    assert msg == "Выиграли нолики!!!"
    assert m.win is True
    assert m.stat["win_o"] == 1

#Проверка выигрыша по диагоналям
def test_is_win_pobeda7():
    reset_globals()
    f = [["_", "_", "X"], ["_", "X", "O"], ["X", "_", "O"]]
    m.player = "X"
    msg = m.is_win(f)
    assert msg == "Выиграли крестики!!!"
    assert m.win is True
    assert m.stat["win_x"] == 1

def test_is_win_pobeda8():
    reset_globals()
    f = [["O", "_", "_"], ["X", "O", "_"], ["X", "_", "O"]]
    m.player = "O"
    msg = m.is_win(f)
    assert msg == "Выиграли нолики!!!"
    assert m.win is True
    assert m.stat["win_o"] == 1



    


  
#Проверка ничьи
def test_is_win_nichya():
    reset_globals()
    f = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"],
    ]
    m.player = "X"
    msg = m.is_win(f)

    assert msg == "Ничья ):"
    assert m.win is True
    assert m.stat["draw"] == 1


def test_is_win_prodolzhaetsya_igra():
    reset_globals()
    f = [
        ["_", "O", "X"],
        ["_", "_", "_"],
        ["O", "_", "_"],
    ]
    m.player = "O"
    msg = m.is_win(f)

    assert msg == "Ход крестиков"
    assert m.player == "X"
    assert m.win is False


