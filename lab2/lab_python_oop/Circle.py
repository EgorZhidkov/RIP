from lab_python_oop.GeometrickFigure import GeometricFigure
from lab_python_oop.FiguresColour import FiguresColour
import math
class Circle(GeometricFigure):
    # radius = 0
    figure_name = 'Квадрат'

    def __init__(self, rad, c):
        self.radius = rad
        self.colour = FiguresColour(c)._colour_





    def search_square(self):
        return self.radius * (math.pi ** 2)

    def __repr__(self):
        return 'Фигура {}, цвет {}, радиус {}, площадь {}'.format(
            self.figure_name,
            self.colour,
            self.radius,
            self.search_square()
        )