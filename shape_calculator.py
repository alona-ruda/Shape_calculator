from math import pi, sqrt


def distance_between_points(x1, y1, x2, y2):
    """
     Calculate the distance between two points (x1, y1) and (x2, y2).

     Parameters:
     x1 (float): The x-coordinate of the first point.
     y1 (float): The y-coordinate of the first point.
     x2 (float): The x-coordinate of the second point.
     y2 (float): The y-coordinate of the second point.

     Returns:
     float: The distance between the two points.
     """
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def parse_input(data):
    """
    Parse input data string and return a dictionary of parsed values.

    Parameters:
    data (str): Input data string containing shape and its parameters.

    Returns:
    dict: Parsed values in a dictionary format.

    Raises:
    ValueError: If input data is invalid or cannot be parsed correctly.
    """
    divided_data = data.split()
    if len(divided_data) < 2:
        raise ValueError("Invalid input data")

    result_dict = {"Shape": divided_data[0]}
    i = 1
    while i < len(divided_data):
        key = divided_data[i]
        if not isinstance(key, str):
            raise ValueError(f"Invalid key type: {key}. Key must be a string.")
        values = []
        i += 1
        while i < len(divided_data):
            try:
                value = float(divided_data[i])
                values.append(value)
                i += 1
            except ValueError:
                break
        if not values:
            raise ValueError(f"Invalid data format for key: {key}")
        result_dict[key] = values[0] if len(values) == 1 else values
    return result_dict


class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def __str__(self):
        return "Circle"

    def get_perimeter(self):
        return 2 * pi * self.radius

    def get_area(self):
        return pi * (self.radius ** 2)


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.side_1 = abs(x2 - x1)
        self.side_2 = abs(y2 - y1)

    def __str__(self):
        return "Rectangle"

    def get_perimeter(self):
        return 2 * (self.side_1 + self.side_2)

    def get_area(self):
        return self.side_1 * self.side_2


class Square:
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side must be positive")
        self.side = side

    def __str__(self):
        return "Square"

    def get_perimeter(self):
        return self.side * 4

    def get_area(self):
        return self.side ** 2


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.side_a = distance_between_points(x1, y1, x2, y2)
        self.side_b = distance_between_points(x2, y2, x3, y3)
        self.side_c = distance_between_points(x3, y3, x1, y1)

        if not self.is_valid_triangle():
            raise ValueError("The given points do not form a valid triangle.")

    def __str__(self):
        return "Triangle"

    def is_valid_triangle(self):
        a, b, c = self.side_a, self.side_b, self.side_c
        return a + b > c and b + c > a and c + a > b

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def get_area(self):
        s = self.get_perimeter() / 2
        return sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))


def calc(data):
    """
    Calculate the perimeter and area of a shape based on the input data.

    Parameters:
    data (str): Input data string containing the shape and its parameters.

    Returns:
    str: The perimeter and area of the shape.

    Raises:
    ValueError: If the shape is unknown or if input data is invalid.
    """
    parsed_data = parse_input(data)
    shape = None
    match parsed_data['Shape']:
        case 'Circle':
            shape = Circle(parsed_data['Radius'])
        case 'Triangle':
            x1, y1 = parsed_data['Point1']
            x2, y2 = parsed_data['Point2']
            x3, y3 = parsed_data['Point3']
            shape = Triangle(x1, y1, x2, y2, x3, y3)
        case 'Rectangle':
            if 'TopRight' in parsed_data and 'BottomLeft' in parsed_data:
                x1, y1 = parsed_data['TopRight']
                x2, y2 = parsed_data['BottomLeft']
            elif 'TopLeft' in parsed_data and 'BottomRight' in parsed_data:
                x1, y1 = parsed_data['TopLeft']
                x2, y2 = parsed_data['BottomRight']
            else:
                raise ValueError("Invalid coordinates for Rectangle")
            shape = Rectangle(x1, y1, x2, y2)
        case 'Square':
            shape = Square(parsed_data['Side'])
        case _:
            raise ValueError(f"Unknown shape: {parsed_data['Shape']}. Please try again")

    return (f'Perimeter of {shape} = {round(shape.get_perimeter(), 2)}. '
            f'Area = {round(shape.get_area(), 2)}')


def input_from_user():
    """
    Prompt the user for shape data and print the calculated perimeter and area.
    """
    data = input("Please provide shape's data to calculate: ")
    print(calc(data))