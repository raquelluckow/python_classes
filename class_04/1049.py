data = {
    "vertebrado": {
        "ave": {
            "carnivoro": "aguia",
            "onivoro": "pomba"
        },
        "mamifero": {
            "onivoro": "homem",
            "herbivoro": "vaca"
        }
    }, 
    "invertebrado": {
        "inseto": {
            "hematofago": "pulga",
            "herbivoro": "lagarta"
        },
        "anelideo": {
            "hematofago": "sanguessuga",
            "onivoro": "minhoca"
        }
    }
}

#input1 = input()
#input2 = input()
#input3 = input()

print(data[input()][input()][input()])
