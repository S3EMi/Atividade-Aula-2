import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def restart():
    def gotor():
        pause()
        if pause == "":
            clearConsole()
            restart()
        else:
            clearConsole()
            restart()

    def pause():
        input("\nPressione ENTER para continuar...")

    numb = input("\n-----------------------\nDigite o número: ")
    try:
        float(numb)
    except ValueError:
        print("Erro: Ocorreu um erro, tente novamente.")
        gotor()
    result = float(numb) % 2
    if result > 0:
        print("\nO número", numb, "é ímpar.")
        print(numb, " / 2", " = ", float(numb)/2, " ou ", numb, " com resto ", result)
        gotor()
    else:
        print("O número dado é par.")
        gotor()

restart()
