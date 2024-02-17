#!/usr/bin/python3
"""Module that checks with unit testing the rectangle.py"""
import unittest
import os
from models.rectangle import Rectangle
import pep8

class TestRectangle(unittest.TestCase):
    """Class that checks rectangle.py"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def rectangle_1_2(self):
        """Test of Rectangle(1, 2)"""
        rectangle = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_1_2_3_exists(self):
        """Test if Rectangle(1, 2, 3) exists"""
        rectangle = Rectangle(1, 2, 3)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)

    def test_rectangle_with_four_param(self):
        """Rectangle(1, 2, 3, 4)"""
        rectangle = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_rectangle_width_string(self):
        """Rectangle("1", 2)"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rectangle_x_str(self):
        """Test of Rectangle(1, 2, "3")"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rectangle_width_string(self):
        """Rectangle(1, "2")"""
        with self.assertRaises(TypeError):
            Rectangle(1,"2")

    def test_rectangle_y_str(self):
        """Test of Rectangle(1, 2, 3, "4")"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_with_5_params(self):
        """Test of Rectangle(1,2,3,4,5)"""
        rectangle = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rectangle.width,1)
        self.assertEqual(rectangle.height,2)
        self.assertEqual(rectangle.x,3)
        self.assertEqual(rectangle.y,4)
        self.assertEqual(rectangle.id,5)

    def test_rectangle_negative_width(self):
        """Test creating Rectangle with negative width"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_negative_height(self):
        """Test creating Rectangle with negative height"""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rectangle_zero_width(self):
        """Test creating Rectangle with zero width"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_zero_height(self):
        """Test creating Rectangle with zero height"""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_negative_x(self):
        """Test creating Rectangle with negative x-coordinate"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rectangle_negative_y(self):
        """Test creating Rectangle with negative y-coordinate"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
        def test_area(self):
        """Test the area() method"""
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.area(), 12)
