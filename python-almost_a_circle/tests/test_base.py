#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_automatic_id(self):
        base = Base()

        self.assertEqual(base.id, 1)

if __name__ == '__main__':
    unittest.main()
