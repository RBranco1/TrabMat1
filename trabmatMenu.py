from time import sleep
def menu():
    x = 0
    print("""MENU
    1- Questão 1 - Bhaskara
    2- Questão 2 - Pivo e Ala
    3- Questão 3 - Operadores pares
    4- Questão 4 - Imaginarios
    5- Questão 5 - Operadores pares
    6- Questão 6 - Volei
    7- Questão 7 - Urna
    8- Questão 8 - Hexagono
    9- Questão 9 - Dados
    10- Questão 10 - Loteria
    0- Sair.
        """)

    opcao = int(input('Selecione uma opção: '))
    print('Processando informação', end='', flush='True')
    while x < 4:
        print('.', end='', flush='True')

        x += 1
        sleep(0.3)
    return opcao
def retorna():
    q = input("Gostaria de retornar ao menu?(S/N) ")
    if q == 'S':
        opcao = menu()
        return opcao
    elif q == 's':
        opcao = menu()
        return opcao
    else:
        opcao = 0
        return opcao

