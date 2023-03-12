andar_1 = int(input())
andar_2 = int(input())
andar_3 = int(input())
total_min = 100000

def tempo_andar(pessoas,andar,cafeteira):
    tempo = 2*pessoas*abs(cafeteira-andar)
    return tempo

for i in range(3):
    cafeteira = i
    total = tempo_andar(andar_1,1,cafeteira) + tempo_andar(andar_2,2,cafeteira) + tempo_andar(andar_3,3,cafeteira)
    total_min = min(total,total_min)
print(total_min)


