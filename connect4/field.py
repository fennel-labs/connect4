import numpy as np
from enum import IntEnum, unique

class Field:

    WIDTH = 7
    HEIGHT = 5
    WIN_LENGTH = 4
    

    @unique
    class Player(IntEnum):
        P1 = -1
        P2 = +1

    def __init__(self):
        self.grid = np.zeros((self.HEIGHT, self.WIDTH), dtype=np.int8)
        self.filllevel = np.zeros(self.WIDTH, dtype=np.int8)
        self.count_moves = 0

    
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
        self.count_moves += 1
        return True

    def check(self):
        # directions where winning conditions can occur
        directions = [ 
            # (direction in grid, x/width-limits, y/height-limits)
            ((0,1),  (0,self.WIDTH-self.WIN_LENGTH), (0, self.HEIGHT-1)),               # --ros
            ((1,0),  (0,self.WIDTH-1),               (0, self.HEIGHT-self.WIN_LENGTH)), # |-rows
            ((1,1),  (0,self.WIDTH-self.WIN_LENGTH), (0, self.HEIGHT-self.WIN_LENGTH)), # /-rows
            ((-1,1), (0,self.WIDTH-self.WIN_LENGTH), (self.WIN_LENGTH-1,self.HEIGHT-1)) # \-rows
            ]

        # iterate row-wise over field (better than colwise because rows tend to be filled first)
        for col in range(0, self.WIDTH):
            for row in range(0, self.HEIGHT):
                pos_start = (row, col) # current grid position that acts as start point
                player = self.grid[pos_start] # player at the current grid position
                
                # if this field has no chip, there is nothing to do here
                if player == 0:
                    continue

                # from the grid position check all directions
                for direction in directions:
                    # check wether a winning combination fits in
                    if(col >= direction[1][0] and col <= direction[1][1] and
                       row >= direction[2][0] and row <= direction[2][1]):
                        # the direction in where to look for winning combination
                        increment = direction[0]
                        pos = pos_start
                        num_consecutive = 1
                        # go self.WIN_LENGTH-1 steps in the current direction
                        for _ in range(0,self.WIN_LENGTH-1): # (WIN_LENGTH-1) iterations
                            pos = tuple(np.add(pos,increment))
                            pos_value = self.grid[pos]
                            if pos_value != player:
                                # the player changed, so there can't be a winning combination here
                                break
                            num_consecutive += 1
                        if num_consecutive == self.WIN_LENGTH:
                            return player
                    else:
                        # winning combination can't fit in
                        continue
        # no player was found
        return 0

                