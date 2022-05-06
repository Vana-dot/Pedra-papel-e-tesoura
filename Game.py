from random import randint

print('''Opções de partida:
        1-Partida unica
        3-Melhor de 3
        5-Melhor de 5
        '''
        )
nump=int(input('Informe o número de partidas:'))

if(nump == 1):
        stop = 's'
        for i in range(1):
          i = ['Pedra','Papel','Tesoura']
          print('')
          print("""Opções:
            0->Pedra
            1->Papel
            2->Tesoura \n"""
            )
          jgd = int(input('Qual sua jogada:'))
          pc=randint(0,2)

          if jgd>=3:
             print("Opção invalida")
             stop = input('Vamos jogar novamente? s/n:')
          if pc == 0:
            if jgd == 0:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Empate!!')
            elif jgd == 1:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Jogador venceu')
            elif jgd == 2:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Pc venceu')
          elif pc == 1:
            if jgd == 0:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Pc venceu')
            elif jgd == 1:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Empate!!')
            elif jgd == 2:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Jogador venceu')
          elif pc == 2:
            if jgd == 0:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Jogador venceu')
            elif jgd == 1:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Pc venceu')
            elif jgd == 2:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Empate!!')

elif(nump == 3):
       stop ='s'
       for i in range(3):
          i = ['Pedra','Papel','Tesoura']
          print('')
          print("""Opções:
            0->Pedra
            1->Papel
            2->Tesoura \n"""
            )
          jgd = int(input('Qual sua jogada:'))
          pc=randint(0,2)
          if jgd>=3:
             print("Opção invalida")
             stop = input('Vamos jogar novamente? s/n:')
          if pc == 0:
            if jgd == 0:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Empate!!')
            elif jgd == 1:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Jogador venceu')
            elif jgd == 2:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Pc venceu')
          elif pc == 1:
            if jgd == 0:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Pc venceu')
            elif jgd == 1:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Empate!!')
            elif jgd == 2:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Jogador venceu')
          elif pc == 2:
            if jgd == 0:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Jogador venceu')
            elif jgd == 1:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Pc venceu')
            elif jgd == 2:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Empate!!')
                 
elif(nump == 5):
       stop='s'
       for i in range(5):
          i = ['Pedra','Papel','Tesoura']
          print('')
          print("""Opções:
            0->Pedra
            1->Papel
            2->Tesoura\n"""
            )
          jgd = int(input('Qual sua jogada:'))
          pc=randint(0,2)
          if jgd>=3:
             print("Opção invalida")
             stop = input('Vamos jogar novamente? s/n:')
          if pc == 0:
            if jgd == 0:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Empate!!')
            elif jgd == 1:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Jogador venceu')
            elif jgd == 2:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Pc venceu')
          elif pc == 1:
            if jgd == 0:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Pc venceu')
            elif jgd == 1:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Empate!!')
            elif jgd == 2:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Jogador venceu')
          elif pc == 2:
            if jgd == 0:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Jogador venceu')
            elif jgd == 1:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Pc venceu')
            elif jgd == 2:
                print('='*25)
                print('Computador jogou {}'.format(i[pc]))
                print('Jogador jogou {}'.format(i[jgd]))
                print('='*25)
                print('')
                print('Empate!!')

