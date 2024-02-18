#!/usr/bin/python3
import unittest
import os
from models.square import Square
import pep8

class TestSquare(unittest.TestCase):
    """Class that checks square.py"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    def test_square_init(self):
        """Test the initialization of Square"""
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_square_init_with_one_arg(self):
        """Test initialization with one argument"""
        square = Square(1)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.width, 1)
        self.assertEqual(square.height, 1)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_square_init_with_two_args(self):
        """Test initialization with two arguments"""
        square = Square(1, 2)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.width, 1)
        self.assertEqual(square.height, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 0)

    def test_square_init_with_three_args(self):
        """Test initialization with three arguments"""
        square = Square(1, 2, 3)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.width, 1)
        self.assertEqual(square.height, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_init_with_non_integer_size(self):
        """Test initialization with non-integer size"""
        with self.assertRaises(TypeError):
            Square("1")

    def test_square_init_with_non_integer_x(self):
        """Test initialization with non-integer x"""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_square_init_with_non_integer_y(self):
        """Test initialization with non-integer y"""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_init_with_negative_size(self):
        """Test initialization with negative size"""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_init_with_negative_x(self):
        """Test initialization with negative x"""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_init_with_negative_y(self):
        """Test initialization with negative y"""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_init_with_zero_size(self):
        """Test initialization with zero size"""
        with self.assertRaises(ValueError):
            Square(0)
