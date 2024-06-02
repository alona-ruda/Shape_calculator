import unittest
from task_DiversiPy import (parse_input, Rectangle, Square, Triangle,
                            Circle, calc)


class TestParseData(unittest.TestCase):
    def test_parse_triangle(self):
        p = parse_input("Triangle Point1 5 5 Point2 8 8 Point3 10 2")
        self.assertEqual(p['Shape'], "Triangle")
        self.assertEqual(p['Point1'], [5.0, 5.0])
        self.assertEqual(p['Point2'], [8.0, 8.0])
        self.assertEqual(p['Point3'], [10.0, 2.0])

    def test_parse_rectangle(self):
        r = parse_input("Rectangle TopRight 2 2 BottomLeft 1 1")
        self.assertEqual(r['Shape'], 'Rectangle')
        self.assertEqual(r['TopRight'], [2.0, 2.0])
        self.assertEqual(r['BottomLeft'], [1.0, 1.0])

    def test_len_input(self):
        with self.assertRaises(ValueError):
            parse_input('Square')

    def test_invalid_key(self):
        with self.assertRaises(ValueError):
            parse_input('Square 1 Side')

    def test_not_values(self):
        with self.assertRaises(ValueError):
            parse_input('Square Side')


class TestCircle(unittest.TestCase):
    def test_circle(self):
        circle = Circle(5)
        self.assertEqual(round(circle.get_area(), 3), 78.54)
        self.assertEqual(round(circle.get_perimeter(), 3), 31.416)

    def test_circle_float(self):
        circle = Circle(23.3)
        self.assertEqual(round(circle.get_area(), 3), 1705.539)
        self.assertEqual(round(circle.get_perimeter(), 3), 146.398)

    def test_circle_negative(self):
        with self.assertRaises(ValueError):
            Circle(-23)

    def test_circle_zero_radius(self):
        with self.assertRaises(ValueError):
            Circle(0)


class TestRectangle(unittest.TestCase):
    def test_rectangle_positive(self):
        rectangle = Rectangle(1, 2, 5, 8)
        self.assertEqual(rectangle.side_1, 4)
        self.assertEqual(rectangle.side_2, 6)
        self.assertEqual(rectangle.get_perimeter(), 20)
        self.assertEqual(rectangle.get_area(), 24)

    def test_rectangle_negative(self):
        rectangle = Rectangle(-8, 2, -2, -5)
        self.assertEqual(rectangle.side_1, 6)
        self.assertEqual(rectangle.side_2, 7)
        self.assertEqual(rectangle.get_perimeter(), 26)
        self.assertEqual(rectangle.get_area(), 42)


class TestSquare(unittest.TestCase):
    def test_square(self):
        square = Square(5)
        self.assertEqual(square.get_area(), 25)
        self.assertEqual(square.get_perimeter(), 20)

    def test_square_negative(self):
        with self.assertRaises(ValueError):
            Square(-2)


class TestTriangle(unittest.TestCase):
    def test_triangle_positive(self):
        triangle = Triangle(0, 0, 3, 0, 0, 4)
        self.assertEqual(triangle.side_a, 3.0)
        self.assertEqual(triangle.side_b, 5.0)
        self.assertEqual(triangle.side_c, 4.0)
        self.assertEqual(triangle.get_perimeter(), 12)
        self.assertEqual(triangle.get_area(), 6)

    def test_triangle_mixed(self):
        triangle = Triangle(-2, 3, -8, -10, 2, -5)
        self.assertEqual(round(triangle.side_a, 3), 14.318)
        self.assertEqual(round(triangle.side_b, 3), 11.18)
        self.assertEqual(round(triangle.side_c, 3), 8.944)
        self.assertEqual(round(triangle.get_perimeter(), 3), 34.442)
        self.assertEqual(round(triangle.get_area(), 3), 50)

    def test_triangle_float(self):
        triangle = Triangle(3.8, -2, -1, 1, 0, -3.6)
        self.assertEqual(round(triangle.side_a, 3), 5.66)
        self.assertEqual(round(triangle.side_b, 3), 4.707)
        self.assertEqual(round(triangle.side_c, 3), 4.123)
        self.assertEqual(round(triangle.get_perimeter(), 3), 14.491)
        self.assertEqual(round(triangle.get_area(), 3), 9.54)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(0, 0, 1, 1, 2, 2)


class TestCalc(unittest.TestCase):
    def test_wrong_shape(self):
        with self.assertRaises(ValueError):
            calc("Cirecle Center 1 1 Radius 2")

    def test_circle(self):
        result = calc("Circle Radius 2")
        self.assertEqual(result, "Perimeter of Circle = 12.57. Area = 12.57")

    def test_circle_negative(self):
        with self.assertRaises(ValueError):
            calc("Circle Radius -5")

    def test_triangle(self):
        result = calc("Triangle Point1 0 0 Point2 3 0 Point3 0 4")
        self.assertEqual(result, "Perimeter of Triangle = 12.0. Area = 6.0")

    def test_rectangle(self):
        result = calc("Rectangle TopRight 5 8 BottomLeft 1 2")
        self.assertEqual(result, "Perimeter of Rectangle = 20.0. Area = 24.0")

    def test_square(self):
        result = calc("Square Side 4")
        self.assertEqual(result, "Perimeter of Square = 16.0. Area = 16.0")

    def test_invalid_data_format(self):
        with self.assertRaises(ValueError):
            calc("Circle Radius two")

    def test_missing_values(self):
        with self.assertRaises(ValueError):
            calc("Rectangle TopRight 5 8 BottomLeft")
