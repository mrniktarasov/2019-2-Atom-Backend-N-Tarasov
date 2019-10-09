import unittest
from TicTacToe import TicTacToe

class TicTacToeTestCase(unittest.TestCase):

    def test_checkWin(self):
        TTTgame = TicTacToe()
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
        self.assertEqual(TTTgame.checkWin(), False)


if __name__ == '__main__':
    unittest.main()