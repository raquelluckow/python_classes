par = [0]*5
impar = [0]*5
count_par = 0
count_impar = 0

for i in range (15):
    n = int(input())
    if n %2 == 0:
        if count_par == 5:
            print(f'par[0] = {par[0]}')
            print(f'par[1] = {par[1]}')
            print(f'par[2] = {par[2]}')
            print(f'par[3] = {par[3]}')
            print(f'par[4] = {par[4]}')
            par = [0]*5
            count_par = 0
        else:
            par[count_par] = n
            count_par += 1
        #par.append(n)
    elif n %2 != 0:
        if count_impar == 5:
            print(f'impar[0] = {impar[0]}')
            print(f'impar[1] = {impar[1]}')
            print(f'impar[2] = {impar[2]}')
            print(f'impar[3] = {impar[3]}')
            print(f'impar[4] = {impar[4]}')
            impar = [0]*5
            count_impar = 0
        else:
            impar[count_impar] = n
            count_impar += 1
        #impar.append(n)
#NÃO SEI RESOLVER O INDEX PQ VAI PASSAR DE 5

   
