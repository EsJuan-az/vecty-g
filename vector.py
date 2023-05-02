from math import radians, sin, cos

class Vector2():
    @staticmethod
    def O():
        return Vector2(0,0)
    @staticmethod
    def E1():
        return Vector2(1,0)
    @staticmethod
    def E2():
        return Vector2(0, 1)
    
    def ortogonal(self):
        return TransformacionLineal2(0, -1, 1, 0).aplicar(self) #Vector2(-v.y, v.x)
    
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
        return self * v2.ortogonal() == 0



class Recta2():
    @staticmethod
    def dosPuntos(p1, p2):
        director = p2 - p1
        return Recta2.vectorialParametrica(director, p1)
    
    @staticmethod
    def ecuacionNormal(normal, punto):
        params = {
            "normal": normal,
            "punto": punto,
            "director": normal.ortogonal()
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
            "director": normal.ortogonal()
        }

    @staticmethod
    def vectorialParametrica(director, punto):
        params = {
            "normal": director.ortogonal(),
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
    
    def P(self, X):
        return TransformacionLineal2.P(self.director).aplicar(X) + TransformacionLineal2.P(self.normal).aplicar(self.punto)


    def S(self, X):
        return (self.P(X) * 2) - X
    

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
    def P(DL, X = None):
        D = None
        if isinstance(DL, Recta2) and Vector2.O() in DL:
            D = DL.director
        elif isinstance(DL, Vector2):
            D = DL
        else:
            raise TypeError
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
    def S(DL):
        D = None
        if isinstance(DL, Recta2) and Vector2.O() in DL:
            D = DL.director
        elif isinstance(DL, Vector2):
            D = DL
        else:
            raise TypeError
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

    def __init__(self, a, b, c, d, r = 1.0):
        self.a = a * r
        self.b = b * r
        self.c = c * r
        self.d = d * r
        self.setName("T")
    
    def setName(self, name):
        self.name = name

    def esInyectiva(self):
        return not ( self.aplicar(Vector2.E1()) == self.aplicar(Vector2.E2()).ortogonal() )
    
    def aplicar(self, v):
        return Vector2(self.a * v.x + self.b * v.y, self.c * v.x + self.d * v.y)
    
    def __eq__(self, v):
        return round(self.a,2) == round(v.a,2) and round(self.b,2) == round(v.b,2) and round(self.c,2) == round(v.c,2) and round(self.d,2) == round(v.d,2)

    def __str__(self):
        a = round(self.a, 2)
        b = round(self.b, 2)
        c = round(self.c, 2)
        d = round(self.d, 2)
        lenName = len(f"{self.name} = ")
        tabs = (lenName + (lenName % 8)) // 8
        tabstring = "\t" * (1 if tabs == 0 else tabs) 
        return f"{self.name} = \t({a}x + {b}y)\n{tabstring}({c}x + {d}y)\n"
