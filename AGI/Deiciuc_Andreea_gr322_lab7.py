# Scrieti un program (in Python) care sa determine un punct de pe o curba B-spline
# cubica, in,plan, cu 5 puncte de control, folosind algoritmul lui
# Boor.
class Punct():
    def __init__(self, x, y, ):
        self.x = x
        self.y = y



    def multiply(self, const):
        return Punct(self.x * const, self.y * const)

    def __add__(self, other):
        return Punct(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Punct(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x} , {self.y})"

#consola
def puncte_de_control():
    lista_puncte = []
    for i in range(0, 5):
        x = float(input("Dati valoarea coordonatei x: "))
        y = float(input("Dati valoarea coordonatei y: "))
        lista_puncte.append(Punct(x, y))

    return lista_puncte

def noduri():
    lista_noduri = []
    for i in range(0, 9):
        nod = float(input("Introduceti valoarea nodului: "))
        lista_noduri.append(nod)
    return lista_noduri

#fisier
def puncte_de_control_file():
    lista_puncte = []
    with open("punct_de_control.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            x = float(line.split(',')[0])
            y = float(line.split(",")[1])
            punct = Punct(x, y)
            lista_puncte.append(punct)
    return lista_puncte


def noduri_file():
    noduri = []
    with open("noduri.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            noduri.append(float(line))

    return noduri

# def read_file():
#     lista_puncte = []
#     noduri = []
#     t = 0
#     with open("info.txt", 'r' ) as f:
#         lines = f.readlines()
#         for line in lines:
#             if len(line) == 2:
#                 x = float(line.split(',')[0])
#                 y = float(line.split(",")[1])
#                 punct = Punct(x, y)
#                 lista_puncte.append(punct)
#             elif len(line) == 1:
#                 noduri.append(float(line))
#             elif line.__eq__( f"t =" )
#





def algoritmul_lui_Boor(t,puncte_de_control, noduri):
    """
    Algoritmul lui Boor pentru determinarea unui punct
     r(t) de pe o curba B-spline cubica
    :param t:
    :param puncte_de_control: lista cu punctele de control
    :param noduri: lista de noduri
    :return: r(t) ( punctul de pe curba)
    """

    t3 = noduri[3]
    t5 = noduri[5]

    if t3 > t  and t > t5:
        raise ValueError(f'Valoare incorecta! t>{t5} or t<{t3}')

    #algoritmul lui boor
    for k in range(1, 4):
        for i in range(1, 4):
            alfa = (t - noduri[i])/(noduri[3+1+i-k] - noduri[i])
            d = puncte_de_control[i-1].multiply(1-alfa).__add__(puncte_de_control[i].multiply(alfa))
            r_t = d
    return r_t

def meniu():
    print("1.Introduceti date consola:\n"
          "2.Introduceti date din fisier:\n")

    op = int(input("1 sau 2: "))
    if op == 1:
        print("Introduceti cele 5 puncte: ")
        lista_puncte = puncte_de_control()
        print("Introduceti cele 9 noduri")
        list_noduri = noduri()
        print(f"Introduceti t({list_noduri[3]} <= t <= {list_noduri[5]}: ")
        t = float(input("t: "))
        print("Aplicam alboritmul lui Boor pentru a determina un punct de pe curba: \n")
        r_t = algoritmul_lui_Boor(t, lista_puncte, list_noduri)
        print(r_t)
    elif op == 2:
        lista_puncte = puncte_de_control_file()
        lista_noduri = noduri_file()
        print(f"Introduceti t({lista_noduri[3]} <= t <= {lista_noduri[5]}: ")
        t = float(input("t: "))
        print("Aplicam alboritmul lui Boor pentru a determina un punct de pe curba: \n")
        r_t = algoritmul_lui_Boor(t, lista_puncte, lista_noduri)
        print(r_t)

    else:
        print("Optiune gresita!Reincercati!")
def main():
    meniu()

main()
