class Punct():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def multiply(self, const):
        return Punct(self.x * const, self.y * const, self.z * const)

    def __add__(self, other):
        return Punct(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Punct(self.x - other.x, self.y - other.y, self.z - other.z)

    def __str__(self):
        return f"({self.x} , {self.y} , {self.z})"



def determinarea_lui_r_t(puncte_control, t):
    n = len(puncte_control)
    puncte = puncte_control.copy()
    lista_intermediara = []
    for i in range(n-1):
        for j in range(n-1):
            lista_intermediara.append(puncte[j].multiply(1-t) + puncte[j+1].multiply(t))
        puncte = lista_intermediara
        lista_intermediara = []
        n -= 1

    return puncte


def determinarea_lui_r_derivat_t(puncte_control, t):
    n = len(puncte_control)
    puncte = puncte_control.copy()
    lista_puncte_contol_deriv = []
    lista_intermediara = []
    for i in range(n-1):
        lista_puncte_contol_deriv.append(puncte[i+1].multiply(n-1).__sub__(puncte[i].multiply(n-1)))

    for i in range(n - 2):
        for j in range(n-2):
            lista_intermediara.append(lista_puncte_contol_deriv[j].multiply(1-t) + lista_puncte_contol_deriv[j+1].multiply(t))
        lista_puncte_contol_deriv = lista_intermediara
        lista_intermediara = []
        n -= 1

    return lista_puncte_contol_deriv


def main():
    try:
    #grad curba
        gard_curba = int(input("Introduceti gradul curbei Bezier:\n"))

    #puncte de control
        puncte_control = []
        print("Introduceti punctele de control: ")
        for i in range(gard_curba + 1):
            print(f"Coordonatele punctului P{i}")
            x = float(input("x: "))
            y = float(input("y: "))
            z = float(input("z: "))
            puncte_control.append(Punct(x, y, z))

    #Introducerea constantei t
        t = float(input("introduceti t (0<= t <= 1): "))
        if t < 0 or t > 1:
            raise ValueError("Valoare incorecta!")

    #determinarea lui r(t)
        r_t = determinarea_lui_r_t(puncte_control, t)

        print(f"r({t}) = {r_t[0]}")

    #determinarea lui r'(t)
        r_deriv_t = determinarea_lui_r_derivat_t(puncte_control, t)
        print(f"r'({t}) = {r_deriv_t[0]}")



    except ValueError as e:
        print(e)
main()
