

class FiguresColour():
    
    def __init__(self, value):
        self._colour_ = value

    @property
    def colour(self):
        return self._colour_

    @colour.setter
    def colour(self, value):
        self._colour_ = value
