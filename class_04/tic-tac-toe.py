velha = {'top-L' : '', 'top-M': '', 'top-R': '',
        'mid-L': '', 'mid-M': '', 'mid-R': '',
        'low-L': '', 'low-M': '', 'low-R': '' }

def printvelha(jogo):
    print('{0: >5}{}'.format(jogo['top-L'], "|") + jogo['top-M'] + ' |' + jogo['top-R'])
    print('-----')
    print(jogo['mid-L'] + ' |' + jogo['mid-M'] + ' |' + jogo['mid-R'])
    print('-----')
    print(jogo['low-L'] + ' |' + jogo['low-M'] + ' |' + jogo['low-R'])

turn = 'X'

for i in range(9):
    printvelha(velha)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    velha[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printvelha(velha)

#COMO TIRAR O ESPAÇO?