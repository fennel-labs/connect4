from connect4.field import Field
import unittest
import numpy as np

class TestField(unittest.TestCase):

    def setUp(self):
        self.field = Field()

    def test_legal_placement(self):
        self.field.place(1,Field.Player.P1)
        self.field.place(1,Field.Player.P2)
        self.field.place(2,Field.Player.P1)
        self.field.place(1,Field.Player.P1)
        self.field.place(1,Field.Player.P2)
        self.field.place(1,Field.Player.P1)

        grid_expected = np.zeros_like(self.field.grid)
        grid_expected[0,1] = Field.Player.P1
        grid_expected[1,1] = Field.Player.P2
        grid_expected[0,2] = Field.Player.P1
        grid_expected[2,1] = Field.Player.P1
        grid_expected[3,1] = Field.Player.P2
        grid_expected[4,1] = Field.Player.P1

        self.assertTrue(np.array_equal(self.field.grid, grid_expected))

    def test_illegal_placement(self):
        with self.assertRaises(ValueError):
            self.field.place(-1, Field.Player.P1)
        with self.assertRaises(ValueError):
            self.field.place(Field.WIDTH + 1, Field.Player.P1)
        with self.assertRaises(ValueError):
            self.field.place(0, 20)
    
    def test_rejected_placement(self):
        for col in range(0,self.field.WIDTH):
            # fill up one row and check whether return values fit
            for _ in range(0,self.field.HEIGHT):
                self.assertTrue(self.field.place(col,Field.Player.P1))
            self.assertFalse(self.field.place(col,Field.Player.P1))
            self.assertFalse(self.field.place(col,Field.Player.P2))

    def test_checks(self):
        # horizontal test
        increment = (0,1)
        for col in range(0,Field.WIDTH - Field.WIN_LENGTH + 1):
            for row in range(0, Field.HEIGHT):
                self.field = Field()
                pos = (row, col)
                # put 4 chips in a winning condtion into the field
                for _ in range(0,Field.WIN_LENGTH):
                    self.assertEqual(self.field.check(),0)
                    self.field.grid[pos] = Field.Player.P1
                    pos = tuple(np.add(pos,increment))
                #print(self.field)
                self.assertEqual(self.field.check(),Field.Player.P1)

        # vertical test
        increment = (1,0)
        for col in range(0,Field.WIDTH):
            for row in range(0, Field.HEIGHT - Field.WIN_LENGTH + 1):
                self.field = Field()
                pos = (row, col)
                # put 4 chips in a winning condtion into the field
                for _ in range(0,Field.WIN_LENGTH):
                    self.assertEqual(self.field.check(),0)
                    self.field.grid[pos] = Field.Player.P2
                    pos = tuple(np.add(pos,increment))
                #print(self.field)
                self.assertEqual(self.field.check(),Field.Player.P2)  

        # diagnoal 1 test
        increment = (1,1)
        for col in range(0,Field.WIDTH - Field.WIN_LENGTH + 1):
            for row in range(0, Field.HEIGHT - Field.WIN_LENGTH + 1):
                self.field = Field()
                pos = (row, col)
                # put 4 chips in a winning condtion into the field
                for _ in range(0,Field.WIN_LENGTH):
                    self.assertEqual(self.field.check(),0)
                    self.field.grid[pos] = Field.Player.P1
                    pos = tuple(np.add(pos,increment))
                #print(self.field)
                self.assertEqual(self.field.check(),Field.Player.P1)  

        # diagnoal 2 test
        increment = (-1,1)
        for col in range(0,Field.WIDTH - Field.WIN_LENGTH + 1):
            for row in range(Field.WIN_LENGTH-1, Field.HEIGHT):
                self.field = Field()
                pos = (row, col)
                # put 4 chips in a winning condtion into the field
                for _ in range(0,Field.WIN_LENGTH):
                    self.assertEqual(self.field.check(),0)
                    self.field.grid[pos] = Field.Player.P2
                    pos = tuple(np.add(pos,increment))
                #print(self.field)
                self.assertEqual(self.field.check(),Field.Player.P2)  


if __name__ == '__main__':
    unittest.main()
    