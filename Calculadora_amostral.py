

import os

def titulo(txt):
    print('-'*70)
    print(txt)
    print('-'*70)


titulo('                        TRABALHO INDIVIDUAL 2         ')
titulo('                        CALCULADORA AMOSTRAL          ')
titulo('  ESTA CALCULADORA FOI CRIADA PARA CALCULAR O TAMANHO DE UMA AMOSTRA     ')

tam_populacao = int(input("Digite a população: ")) 

margem_de_erro = int(input('Escolha a margem de erro: '))

margem_de_erro = margem_de_erro / 100 # converter em porcentagem 

amostra_inicial = 1 / margem_de_erro ** 2

amostra = (tam_populacao * amostra_inicial)/(tam_populacao + amostra_inicial)

print('Para uma população de {}, a amostra é de {:.0f} habitantes, a margem de erro é de {:.0%}'.format(tam_populacao, amostra, margem_de_erro))






bom = 0
ruim = 0

while True:
    
    print(f'TOTAL BOM: {bom} {os.linesep}TOTAL RUIM:{ruim}')

    votos = float(input(f'Se você acha que o serviço está bom Digite - 1 {os.linesep}Se você acha que o serviço está ruim: digite - 2{os.linesep}Seu voto: '))
    try:
        if votos == 1:
            bom += 1
        elif votos == 2:
            ruim += 1
        
        else:
            pass
    except:

        print('Digite apenas 1 ou 2')
    os.system('cls')
    if (bom + ruim) > amostra - 1:
            print('*'*20)
            print('VOTAÇÃO ENCERRADA')
            print('*'*20)
            break

amostra = amostra /100

bom = (bom * 0.01 / amostra)
ruim = (ruim * 0.01 / amostra) 

print('o total de votos bons foram {:.2%} com uma margem de erro de {:.0%} para mais ou para menos'.format(bom, margem_erro))
print('o total de votos ruim foram {:.3%} com uma margem de erro de {:.0%} para mais ou para menos'.format(ruim, margem_erro))

       
    




    









 



