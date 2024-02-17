#!/usr/bin/python3
"""Module checking unittest of Base.py"""
import unittest
import os
import pep8
from models.base import Base

class TestBase(unittest.TestCase):
    """Class for checking base.py"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_automatic_id(self):
        """Check the automatic id assignment"""
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)

    def test_save_id_89(self):
        """ Create a Base instance with ID 89"""
        base_89 = Base(89)
        self.assertEqual(base_89.id, 89)

if __name__ == '__main__':
    unittest.main()
