#!/usr/bin/python3
"""a class Rectangle that defines a rectangle -> 0-rectangle.py"""


class Rectangle:
    """said class that defines properties of a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation of rectangle

        Args: width(int) rectanle width
          height (int) rectangle height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property 
    def width(self):
        """retrieves width of rectangle"""
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of our square"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
    
    def __str__(self):
        """Prints the rectangle in #form"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        return "\n".join([str(self.print_symbol) * self.__width for _ in range(self.__height)])
    
    def __repr__(self):
        """Prints said string + locaca"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Deletes an instance of the rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
