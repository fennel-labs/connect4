import numpy as np
from enum import IntEnum, unique

class Field:

    WIDTH = 7
    HEIGHT = 5

    @unique
    class Player(IntEnum):
        P1 = -1
        P2 = +1

    def __init__(self):
        self.grid = np.zeros((self.HEIGHT, self.WIDTH), dtype=np.int8)
        self.filllevel = np.zeros(self.WIDTH, dtype=np.int8)

    
    def __str__(self):
        array = np.flipud(self.grid) # flip it
        array_subs = np.copy(array) # create a copy here, not a view
        # get rid of any minuses and use standardized numbers
        array_subs[array == Field.Player.P1] = 1
        array_subs[array == Field.Player.P2] = 2
        # create string and modify it to a nice looking representation
        string = np.array2string(array_subs)
        string = string.replace("0", " ")
        string = string.replace("1", "O")
        string = string.replace("2", "X")
        return string

    def place(self, slot, player):
        if slot < 0 or slot >= Field.WIDTH:
            raise ValueError('Illegal slot number.')
        if player != Field.Player.P1 and player != Field.Player.P2:
            raise ValueError('Unknown player.')



        # return false if capacity is exceeded
        if self.filllevel[slot] >= Field.HEIGHT:
            return False
        
        # capacity is not yet exceeded
        self.grid[self.filllevel[slot], slot] = player
        self.filllevel[slot] += 1
        return True

    def check(self):
        # TODO: implement
        return



# test = Field()
# print(test.place(1,Field.Player.P1))
# print(test)
# print(test.place(1,Field.Player.P2))
# print(test)
# print(test.place(2,Field.Player.P1))
# print(test)
# print(test.place(1,Field.Player.P1))
# print(test)
# print(test.place(1,Field.Player.P2))
# print(test)
# print(test.place(1,Field.Player.P1))
# print(test)
# print(test.place(1,Field.Player.P2))
# print(test)

#test.place(-1,Field.Player.P1)
#test.place(7,Field.Player.P1)
#test.place(0, 3)
