#!/usr/bin/python3
"""Module that checks with unit testing the rectangle.py"""
import unittest
import os
import sys
from models.rectangle import Rectangle
import pep8
from io import StringIO

class TestRectangle(unittest.TestCase):
    """Class that checks rectangle.py"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_rectangle_1_2(self):
        """Test of Rectangle(1, 2)"""
        rectangle = Rectangle(1, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

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

    def test_rectange_width_string(self):
        """Test the constructor of Rectangle class with string width."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rectangle_height_string(self):
        """Rectangle(1, "2")"""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rectangle_x_str(self):
        """Test of Rectangle(1, 2, "3")"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

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


    def test_str_method(self):
        """Test of __str__() for Rectangle"""
        rectangle = Rectangle(1, 2, 3, 4, 89)
        expected_output = "[Rectangle] (89) 3/4 - 1/2"
        self.assertEqual(str(rectangle), expected_output)

    def test_display_without_xy(self):
        """Test of display() without x and y"""
        rectangle = Rectangle(2, 2)
        expected_output = None
        self.assertEqual(rectangle.display(), expected_output)

    def test_display(self):
        """Test of display()"""
        rectangle = Rectangle(2, 2, 1, 1)
        expected_output = None 
        self.assertEqual(rectangle.display(), expected_output)

    def test_to_dictionary(self):
        """Test of to_dictionary() in Rectangle"""
        rectangle = Rectangle(1, 2, 3, 4, 89)
        expected_dict = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)

    def test_update_methods(self):
        """Test of update() methods in Rectangle"""
        rectangle = Rectangle(1, 2, 3, 4, 89)
        rectangle.update(90)
        self.assertEqual(rectangle.id, 90)

        rectangle.update(90, 2)
        self.assertEqual(rectangle.width, 2)

        rectangle.update(90, 2, 3)
        self.assertEqual(rectangle.height, 3)

        rectangle.update(90, 2, 3, 4)
        self.assertEqual(rectangle.x, 4)

        rectangle.update(90, 2, 3, 4, 5)
        self.assertEqual(rectangle.y, 5)

        rectangle.update(id=91)
        self.assertEqual(rectangle.id, 91)

        rectangle.update(id=91, width=2)
        self.assertEqual(rectangle.width, 2)

    def test_create_method(self):
        """Test of Rectangle.create() method in Rectangle"""
        rectangle_dict = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        rectangle = Rectangle.create(**rectangle_dict)
        self.assertEqual(rectangle.to_dictionary(), rectangle_dict)

    def test_display_without_x_and_y(self):
        """Test display() without x and y."""
        captured_output = StringIO()          
        sys.stdout = captured_output          

        r = Rectangle(4, 2)
        r.display()

        sys.stdout = sys.__stdout__  

        self.assertEqual(captured_output.getvalue(), "####\n####\n")

    def test_display_without_y(self):
        """Test display() without y."""
        captured_output = StringIO()          
        sys.stdout = captured_output          

        r = Rectangle(4, 2, 2)
        r.display()

        sys.stdout = sys.__stdout__  

        self.assertEqual(captured_output.getvalue(), "  ####\n  ####\n")

    def test_display(self):
        """Test display()."""
        captured_output = StringIO()          
        sys.stdout = captured_output          

        r = Rectangle(4, 2, 2, 2)
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "\n\n  ####\n  ####\n")

    def test_load_from_file_nonexistent(self):
        """Test of Rectangle.load_from_file() when file doesn’t exist."""
        # Arrange
        filename = "Rectangle.json"
        if os.path.exists(filename):
            os.remove(filename)  # Ensure the file doesn't exist

        # Act
        instances = Rectangle.load_from_file()

        # Assert
        self.assertEqual(instances, [])

    def test_load_from_file_exists(self):
        """Test of Rectangle.load_from_file() when file exists."""
        # Arrange
        filename = "Rectangle.json"
        instances_data = [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                          {"id": 2, "width": 3, "height": 4, "x": 5, "y": 6}]
        # Write data to the file
        with open(filename, 'w') as file:
            file.write(Rectangle.to_json_string(instances_data))

        # Act
        instances = Rectangle.load_from_file()

        # Assert
        self.assertEqual(len(instances), len(instances_data))
        for instance, data in zip(instances, instances_data):
            self.assertIsInstance(instance, Rectangle)
            self.assertEqual(instance.id, data['id'])
            self.assertEqual(instance.width, data['width'])
            self.assertEqual(instance.height, data['height'])
            self.assertEqual(instance.x, data['x'])
            self.assertEqual(instance.y, data['y'])

        # Clean up - remove the file
        os.remove(filename)
