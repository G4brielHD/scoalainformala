from fractions import Fraction

class Fractie:

    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor


    def __str__(self):
        return str(self.numarator)+"/"+str(self.numitor)

    def __add__(self, otherfraction):
        newnumarator = self.numarator*otherfraction.numitor + self.numitor*otherfraction.numarator
        newnumitor = self.numitor*otherfraction.numitor
        common = gcd(newnumarator, newnumitor)
        return Fractie(newnumarator//common, newnumitor//common)

    def __sub__(self, otherfraction):
        newnumarator = self.numarator*otherfraction.numitor - self.numitor*otherfraction.numarator
        newnumitor = self.numitor*otherfraction.numitor
        common = gcd(newnumarator, newnumitor)
        return Fractie(newnumarator//common, newnumitor//common)

# inverse nu am gasit nicicum cum sa fac. Am incercat mai jos insa nu imi returneaza nimic .. :(

    # def __invert__(self, numarator, numitor):
    #     return Fractie(self.numarator, self.numitor * -1)

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


f1 = Fractie(9,6)
f2 = Fractie(4,7)
f3 = f1+f2
f4 = f1-f2
print(f3)
print(f4)






































