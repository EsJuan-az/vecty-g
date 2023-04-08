
class Vector():
    @staticmethod
    def elOrtogonal(v):
        return Vector(-v.y, v.x)
    @staticmethod
    def sonOrtogonales(v1, v2):
        return v1 * v2 == 0
    @staticmethod
    def colineales(*vs):
        if len(vs) <= 2:
            return True
        recta = Recta.dosPuntos(vs[0], vs[1])
        for v in vs:
            if v not in recta:
                return False
        return True    
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



class Recta():
    @staticmethod
    def dosPuntos(p1, p2):
        director = p2 - p1
        return Recta.vectorialParametrica(director, p1)
    @staticmethod
    def ecuacionNormal(normal, punto):
        params = {
            "normal": normal,
            "punto": punto,
            "director": Vector.elOrtogonal(normal)
        }
        recta = Recta(params)
        return recta
    @staticmethod
    def ecucacionGeneral(a, b, c, x = None, y = None):
        normal = Vector(a, b)
        if x:
            punto = Vector(x, (-a*x - c) / b)
        elif y:
            punto = Vector(x, (-b*y - c) / a)
        else:
            punto = Vector(0,0)
        params = {
            "normal": normal,
            "punto": punto,
            "director": Vector.elOrtogonal(normal)
        }
    @staticmethod
    def vectorialParametrica(director, punto):
        params = {
            "normal": Vector.elOrtogonal(director),
            "director": director,
            "punto": punto
        }
        return Recta(params)
    def __init__(self, params):
        self.normal = params["normal"]
        self.punto = params["punto"]
        self.director = params["director"]
        self.a = self.normal.x
        self.b = self. normal.y
        self.c = -self.a * self.punto.x - self.b * self.punto.y
        self.pendiente = self.director.y / self.director.x

    def __str__(self):
        return f"NORMALES: r{self.normal}\nDIRECTORES: r{self.director}\nPUNTO: {self.punto}\nEC. GENERAL: {self.ecuacionGeneral()}"
    def ecuacionGeneral(self):
        return f"{self.a}x + {self.b}y + {self.c} = 0"
    def __contains__(self, v):
        return self.a * v.x + self.b * v.y + self.c == 0
        