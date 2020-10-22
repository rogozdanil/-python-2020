# -*- coding: utf8 -*-
from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square
import arrow


def main():
    print("Рогозин Данила ИУ5-51Б")
    print(arrow.now(), "\n")

    rectangle = Rectangle("синего", 17, 17)
    circle = Circle("зеленого", 17)
    square = Square("красного", 17)

    print(rectangle)
    print(circle)
    print(square)


if __name__ == "__main__":
    main()
