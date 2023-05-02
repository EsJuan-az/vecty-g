from math import radians, sin, cos
class Vector2():
    @staticmethod
    def elOrtogonal(v):
        return Vector2(-v.y, v.x)
    
    @staticmethod
    def sonOrtogonales(v1, v2):
        return v1 * v2 == 0
    
    @staticmethod
    def colineales(*vs):
        if len(vs) <= 2:
            return True
        recta = Recta2.dosPuntos(vs[0], vs[1])
        for v in vs:
            if v not in recta:
                return False
        return True    
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Vector2(self.x + v.x, self.y + v.y)
    
    def __sub__(self, v):
        return Vector2(self.x - v.x, self.y - v.y)
    
    def __mul__(self, v):
        if isinstance(v, Vector2):
            return self.x * v.x + self.y * v.y
        elif isinstance(v, (int, float)):
            return TransformacionLineal2.H(v).aplicar(self)
        else:
            raise TypeError

    def __str__(self):
        return f"""({self.x},{self.y})"""
    
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** .5
    
    def __eq__(self, v2):
        return self * Vector2.elOrtogonal(v2) == 0



class Recta2():
    @staticmethod
    def P(L, X):
        return TransformacionLineal2.P(L.director).aplicar(X) + TransformacionLineal2.P(L.normal).aplicar(L.punto)

    @staticmethod
    def dosPuntos(p1, p2):
        director = p2 - p1
        return Recta2.vectorialParametrica(director, p1)
    
    @staticmethod
    def ecuacionNormal(normal, punto):
        params = {
            "normal": normal,
            "punto": punto,
            "director": Vector2.elOrtogonal(normal)
        }
        recta = Recta2(params)
        return recta
    
    @staticmethod
    def ecucacionGeneral(a, b, c, x = None, y = None):
        normal = Vector2(a, b)
        if x:
            punto = Vector2(x, (-a*x - c) / b)
        elif y:
            punto = Vector2(x, (-b*y - c) / a)
        else:
            punto = Vector2(0,0)
        params = {
            "normal": normal,
            "punto": punto,
            "director": Vector2.elOrtogonal(normal)
        }

    @staticmethod
    def vectorialParametrica(director, punto):
        params = {
            "normal": Vector2.elOrtogonal(director),
            "director": director,
            "punto": punto
        }
        return Recta2(params)
    
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
        
class TransformacionLineal2():
    @staticmethod
    def O():
        O = TransformacionLineal2(0, 0, 0, 0)
        O.setName("O")
        return O
    
    @staticmethod
    def I():
        I = TransformacionLineal2(1, 0, 0, 1)
        I.setName("I")
        return I
    
    @staticmethod
    def H(r):
        Hr = TransformacionLineal2(r, 0, 0, r)
        Hr.setName(f"H[{r}]")
        return Hr
    
    @staticmethod
    def P(D):
        d1 = D.x
        d2 = D.y
        divisor = (d1 ** 2 + d2 ** 2)
        a = (d1 ** 2) / divisor
        bc = (d1 * d2) / divisor
        d = (d1 ** 2) / divisor
        pD = TransformacionLineal2(a, bc, bc, d)
        pD.setName(f"P{D}")
        return pD
    
    @staticmethod
    def S(D):
        d1 = D.x
        d2 = D.y
        divisor = (d1 ** 2 + d2 ** 2)
        a = (d1 ** 2 - d2 ** 2) / divisor
        bc = (2 * d1 * d2) /divisor
        sD = TransformacionLineal2(a, bc, bc, -a)
        sD.setName(f"S{D}")
        return sD
    
    @staticmethod
    def R_RAD(t):
        c = cos(t)
        s = sin(t)
        R = TransformacionLineal2(c, -s, s, c)
        R.setName(f"R[{t}rad]")
        return R
    
    @staticmethod
    def R_DEG(t):
        c = cos(radians(t))
        s = sin(radians(t))
        R = TransformacionLineal2(c, -s, s, c)
        R.setName(f"R[{t}°]")
        return R

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.setName("T")
    
    def setName(self, name):
        self.name = name

    def aplicar(self, v):
        return Vector2(self.a * v.x + self.b * v.y, self.c * v.x + self.d * v.y)
    
    def __str__(self):
        a = round(self.a, 2)
        b = round(self.b, 2)
        c = round(self.c, 2)
        d = round(self.d, 2)
        return f"{self.name} = \t({a}x + {b}y)\n\t\t({c}x + {d}y)"
