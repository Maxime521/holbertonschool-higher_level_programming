from abc import ABC, abstractmethod
import math


class Shape(ABC):

    """
    An abstract class representing a geometric shape.
    Classes inheriting from Shape implement the area and perimeter methods.
    """

    @abstractmethod
    def area(self):
        """Abstract method to calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """A class representing a circle. Inherits from abstract class Shape."""
    def __init__(self, radius):
        """
        Constructor for the Circle class.

        :param radius: The radius of the circle (float or int).
        """
        self.radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculates and returns perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """class representing rectangle. Inherits from the abstract class Shape."""
    def __init__(self, width, height):
        """
        Constructor for the Rectangle class.

        :param width: The width of the rectangle (float or int).
        :param height: The height of the rectangle (float or int).
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a geometric shape.
    Uses duck typing: the object passed have the area and perimeter methods.

    :param shape: An object of type Shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


circle = Circle(radius=5)
shape_info(circle)

rectangle = Rectangle(width=4, height=6)
shape_info(rectangle)
