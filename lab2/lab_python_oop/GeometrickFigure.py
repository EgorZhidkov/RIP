from abc import ABC, abstractmethod, abstractproperty

class GeometricFigure(ABC):
    square = 0


    @abstractmethod
    def search_square(self):
        pass