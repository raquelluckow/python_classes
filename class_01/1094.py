n_testes = int(input())
t = 0
coelhos = 0
ratos = 0
sapos = 0
for i in range(n_testes):
    n, tipo = input().split(" ")
    #n = int(input())
    #tipo = str(input())
    n = int(n)
    t += n
    if tipo == "C":
        coelhos += n
    elif tipo == "R":
        ratos += n
    elif tipo == "S":
        sapos += n
perc_c = (coelhos/t)*100
perc_r = (ratos/t)*100
perc_s = (sapos/t)*100

print("Total: {} cobaias".format(t))
print("Total de coelhos: {}".format(coelhos))
print("Total de ratos: {}".format(ratos))
print("Total de sapos: {}".format(sapos))
print("Percentual de coelhos: {:.2f} %".format(perc_c))
print("Percentual de ratos: {:.2f} %".format(perc_r))
print("Percentual de sapos: {:.2f} %".format(perc_s))

#%.1f' %(average))

