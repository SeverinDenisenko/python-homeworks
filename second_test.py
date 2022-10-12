from second import *


def test_planet():
    pl1 = Planet("Earth", 1)
    pl1.show()
    pl2 = Planet("Mars", 1.52)
    print(Planet.hohmann(pl1, pl2))


def test_robot():
    r1 = Robot(1, 2)
    r1.show()
    r1.move_up(1)
    r1.show()
    r1.save("robot")
    r2 = Robot.load("robot")
    r2.show()


def test_triangles():
    p1 = Point(0, 0)
    p2 = Point(1, 1)
    p3 = Point(0, 1)
    t = Triangle(p1, p2, p3)
    print(t.area)
    print(t.perimeter)
    tc = ColouredTriangle(p1, p2, p3, 1)
    print(tc.is_inside(Point(0.25, 0.99)))
    print(tc.is_inside(Point(0.25, 1.01)))
    print(tc.is_inside(Point(1, 0)))


def test_super_list():
    a = SuperList()

    a.append("123")
    a.append(3)
    a.append(3.14159)

    a.save("list")

    b = SuperList.load("list")
    print(b)


if __name__ == "__main__":
    test_planet()
    test_robot()
    test_triangles()
    test_super_list()
