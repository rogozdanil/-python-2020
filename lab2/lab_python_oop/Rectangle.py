# -*- coding: utf8 -*-
from lab_python_oop.GeometricFigure import GeometricFigure
from lab_python_oop.FigureColor import FigureColor


class Rectangle(GeometricFigure):
    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, color, width, height):
        self._width = width
        self._height = height
        self._figure_color = FigureColor()
        self._figure_color.color_property = color

    def _square(self):
        return self._width * self._height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_figure_type(),
            self._figure_color.color_property,
            self._width,
            self._height,
            self._square()
        )
