import unittest
from solutions.kyu8 import move


class MoveTestCase(unittest.TestCase):
    def test_move(self):
        self.assertEqual(move.move(0, 4), 8)
        self.assertEqual(move.move(3, 6), 15)
        self.assertEqual(move.move(2, 5), 12)


if __name__ == '__main__':
    unittest.main()
