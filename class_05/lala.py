class Gato:
    def __init__(self,age,color,name = "lala"):
        self.age = age
        self.color = color
        self.name = name
    def sound(self):
        return "miau"
    def __str__(self):
        return "O nome do gato é {}".format(self.name)
g1 = Gato(5.5, "amarelo", "pedro")
print(g1)
g2 = Gato(19, "preto", "tapioca")
print(g2)
g3 = Gato(color = "preto", age = 24)
print(g3)

pato = [g1,g2]
