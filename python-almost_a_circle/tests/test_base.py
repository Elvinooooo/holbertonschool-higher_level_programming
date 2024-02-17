#!/usr/bin/python3
import unittest
import os
from models.base import Base

class TestBase(unittest.TestCase):
    def test_automatic_id(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)

if __name__ == '__main__':
    unittest.main()
