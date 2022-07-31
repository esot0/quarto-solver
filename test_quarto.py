from quarto import *

def test_horizontal_win():
    g = Game()
    g.choose_piece(1)
    g.place_piece((0,0))
    check = g.check_horizontal((0,0))

    g.choose_piece(2)
    g.place_piece((0,1))
    check = g.check_horizontal((0,0))

    g.choose_piece(3)
    g.place_piece((0,2))
    check = g.check_horizontal((0,0))
    assert g.winnable_positions[0] and check

def test_horizontal_loss():
    g = Game()
    g.choose_piece(1)
    g.place_piece((0,0))
    check = g.check_horizontal((0,0))

    g.choose_piece(16)
    g.place_piece((0,1))
    check = g.check_horizontal((0,1))

    g.choose_piece(3)
    g.place_piece((0,2))
    check = g.check_horizontal((0,2))

    assert not g.winnable_positions[0] and not check

def test_vertical_win():
    g = Game()
    g.choose_piece(1)
    g.place_piece((0,0))

    g.choose_piece(2)
    g.place_piece((1,0))

    g.choose_piece(3)
    g.place_piece((2,0))

    g.choose_piece(4)
    g.place_piece((3,0))
    check = g.check_vertical((0,0))

    assert g.winnable_positions[4] and check

def test_vertical_loss():
    g = Game()

    g.choose_piece(1)
    g.place_piece((0,0))

    g.choose_piece(16)
    g.place_piece((1,0))

    g.choose_piece(3)
    g.place_piece((2,0))
    check = g.check_vertical((0,0))

    assert not g.winnable_positions[4] and not check

def test_maj_diagonal_win():
    g = Game()

    g.choose_piece(1)
    g.place_piece((0,0))

    g.choose_piece(2)
    g.place_piece((1,1))

    g.choose_piece(3)
    g.place_piece((2,2))

    g.choose_piece(4)
    g.place_piece((3,3))
    check = g.check_maj_diagonal((0,0))

    assert g.winnable_positions[8] and check

def test_min_diagonal_win():
        g = Game()

        g.choose_piece(1)
        g.place_piece((3,0))

        g.choose_piece(2)
        g.place_piece((2,1))

        g.choose_piece(3)
        g.place_piece((1,2))

        g.choose_piece(4)
        g.place_piece((0,3))
        check = g.check_maj_diagonal((0,0))

        assert g.winnable_positions[9] and check

def test_maj_diagonal_loss():
    g = Game()

    g.choose_piece(1)
    g.place_piece((0,0))

    g.choose_piece(16)
    g.place_piece((1,1))

    g.choose_piece(3)
    g.place_piece((2,2))
    check = g.check_maj_diagonal((0,0))
    assert not g.winnable_positions[8] and not check

def test_min_diagonal_loss():
    g = Game()

    g.choose_piece(1)
    g.place_piece((3,0))

    g.choose_piece(16)
    g.place_piece((2,1))

    g.choose_piece(3)
    g.place_piece((1,2))

    g.choose_piece(4)
    g.place_piece((0,3))

    check = g.check_min_diagonal((0,0))
    assert not g.winnable_positions[9] and not check


def test_win():
    pass
