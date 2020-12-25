# from GeometrickFigure import GeometricFigure
# from FiguresColour import FiguresColour
from lab_python_oop.GeometrickFigure import GeometricFigure 
from lab_python_oop.FiguresColour import FiguresColour


class Rect(GeometricFigure):
    length = 0
    width = 0
    _square = 0
    figure_name = 'Прямоугольник'
    def __init__(self, len, wid, col):
        self.length = len
        self.width = wid
        self.colours = FiguresColour(col)._colour_
    
    def search_square(self):
        self._square = self.length * self.width
        return self._square

    def __repr__(self):
        return 'Фигура {}, цвет {}, первая стороная {},вторая стороная {}, площадь {}'.format(
            self.figure_name,
            self.colours,
            self.width,
            self.length,
            self.search_square()
        )
    