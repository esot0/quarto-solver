from quarto import *

"""

1 = None
2
3
4
5

1 - 2
2 - 3
3 - 4
4 - 5


"""
def test_horizontal_win():
    g = Game(Player(), Player())

    p1 = g.player1
    p2 = g.player2
    p2.choose_piece(1,g)

    p1.place_piece((0,0),g)
    p1.choose_piece(1,g)

    p2.place_piece((0,1),g)
    p2.choose_piece(1,g)

    p1.place_piece((0,2),g)

    check = g.check_horizontal((0,0))
    assert g.winnable_positions[0] and check

def test_horizontal_loss():
    g = Game(Player(), Player())

    p1 = g.player1
    p2 = g.player2

    p2.choose_piece(1,g)
    p1.place_piece((0,0),g)

    p1.choose_piece(13,g)
    p2.place_piece((0,1),g)

    p2.choose_piece(2,g)
    p1.place_piece((0,2),g)


    check = g.check_horizontal((0,2))

    assert not g.winnable_positions[0] and not check

def test_vertical_win():
    g = Game(Player(), Player())
    p1 = g.player1
    p2 = g.player2

    p2.choose_piece(1,g)
    p1.place_piece((0,0),g)

    p1.choose_piece(2,g)
    p2.place_piece((1,0),g)

    p2.choose_piece(3,g)
    p1.place_piece((2,0),g)

    p1.choose_piece(4,g)
    p2.place_piece((3,0),g)
    check = g.check_vertical((0,0))

    assert g.winnable_positions[4] and check

def test_vertical_loss():
    g = Game(Player(), Player())
    p1 = g.player1
    p2 = g.player2

    p2.choose_piece(1,g)
    p1.place_piece((0,0),g)

    p1.choose_piece(13,g)
    p2.place_piece((1,0),g)

    p1.choose_piece(3,g)
    p2.place_piece((2,0),g)
    check = g.check_vertical((0,0))

    assert not g.winnable_positions[4] and not check

def test_maj_diagonal_win():
    g = Game(Player(), Player())
    p1 = g.player1
    p2 = g.player2

    p2.choose_piece(1,g)
    p1.place_piece((0,0),g)

    p1.choose_piece(2,g)
    p2.place_piece((1,1),g)

    p2.choose_piece(3,g)
    p1.place_piece((2,2),g)

    p1.choose_piece(4,g)
    p2.place_piece((3,3),g)
    check = g.check_maj_diagonal((0,0))

    assert g.winnable_positions[8] and check

def test_min_diagonal_win():
    g = Game(Player(), Player())

    p1 = g.player1
    p2 = g.player2

    p2.choose_piece(1,g)
    p1.place_piece((3,0),g)

    p1.choose_piece(1,g)
    p2.place_piece((2,1),g)

    p2.choose_piece(1,g)
    p1.place_piece((1,2),g)

    p1.choose_piece(1,g)
    p2.place_piece((0,3),g)
    check = g.check_min_diagonal((0,0))

    assert g.winnable_positions[9] and check

def test_maj_diagonal_loss():
    g = Game(Player(), Player())
    p1 = g.player1
    p2 = g.player2

    p2.choose_piece(1,g)
    p1.place_piece((0,0),g)

    p1.choose_piece(13,g)
    p2.place_piece((1,1),g)

    p2.choose_piece(3,g)
    p1.place_piece((2,2),g)

    check = g.check_maj_diagonal((0,0))
    assert not g.winnable_positions[8] and not check

def test_min_diagonal_loss():
    g = Game(Player(), Player())
    p1 = g.player1
    p2 = g.player2

    p2.choose_piece(1,g)
    p1.place_piece((3,0),g)

    p1.choose_piece(13,g)
    p2.place_piece((2,1),g)

    p2.choose_piece(3,g)
    p1.place_piece((1,2),g)

    p1.choose_piece(4,g)
    p2.place_piece((0,3),g)

    check = g.check_min_diagonal((0,0))
    assert not g.winnable_positions[9] and not check


#Write xfail
def str_test():
    pass
def test_win():
    pass
