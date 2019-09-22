from time import sleep
import ast
def bhaskara():
        x = 0
        print("\nVocê selecionou o calculador de bhaskara, YEAH!")
        a = int(input("Insira o valor de A e tecle <ENTER>"))
        b = int(input("Insira o valor de B e tecle <ENTER>"))
        c = int(input("Insira o valor de C e tecle <ENTER>"))
        print('Calculando', end='', flush='True')
        while x < 4:
            print('.', end='', flush='True')
            x += 1
            sleep(0.3)

        d = b**2 - 4 * a * c
        print("\nO valor de delta é: ", d)
        c = d **(1/2)
        x1 = (-b + c)/2
        x2 = (-b - c)/2
        if d < 0:
                print("O valor de X1 é: ", complex(round(x1.real),round(x1.imag)))
                print("O valor de X2 é: ", complex(round(x2.real),round(x2.imag)))
        else:
                print("O valor de X1 é: ", x1)
                print("O valor de X2 é: ", x2)

def PivoAla():
    x = 0
    print("\nVocê selecionou Pivo e Ala!, YEAH!")
    j = int(input("quantos jogadores a no time?: "))
    armazem = j
    print('Calculando', end='', flush='True')
    while x < 4:
        print('.', end='', flush='True')
        x += 1
        sleep(0.3)
    a = j - 1
    while (a > 10):
        j = j * a
        a = a - 1
    print("\nA conta é:\n", armazem,"!/(",armazem,"! - 10!)")
    print("\nResposta: A ", j, " maneiras!!")

def Preguica():
    x = 0
    print("\nVocê selecionou algo que deu preguiça de programar, UHUUL!!")
    inutil = int(input("Escreva o primeiro numero e tecle <ENTER>\n"))
    print('Descansando', end='', flush='True')
    while x < 8:
        print('.', end='', flush='True')
        x += 1
        sleep(0.3)
    print("\nUsa o photomath, essa aqui ta foda :)")

def imaginario ():
    x = 0
    print("\nVocê selecionou o calculador de operações imaginarias, Yeah!!\nObs:Escreva a operação e depois a potenciação!!!\nEx:(20+2i)+<ENTER>+5")
    operacao = input("Digite a operação e tecle<ENTER>\n")
    potencia = int(input("Digite a potenciação<ENTER>\n"))
    print('Calculando', end='', flush='True')
    while x < 4:
        print('.', end='', flush='True')
        x += 1
        sleep(0.3)
    operacao = operacao.replace(" ", "")
    operacao = operacao.replace("i", "j")
    operacao = operacao.replace("j", "1j")
    resp = complex(eval(operacao))**potencia
    print("\nA resposta é: ", complex(round(resp.real),round(resp.imag)))

def Volei ():
    x = 0
    print("\nVocê selecionou O montador de equipes de volei inutil, SENSACIONAL!")
    m = int(input("Quantas Meninas a no time?: "))
    posi = int(input("Quantas posições a em um time?: "))
    armazem = m
    armazem1 = posi
    print('Calculando', end='', flush='True')
    while x < 4:
        print('.', end='', flush='True')
        x += 1
        sleep(0.3)
    a = m - 1
    b = posi - 1
    lol = armazem - armazem1
    armazem2 = lol
    c = lol - 1
    while (a > 1):
        m = m * a
        a = a - 1
    while (b > 1):
        posi = posi * b
        b = b - 1
    resp = m  /(posi*lol)
    while (c > 1):
        lol = lol * c
        c = c - 1
    resp = m  /(posi*lol)
    print("\nA conta é:\n", armazem,"!/(",armazem1,"! .",armazem2,"!)")
    print("\nDa para fazer ", resp," times diferentes")

def urna ():
    print("\nVocê selecionou a questão da urna, HORA DA CORRUPÇÃO!")
    x = 0
    Bazul = int(input("\nQuantas bolas azuis tem?: "))
    Bverm = int(input("\nQuantas bolas vermelhas tem?: "))
    print('Calculando', end='', flush='True')
    while x < 4:
        print('.', end='', flush='True')
        x += 1
        sleep(0.3)
    a, a1 = Bazul, Bazul
    a -= 1
    v, v1 = Bverm, Bverm
    v -= 1
    s, s1, soma = Bazul + Bverm, Bazul + Bverm, Bazul + Bverm
    s -= 1
    arranjo, ar, ar1 = soma - 3,soma - 3, soma - 3
    ar -= 1
    while (a > 1):
        a1 = a1 * a
        a = a - 1
    while (v > 1):
        v1 = v1 * v
        v = v - 1
    while (s > 1):
       s1 = s1 * s
       s = s - 1
    while (ar > 1):
        ar1 = ar1 * ar
        ar = ar - 1
    respA = s1/(ar1*6)
    print("\nA conta da A é:\n",soma,"!/3!.",arranjo,"!\n")
    print("A respota da questão A é:",respA)
    div1 = a1/(6 *(Bazul - 3))
    div2 = v1/4
    respB = div1*div2
    print ("\nA conta da B é:\n", Bazul,"/3!(",Bazul,"-3)! .",Bverm,"!/2!(",Bverm,"-2)!")
    print("A resposta da B é: ",respB)

def hexagono():
    x = 0
    print("\nVocê selecinou a hexágonos, 'Hexagon Force!'")
    geo = int(input("quantos lados tem a forma geometrica desejada?: "))
    plano = int(input("quantos pontos tem o seu plano?: "))
    print('Calculando', end='', flush='True')
    while x < 4:
        print('.', end='', flush='True')
        x += 1
        sleep(0.3)
    p1, p = plano, plano
    p -= 1
    g1,g = geo, geo
    g -= 1
    base = plano - geo
    b, b1 = base, base
    b -= 1
    while (g > 1):
        g1 = g1 * g
        g = g - 1
    while (p > 1):
        p1 = p1 * p
        p = p - 1
    while (b > 1):
        b1 = b1 * b
        b = b - 1
    resp = p1/(b1*g1)
    print("\nA conta é:\n", plano , "!/(" ,plano, "-" ,geo, ")!." ,geo, "!" )
    print("\nA resposta é:", resp)

def dados():
    x=0
    print('\nCalculando', end='', flush='True')
    while x < 4:
        print('.', end='', flush='True')
        x += 1
        sleep(0.3)
    print("\nVocê escolheu a sorte! pega a questão de graça ai ;)")
    print("""Questão A:(a soma seja primo):
                6x6 = 36 combinações possiveis
                P = 15/36 = 5/12
Questão B:(Soma seja um numero par e menor que 7)
                P = 9/36 = 1/4""")

def loteria():
    print("\nVocê escolheu loteria, $$!")
    loto = int(input("quantos Numeros tem a lototeria?: "))
    aposta = int(input("quantos numeros o o apostador apostou?: "))
    x=0
    print('Calculando', end='', flush='True')
    while x < 4:
        print('.', end='', flush='True')
        x += 1
        sleep(0.3)
    l1, l = loto, loto
    l -= 1
    a1, a = aposta, aposta
    a -= 1
    dif = loto - aposta
    d, d1 = dif,dif
    d -= 1
    while (a > 1):
        a1 = a1 * a
        a = a - 1
    while (l > 1):
        l1 = l1 * l
        l = l - 1
    while (d > 1):
        d1 = d1 * d
        d = d - 1

    resp = l1/(a1*d1)
    print("\nA conta é:\n",loto,"!/(",aposta,"-",loto,")!")
    print("A resposta é: ", resp) 



    









        
    
