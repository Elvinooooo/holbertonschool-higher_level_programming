#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_automatic_id(self):
        base = Base()
        base = Base()
        self.assertEqual(base.id, 1)
        self.assertEqual(base.id, 2)
        self.assertEqual(base.id, 3)

if __name__ == '__main__':
    unittest.main()
