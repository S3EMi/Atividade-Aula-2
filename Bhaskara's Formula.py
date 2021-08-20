# Nome: Matheus de Paula Barros
# Série: 2 ano EM

import math as mt

def restart():
    def gotor():
        if pause() == "":
            restart()
        else:
            restart()

    def pause():
        input("\nPressione ENTER para continuar...")

    a = input("Primeiro número (a): ")
    b = input("Segundo número (b): ")
    c = input("Terceiro número (c): ")
    try:
        float(a), float(b), float(c)
    except ValueError:
        print("Um ou mais valores dados não foram identificados")
        gotor()

    a = float(a)
    b = float(b)
    c = float (c)
    disc = (b**2 - 4*a*c)
    try:
        res1 = (-b - mt.sqrt(disc))/(2*a)
        res2 = (-b + mt.sqrt(disc))/(2*a)
    except ZeroDivisionError:
        print("Erro: não é possível dividir por 0")
        gotor()
    except ValueError:
        print("Erro de domínio matemático")
        gotor()

    print("\nx' = ", res1)
    print("x'' = ", res2)
    gotor()

restart()
