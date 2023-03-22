import unittest
import argparse

from main import solve_equation

class TestSolveEquation(unittest.TestCase):
   
    def test_solve_equation_1(self):
        self.assertEqual(
            solve_equation('7x - 2 = 21'),
            '7x - 2 = 21\nCleaning up the equation:\n7x - 2 = 21\nRearranging the equation so that all the terms are on one side:\n7x - 2 - 21 = 0\nCombining like terms:\n7x - 23 = 0\nSolving for x:\nx = 3.2857142857142856'
        )
   
    def test_solve_equation_2(self):
        self.assertEqual(
            solve_equation('2(4x + 3) + 6 = 24 -4x'),
            '2(4x + 3) + 6 = 24 -4x\nCleaning up the equation:\n2(4x+3)+6=24-4x\nRearranging the equation so that all the terms are on one side:\n8x + 12 + 6 + 4x - 24 = 0\nCombining like terms:\n12x - 6 = 0\nSolving for x:\nx = 0.5'
        )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve a linear equation')
    parser.add_argument('equation', help='the equation to solve')
    args = parser.parse_args()
    print(solve_equation(args.equation))

if __name__ == '__main__':
    unittest.main()