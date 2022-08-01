class Tree():

    def __init__(self):
        self.data = "quartos"
        self.children = []

    def __str__(self):
        return str(self.data)

    def leaves(self):
        print(self)
        if(len(self.children)==0):
            return self

        for child in self.children:
            print(child.leaves())

    def insert(node):
        pass

    def remove(data):
        pass


t = Tree()
t.data = 2

seven = Tree()
seven.data = 7

five = Tree()
five.data = 5

six = Tree()
six.data = 6

eight = Tree()
eight.data = 8

five.children = [eight, six]

t.children = [seven, five]

t.leaves()

class GameState():
    pass #separate class or build into determine_next_player# every choice is a GameStat

    #Piece, board, maybe playe

    """
    Tree
    Pick piece = parent
    children = places for children to be Pick
    Not interested in noLose or winIfyoucan
    prune the tree!!!!!!!!!!


    """e
