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

        grid_expected = np.zeros((Field.HEIGHT, Field.WIDTH), dtype=np.int8)
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
            self.field.place(10, Field.Player.P1)
        with self.assertRaises(ValueError):
            self.field.place(0, 20)


if __name__ == '__main__':
    unittest.main()
    

#test.place(-1,Field.Player.P1)
#test.place(7,Field.Player.P1)
#test.place(0, 3)
