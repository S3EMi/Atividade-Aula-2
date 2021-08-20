# Nome: Matheus de Paula Barros
# Série: 2 ano EM

import math as mt

def pause():
    input("\nPressione ENTER para continuar")


a = float(input("Primeiro número (a): "))
b = float(input("Segundo número (b): "))
c = float(input("Terceiro número (c): "))

try:
    float(a), float(b), float(c)
except ValueError:
    print("Um ou mais valores dados não foram identificados")
    pause()
    exit()

disc = (b**2 - 4*a*c)
try:
    res1 = (-b - mt.sqrt(disc))/(2*a)
    res2 = (-b + mt.sqrt(disc))/(2*a)
except (ZeroDivisionError, ValueError):
    print("Erro de domínio matemático")
    pause()
    exit()

print("\nx' = ", res1)
print("x'' = ", res2)

pause()
