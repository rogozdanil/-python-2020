# -*- coding: utf8 -*-
from lab_python_oop.GeometricFigure import GeometricFigure
from lab_python_oop.FigureColor import FigureColor
import math


class Circle(GeometricFigure):
    FIGURE_TYPE = "Круг"

    def __init__(self, color, radius):
        self.radius = radius
        self.figure_color = FigureColor()
        self.figure_color.color_property = color

    def _square(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            Circle.get_figure_type(),
            self.figure_color.color_property,
            self.radius,
            self._square()
        )
