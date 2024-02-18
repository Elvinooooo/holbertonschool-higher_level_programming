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

    def test_square_str_method(self):
        """Test of __str__() for Square"""
        square = Square(5, 2, 3, 89)
        expected_output = "[Square] (89) 2/3 - 5"
        self.assertEqual(str(square), expected_output)

    def test_square_to_dictionary(self):
        """Test of to_dictionary() in Square"""
        square = Square(5, 2, 3, 89)
        expected_dict = {'id': 89, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_square_update_methods(self):
        """Test of update() methods in Square"""
        square = Square(5, 2, 3, 89)
        
        square.update(90)
        self.assertEqual(square.id, 90)

        square.update(90, 1)
        self.assertEqual(square.size, 1)

        square.update(90, 1, 2)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

        square.update(90, 1, 2, 3)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

        square.update(id=91)
        self.assertEqual(square.id, 91)

        square.update(id=91, size=2)
        self.assertEqual(square.size, 2)

        square.update(id=91, size=2, x=3)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 3)

    def test_square_create_method(self):
        """Test of Square.create() method in Square"""
        square_dict = {'id': 89, 'size': 5, 'x': 2, 'y': 3}
        square = Square.create(**square_dict)
        self.assertEqual(square.to_dictionary(), square_dict)

    def test_square_save_to_file_none(self):
        """Test of Square.save_to_file(None) in Square."""
        Square.save_to_file(None)
        filename = "Square.json"
        self.assertTrue(os.path.exists(filename))
        with open(filename, "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")
        os.remove(filename)

    def test_square_save_to_file_empty_list(self):
        """Test of Square.save_to_file([]) in Square."""
        Square.save_to_file([])
        filename = "Square.json"
        self.assertTrue(os.path.exists(filename))
        with open(filename, "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")
        os.remove(filename)

    def test_square_save_to_file_with_square(self):
        """Test of Square.save_to_file([Square(1)]) in Square."""
        square = Square(1)
        Square.save_to_file([square])
        filename = "Square.json"
        self.assertTrue(os.path.exists(filename))
        with open(filename, "r") as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1, "size": 1, "x": 0, "y": 0}]')
        os.remove(filename)
