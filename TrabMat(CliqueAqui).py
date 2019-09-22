from time import sleep
from trabmatMenu import *
from trabMatQ import *
x = 0
print('~-' * 40)
print('SUPER PROGRAMA DO TRABALHO DE MATEMATICA!!')
print('~-' * 40)
opcao = menu()

while opcao >= 1:
    
    if opcao == 1:
        bhaskara()
        
    elif opcao == 2:
       PivoAla()
       
    elif opcao == 3:
        Preguica()
        
    elif opcao == 4:
        imaginario()
        
    elif opcao == 5:
        Preguica()
        

    elif opcao == 6:
        Volei()
        
    elif opcao == 7:
        urna()
        
    elif opcao == 8:
        hexagono()
        
    elif opcao == 9:
        dados()
        
    elif opcao == 10:
        loteria()
        
    opcao = retorna()
print("""\nObrigado por usar o programa <3
              made by: Raphael Branco""")
sleep(5.0)

        






    

    
    
