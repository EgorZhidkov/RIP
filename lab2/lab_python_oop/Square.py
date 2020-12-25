from lab_python_oop.GeometrickFigure import GeometricFigure
from lab_python_oop.Rectangle import Rect
from lab_python_oop.FiguresColour import FiguresColour

class Square(Rect):
    length = 0
    figure_name = 'Квадрат'
    def __init__(self, len, c):
        self.length = len * len
        self.colour = FiguresColour(c)._colour_

    def search_square(self):
        return self.length * self.length

    def __repr__(self):
        return 'Фигура {}, цвет {}, сторона квадрата {}, площадь {}'.format(
            self.figure_name,
            self.colour, 
            self.length,
            self.search_square()
        )