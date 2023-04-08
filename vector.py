class Vector():
    @staticmethod
    def elOrtogonal(v):
        return Vector(-v.y, v.x)
    @staticmethod
    def sonOrtogonales(v1, v2):
        return v1 * v2 == 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, v2):
        return Vector(self.x + v2.x, self.y + v2.y)
    def __sub__(self, v2):
        return Vector(self.x - v2.x, self.y - v2.y)
    def __mul__(self, v2):
        if isinstance(v2, Vector):
            return self.x * v2.x + self.y * v2.y
        elif isinstance(v2, (int, float)):
            return Vector(self.x * v2, self.y * v2)
        else:
            raise TypeError
    def __str__(self):
        return f"""({self.x},{self.y})"""
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** .5
    def __eq__(self, v2):
        return self * Vector.elOrtogonal(v2) == 0


