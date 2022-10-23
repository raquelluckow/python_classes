number = int(input())
d_1 = number//100
r_1 = number%100
d_2 = r_1//50
r_2 = r_1%50
d_3 = r_2//20
r_3 = r_2%20
d_4 = r_3//10
r_4 = r_3%10
d_5 = r_4//5
r_5 = r_4%5
d_6 = r_5//2
r_6 = r_5%2
#print(d_1,d_2,d_3,d_4,d_5,d_6)
#print(r_1,r_2,r_3,r_4,r_5,r_6)
#COMO PRINTAR COM ENTENR?
print(number)
print(str(d_1) + ' nota(s) de R$ 100,00')
print(str(d_2) + ' nota(s) de R$ 50,00')
print(str(d_3) + ' nota(s) de R$ 20,00')
print(str(d_4) + ' nota(s) de R$ 10,00')
print(str(d_5) + ' nota(s) de R$ 5,00')
print(str(d_6) + ' nota(s) de R$ 2,00')
print(str(r_6) + ' nota(s) de R$ 1,00')