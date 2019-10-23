import unittest
from TicTacToe import TicTacToe

class TicTacToeTestCase(unittest.TestCase):

    def test_check_win(self):
        TTTgame = TicTacToe("user1", "user2")
        toc = True
        TTTgame.field = [toc, toc, toc,
                         4,   5,   6,
                         7,   8,   9 ]
        self.assertEqual(TTTgame.checkWin(), True)
        TTTgame.field = [ 1,   2,    3,
                          toc,  toc, toc,
                           7,   8,    9 ]
        self.assertEqual(TTTgame.checkWin(), True)
        TTTgame.field = [ 1, 2, 3,
                           4, 5, 6,
                           7, 8, 9 ]
        self.assertEqual(TTTgame.checkWin(), False)    
        TTTgame.field = [ 1, 2, 3,
                           4, 5, 6,
                           toc, toc, toc ]
        self.assertEqual(TTTgame.checkWin(), True)   
        TTTgame.field = [ toc, 2, 3,
                           toc, 5, 6,
                           toc, 8, 9 ]
        self.assertEqual(TTTgame.checkWin(), True)
        TTTgame.field = [ 1, toc, 3,
                           4, toc, 6,
                           7, toc, 9 ]
        self.assertEqual(TTTgame.checkWin(), True)
        TTTgame.field = [ 1, 2, toc,
                           4, 5, toc,
                           7, 8, toc ]
        self.assertEqual(TTTgame.checkWin(), True)
        TTTgame.field = [ toc, 2, 3,
                           4, toc, 6,
                           7, 8, toc ]
        self.assertEqual(TTTgame.checkWin(), True)
        TTTgame.field = [ 1, 2, toc,
                           4, toc, 6,
                           toc, 8, 9 ]
        self.assertEqual(TTTgame.checkWin(), True)
        TTTgame.field = [ 1, 2, 3,
                          4, "x", 6,
                         "x", 8, "x" ]
        self.assertFalse(TTTgame.checkWin())

    def test_check_field (self):
        TTTgame = TicTacToe("user1", "user2")
        TTTgame.field = [1,   2,   3,
                         4,   5,   6,
                         7,   8,   9 ]
        self.assertEqual(TTTgame.write_field (1, "X"), 0)
        self.assertEqual(TTTgame.write_field (2, "X"), 0)
        self.assertEqual(TTTgame.write_field (3, "X"), 0)
        self.assertEqual(TTTgame.write_field (4, "X"), 0)
        self.assertEqual(TTTgame.write_field (5, "X"), 0)
        self.assertEqual(TTTgame.write_field (6, "X"), 0)
        self.assertEqual(TTTgame.write_field (7, "X"), 0)
        self.assertEqual(TTTgame.write_field (8, "X"), 0)
        self.assertEqual(TTTgame.write_field (9, "X"), 0)

        self.assertEqual(TTTgame.write_field (0, "X"), 1)
        self.assertEqual(TTTgame.write_field (-1, "X"), 1)
        self.assertEqual(TTTgame.write_field (10, "X"), 1)

        self.assertEqual(TTTgame.write_field (1, "X"), 2)
        self.assertEqual(TTTgame.write_field (2, "X"), 2)
        self.assertEqual(TTTgame.write_field (3, "X"), 2)
        self.assertEqual(TTTgame.write_field (4, "X"), 2)
        self.assertEqual(TTTgame.write_field (5, "X"), 2)
        self.assertEqual(TTTgame.write_field (6, "X"), 2)
        self.assertEqual(TTTgame.write_field (7, "X"), 2)
        self.assertEqual(TTTgame.write_field (8, "X"), 2)
        self.assertEqual(TTTgame.write_field (9, "X"), 2)

if __name__ == '__main__':
    unittest.main()