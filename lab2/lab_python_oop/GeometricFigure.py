from abc import ABC, abstractmethod


class GeometricFigure(ABC):
    FIGURE_TYPE = None

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    @abstractmethod
    def _square(self):
        pass
