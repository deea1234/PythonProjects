"""
    Determinarea unei unui punct de pe o curba Bezier cubica rationala,
    in plan,folosind algoritmul lui de Castelijau rational.
"""

class Punct:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __add__(self, other):
        return Punct(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Punct(self.x - other.y , self.y - other.y)

    def multiply(self, const):
        return Punct(self.x * const ,self.y * const)

    def __str__(self):
        return f"({self.x} , {self.y})"


def add_point():
    lista_puncte = []
    print("Intoroduceti 4 puncte :")
    for i in range(0, 4):
        print(f'punct{i}')
        x = float(input("x: "))
        y = float(input("y: "))
        lista_puncte.append(Punct(x, y))

    return lista_puncte

def add_point_fisier():
    lista_puncte = []
    with open("puncte.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            x = float(line.split(',')[0])
            y = float(line.split(',')[1])
            lista_puncte.append(Punct(x, y))
    return lista_puncte


def add_ponderi_file():
    lista_ponderi = []
    with open("ponderi.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            lista_ponderi.append(float(line))
    return lista_ponderi

def add_ponderi():
    lista_ponderi = []
    print("introduceti 4 ponderi: ")
    for i in range(0, 4):
        p = float(input(f"pondere{i}: "))
        lista_ponderi.append(p)

    return lista_ponderi

def alg_de_Castelijau_rational(puncte, ponderi, t):
    grad = len(ponderi) - 1

    temp_ponderi = ponderi.copy()# copie ponderi


    for k in range(grad):
        for i in range(grad - k):
            temp_ponderi[i] = (1 - t) * temp_ponderi[i] + t * temp_ponderi[i + 1]
        for j in range(grad - k):
            x = (((1 - t) * ponderi[j] * puncte[j].x) + (t * puncte[j + 1].x * ponderi[j + 1]))/temp_ponderi[j]
            y = (((1 - t) * ponderi[j] * puncte[j].y) + (t * puncte[j + 1].y * ponderi[j + 1]))/temp_ponderi[j]

            puncte[j] = Punct(x, y)

        #mutam lista de ponderi temporara in lista de ponderi pentru urmatoarea iteratie
        ponderi.clear()
        ponderi = temp_ponderi.copy()
    return puncte[0]

def meniu():
    print("Alegeti optiunea de introducere a datelor: ")
    optiune = int(input("1.Date din fisier.\n"
                        "2.Date introduse de la tastatura.\n"))

    if optiune == 1:
        lista_puncte = add_point_fisier()
        lista_ponderi = add_ponderi_file()

        t = float(input("introduceti t: "))
        if t < 0 or t > 1:
            raise Exception("t INVALID!")

        print(f'r({t}) ={alg_de_Castelijau_rational(lista_puncte, lista_ponderi, t)}')

    elif optiune == 2:
        lista_puncte = add_point()
        lista_ponderi = add_ponderi()
        t = float(input("introduceti t: "))
        if t < 0 or t > 1:
            raise Exception("t INVALID!")
        print(f'r({t}) ={alg_de_Castelijau_rational(lista_puncte, lista_ponderi, t)}')

    else:
        print("Varianta incorecta! Reinceracti!")

def main():

    meniu()

    #exemplu gata introdus
    # lista_puncte = [Punct(0, 0), Punct(1, 1), Punct(3, 5), Punct(4, -1)]
    # lista_ponderi = [1, 2, 2, 1]
    # t = 0.33 #float(input("t: "))
    # print(f'r({t}) = {alg_de_Castelijau_rational(lista_puncte, lista_ponderi, t)}')

main()

