from math import sqrt

def dreapta_prin_ec_generala():
    a = float(input("introduceti a: "))
    b = float(input("introduceti b: "))
    c = float(input(" introduceti c: "))
    if (a == 0 and b == 0):
        raise ValueError("EROARE: nu ati introdus coordonatele corect (a=b=0)!\n")

    dreapta = f'dreapta este d: {a}x+{b}y+{c} = 0 \n'
    print(dreapta)
    return a,b,c

def dreapta_prin_pct_vector():
    print("Fie punctul A(x,y). Introduceti coordonatele punctului:")
    x = float(input("x: "))
    y = float(input("y: "))

    print("Fie vectorul director V(v1,v2). Introduceti coordonatele vectorului: ")
    v1 = float(input("v1: "))
    v2 = float(input("v2: "))

    dreapta = f"dreapta este d:{-v2}x+{v1}y+({(v2*x) - (v1*y)}) = 0 \n"
    print(dreapta)

    if(v1 + v2 == 0):
        raise Exception("ERROR:Vectorul nu se poate anula!")

    a = -v2
    b = v1
    c = (v2*x) - (v1*y)

    if(a == 0 and b == 0):
        raise Exception("ERROR: coordonate gresite(a=b=0)!")

    return a, b, c

def det_punct_intersectie_0y(a, b, c):
    x = 0
    y = -c/b

    return x, y

def det_punct_intersectie_0x(a, b, c):
    x = -c/a
    y = 0

    return x, y

def matrice_poligon(puncte):
    matrix = []
    line_x = []
    line_y = []
    line_1 = []
    for punct in puncte:
        line_x.append(punct[0])
        line_y.append(punct[1])
        line_1.append(1)
    matrix.append(line_x)
    matrix.append(line_y)
    matrix.append(line_1)

    return matrix

def poligon():
    varfuri = float(input("Cate varfuri are poligonul: "))
    if(varfuri <= 0):
        raise Exception("ERROR: Numarul de varfuri trebuie sa fie un intreg pozitiv! ")
    punctele = []
    while(varfuri):
        print("Introduceti coordonatele punctelor: ")
        print(f"Coordonatele punctului P{int(varfuri - (varfuri-1))}:")
        x = float(input("x: "))
        y = float(input("y: "))
        punctele.append((x, y))
        varfuri -= 1

    return punctele

def det_matrice_tranzlatie(x,y):

    matrix = [[1, 0, x],
              [0, 1, y],
              [0, 0, 1]]

    return matrix

def matrix_multiply(matrix1, matrix2):
    matrix = [[sum(a * b for a, b in zip(A_row, B_col))
               for B_col in zip(*matrix2)]
              for A_row in matrix1]

    return matrix

def det_cos_sin(a, b):
    sin = a / (sqrt(a ** 2 + b ** 2))

    cos = -b / (sqrt(a ** 2 + b ** 2))

    return sin, cos

def matrix_rot_teta(cos, sin):
    matrix = [[cos, -sin, 0],
              [sin, cos, 0],
              [0, 0, 1]]

    return matrix

def det_matrice_reflexie_ox():
    matrix = [[1, 0, 0],
              [0, -1, 0],
              [0, 0, 1]]

    return matrix

def det_matrice_reflexie_oy():
    matrix = [[-1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]]

    return matrix

def print_matrix(matrix):
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])

def main():
    print(":)")

    try:
        a = 0
        b = 0
        c = 0
        print("Alegeti metoda in care introduceti dreapta:")
        print("1. Dreapta prin ecuatia generala.")
        print("2. Dreapta prin punct si vector director.")
        optiune = input()
        if (optiune == "1"):
            a, b, c =dreapta_prin_ec_generala()
        elif (optiune == "2"):
            a, b, c = dreapta_prin_pct_vector()

        if(a == 0):
            if(c == 0):
                print("dreapat este Ox!", end="\n")
            else:
                print("dreapat este paralela cu Ox!", end="\n")
            #dreapta este paralela cu Ox
            x, y = det_punct_intersectie_0y(a, b, c)

            t1 = det_matrice_tranzlatie(x, y)
            print("Matricea translatiei care face dreapta sa treaca prin origine este:\n")
            print_matrix(t1)
            print(" ")

            rx = det_matrice_reflexie_ox()
            print("Matricea reflexiei fata de Ox:\n")
            print_matrix(rx)
            print(" ")

            t2 = det_matrice_tranzlatie(x, -y)
            print("Matricea translatiei care aduce dreapta in pozitia initiala este:\n")
            print_matrix(t2)
            print(" ")

            matrice_finala = matrix_multiply(matrix_multiply(t2, rx), t1)
            print("Matricea transformarii compuse este: \n")
            print_matrix(matrice_finala)
            print(" ")

        elif(b == 0):
            if(c==0):
                print('dreapta este Oy!')
            else:
                print("dreapta este paralela cu Oy!", end="\n")
            #dreapta este paralele cu Oy
            x, y = det_punct_intersectie_0x(a, b, c)

            t1 = det_matrice_tranzlatie(x, y)
            print("Matricea translatiei care face dreapta sa treaca prin origine este:\n")
            print_matrix(t1)
            print(" ")

            ry = det_matrice_reflexie_oy()
            print("Matricea reflexiei fata de Oy:\n")
            print_matrix(ry)
            print(" ")

            t2 = det_matrice_tranzlatie(-x, y)
            print("Matricea translatiei care aduce dreapta in pozitia initiala este:\n")
            print_matrix(t2)
            print(" ")

            matrice_finala = matrix_multiply(matrix_multiply(t2, ry), t1)
            print("Matricea transformarii compuse este: \n")
            print_matrix(matrice_finala)
            print(" ")

        elif(c == 0):
            print("dreapta trece prin origine!", end="\n")
            #dreapta tece prin punctul O(0,0), adica prin origine
            sin, cos = det_cos_sin(a, b)

            rot1 = matrix_rot_teta(cos, -sin)
            print("Matricea rotatiei fata de origine care face ca dreapta sa se"
                  "suprapuna peste o axa este: \n")
            print_matrix(rot1)
            print(" ")

            rx = det_matrice_reflexie_ox()
            print("Matricea reflexiei fata de Ox:\n")
            print_matrix(rx)
            print(" ")

            rot2 = matrix_rot_teta(cos, sin)
            print("Matricea rotatiei fata de origine care aduce dreapta la directia initiala este: \n")
            print_matrix(rot2)
            print(" ")

            matrice_finala = matrix_multiply(matrix_multiply(rot2, rx), rot1)
            print("Matricea transformarii compuse este: \n")
            print_matrix(matrice_finala)
            print(" ")

        else:
            #nu avem caz exceptat
            x, y = det_punct_intersectie_0y(a, b, c)
            sin, cos = det_cos_sin(a, b)
            t1 = det_matrice_tranzlatie(x, y)
            print("Matricea translatiei care face dreapta sa treaca prin origine este:\n")
            print_matrix(t1)
            print(" ")

            t2 = det_matrice_tranzlatie(x, -y)
            print("Matricea translatiei care aduce dreapta in pozitia initiala este:\n")
            print_matrix(t2)
            print(" ")

            rot1 = matrix_rot_teta(cos, -sin)
            print("Matricea rotatiei fata de origine care face ca dreapta sa se "
                  "suprapuna peste o axa este: \n")
            print_matrix(rot1)
            print(" ")

            rot2 = matrix_rot_teta(cos, sin)
            print("Matricea rotatiei fata de origine care aduce dreapta la directia initiala este: \n")
            print_matrix(rot2)
            print(" ")

            rx = det_matrice_reflexie_ox()
            print("Matricea reflexiei fata de Ox:\n")
            print_matrix(rx)
            print(" ")

            matrice_finala = matrix_multiply(matrix_multiply(matrix_multiply(matrix_multiply(t2, rot2), rx), rot1), t1)
            print("Matricea transformarii compuse este: \n")
            print_matrix(matrice_finala)
            print(" ")

        print("Alegeti un poligon: ")
        puncte = poligon()
        # matricea formata din punctele poligonului
        m_poligon = matrice_poligon(puncte)

        m_reflexie = matrix_multiply(matrice_finala, m_poligon)
        print("matricea coordonatelor omogene: \n")
        print_matrix(m_reflexie)
        print(" ")

    except Exception as e:
        print(e)
main()