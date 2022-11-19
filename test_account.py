import unittest
from account import *

class account_test(unittest.TestCase):
    def test_deposit(self):
        self.assertEqual(deposit(10.00, True))
        self.assertEqual(deposit(-2.00, False))
        self.assertEqual(deposit(0, False))

    def test_withdraw(self):
        self.assertEqual(withdraw(10.00, True))
        self.assertEqual(withdraw(-2.00, False))
        


