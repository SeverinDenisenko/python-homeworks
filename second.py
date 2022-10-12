from pickle import dump, load
from typing import List


# 2.3
class Planet:
    def __init__(self, name, axis):
        """
        Class constructor
        :param name: Name of a planet
        :param axis: Semi-major axis in AU
        """
        self.name = name
        self.axis = axis
        self.__calculate_period__()

    def __calculate_period__(self):
        self.period = (self.axis ** 3) ** 0.5

    def show(self):
        """
        Shows info about planet on screen
        """
        print("Planet: " + self.name)
        print("Semi-major axis: " + str(self.axis) + " AU")
        print("Period: " + str(self.period) + " Years")

    @staticmethod
    def hohmann(planet1, planet2):
        """
        :param planet1: instance of a class Planet
        :param planet2: instance of a class Planet
        :return: Time required to get from planet 1 to planet 2 on Hohmann trajectory
        """
        a = (planet1.axis + planet2.axis) / 2
        return (a ** 3) ** 0.5 / 2


# 2.7
class Robot:
    def __init__(self, x, y):
        self.x_0 = x
        self.y_0 = y

        self.x = x
        self.y = y

    def move_up(self, shift):
        """
        Moves robot in positive direction along the y-axis by shift
        """
        self.y += shift

    def move_down(self, shift):
        """
        Moves robot in negative direction along the y-axis by shift
        """
        self.y -= shift

    def move_left(self, shift):
        """
        Moves robot in negative direction along the x-axis by shift
        """
        self.x -= shift

    def move_right(self, shift):
        """
        Moves robot in positive direction along the x-axis by shift
        """
        self.x += shift

    def show(self):
        """
        Shows information about robot movement
        """
        print("Start position: " + str(self.x_0) + ", " + str(self.y_0))
        print("Current position: " + str(self.x) + ", " + str(self.y))
        print("Full distance: " + str(((self.x - self.x_0) ** 2 + (self.y - self.y_0) ** 2) ** 0.5))

    def save(self, filename):
        """
        Writes information about Robot in file
        :param filename: path to file
        """
        with open(filename, "wb") as file:
            # "wb" argument opens the file in binary mode
            dump(self, file)

    # May be better to convert to @staticmethod def load(filename)
    @classmethod
    def load(cls, filename):
        """
        Reads information about Robot from file
        :param filename: path to file
        :return: instance of class Robot
        """
        with open(filename, "rb") as file:
            # "wb" argument opens the file in binary mode
            return load(file)


# 2.9
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def distance(a, b):
        """
        :return: Distance between tho points
        """
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.__calculate_area__()
        self.__calculate_perimeter__()

    def __calculate_area__(self):
        self.area = abs(self.a.x * (self.b.y - self.c.y) +
                        self.b.x * (self.c.y - self.a.y) +
                        self.c.x * (self.a.y - self.b.y)) / 2

    def __calculate_perimeter__(self):
        self.perimeter = (Point.distance(self.a, self.b) +
                          Point.distance(self.b, self.c) +
                          Point.distance(self.c, self.a))

    def is_inside(self, p):
        return self.area == (Triangle(self.a, self.b, p).area +
                             Triangle(self.a, p, self.c).area +
                             Triangle(p, self.b, self.c).area)


class ColouredTriangle(Triangle):
    def __init__(self, a, b, c, colour):
        super().__init__(a, b, c)
        self.colour = colour


# 2.11
class SuperList(List):
    @staticmethod
    def load(filename):
        with open(filename, "rb") as file:
            # "rb" argument opens the file in binary mode
            return load(file)

    def save(self, filename):
        with open(filename, "wb") as file:
            # "wb" argument opens the file in binary mode
            dump(self, file)
