from vector import Vector
class Recta():
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
        normal = Vector.elOrtogonal(director)
        params = {
            "normal": normal,
            "director": director,
            "punto": punto
        }
    def __init__(self, params):
        self.normal = params["normal"]
        self.punto = params["punto"]
        self.director = params["director"]
        self.a = self.normal.x
        self.b = self. normal.y
        self.c = -self.a * self.punto.x - self.b * self.punto.y

    def __str__(self):
        return f"NORMALES: r{self.normal}\nDIRECTORES: r{self.director}\nPUNTO: {self.punto}\nEC. GENERAL: {self.ecuacionGeneral()}"
    def ecuacionGeneral(self):
        return f"{self.a}x + {self.b}y + {self.c} = 0"
    def __contains__(self, v):
        return self.a * v.x + self.b * v.y + self.c == 0
        