class Fractie:

    numarator = "numarator"
    numitor = "numitor"

    def __init__(self,numarator,numitor):   # instanțiem numărător și numitor
        self.numarator = numarator
        self.numitor = numitor


    def __str__(self):                      # afisam "numărător/numitor"
        return str(self.numarator) + ' / ' + str(self.numitor) + " = " + str(self.numarator/self.numitor)


    def __add__(self, other):           # returnam o noua fractie care reprezinta adunarea
        fractie_1 = self.numarator + other.numarator
        fractie_2 = self.numitor
        return Fractie(fractie_1,fractie_2)


    def __sub__(self, other):           # returnam o nouă fracție care reprezinta scădearea
        fractie_3 = self.numarator - other.numarator
        fractie_4 = self.numitor
        return Fractie(fractie_3, fractie_4)


    def inverse(self):                        #returnează o nouă fracție (inversa fracției)
        y = int(self.numarator)
        z = int(self.numitor)
        return Fractie.__str__(Fractie(z,y))



a = Fractie(20,2)
b = Fractie(40,2)
c = Fractie(10,3)               # daca sunt numitori diferiti, imi ia numitorul acestei instante.
d = Fractie(100,2)              # nu inteleg de ce tocmai numitorul de la "c" mi-l ia ca principal.

fractie_final =  c - a - b + c

print(fractie_final)

print(Fractie.__str__(Fractie(10,2)))

print(Fractie.inverse(Fractie(10,2)))


