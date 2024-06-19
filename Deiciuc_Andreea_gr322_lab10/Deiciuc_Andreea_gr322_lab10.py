"""
Python program:  determina un punct de pe o suprafata Bezier
cubica extrudata, folosind algoritmul lui de Casteljau iterat sau cel direct.
"""


class Punct:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def __add__(self, other):
        return Punct(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Punct(self.x - other.y, self.y - other.y, self.z - other.z)

    def multiply(self, const):
        return Punct(self.x * const, self.y * const, self.z * const)

    def __str__(self):
        return f"({self.x} , {self.y}, {self.z})"


def alg_de_Casteljau_iterat(puncteExt, n, m, u0, v0):
    rez = {}
    #initializam
    for j in range(m+1):
        for i in range(n+1):
            rez[(i, j, 0, 0)] = puncteExt[(i, j)]

    #pentru u
    for j in range(m + 1):
        for r in range(1, n + 1):
            for i in range(n - r + 1):
                rez[(i, j, r, 0)] = rez[(i, j, r - 1, 0)].multiply(1 - u0) + rez[(i + 1, j, r - 1, 0)].multiply(u0)

    #pentru v
    for s in range(1, m + 1):
        for j in range(m - s + 1):
            rez[(0, j, n, s)] = rez[(0, j, n, s - 1)].multiply(1 - v0) + rez[(0, j + 1, n, s - 1)].multiply(v0)

    return rez


def puncteExtrudate(puncteInitiale, v, delta):
    n = len(puncteInitiale) - 1
    b = {}
    for i in range(n + 1):
        b[(i, 0)] = puncteInitiale[i]
    for i in range(n + 1):
        b[(i, 1)] = puncteInitiale[i] + v.multiply(delta)

    return b

def main():
    grad_curba = 3

    # citire puncte din fisier
    lista_puncte = []
    with open("Lab10.txt", 'r') as f:
        for i in range(0, grad_curba + 1):
            line = f.readline()
            x = float(line.split(',')[0])
            y = float(line.split(',')[1])
            z = float(line.split(',')[2])
            lista_puncte.append(Punct(x, y, z))

    # citire delta din fisier
        delta = float(f.readline())

        if delta < 0:
            raise Exception("date incorecte: gamma trebuie sa fie mai mare ca 0 (gama>0) ")

    # citire versor din fisier
        versor_parts = f.readline()
        versor = Punct(float(versor_parts.split(',')[0]), float(versor_parts.split(',')[1]),float(versor_parts.split(',')[2]))

    # citire u0 si v0 din fisier

        u0 = float(f.readline())

        if u0 < 0 or u0 > 1:
            raise Exception("DATE INCORECTE: reincercati 0 < u0 < 1")

        v0 = float(f.readline())

        if v0 < 0 or v0 > 1:
            raise Exception("DATE INCORECTE: reincercati 0 < v0 < 1")

        f.close()

        n = len(lista_puncte) - 1
        m = 1

        puncte_extrudate = puncteExtrudate(lista_puncte, versor, delta)
        r = alg_de_Casteljau_iterat(puncte_extrudate, n, m, u0, v0)

        print(f'r({u0}, {v0}) = {r[(0, 0, n, m)]}')





main()
