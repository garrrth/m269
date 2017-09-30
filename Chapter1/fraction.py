class Fraction:

    def __init__(self, top, bottom):
        
        if not isinstance(top, int):
            raise TypeError(str(top)+" is not of type Integer")

        if not isinstance(bottom, int):
            raise TypeError(str(bottom)+" is not of type Integer")

        if bottom < 0:
            top = top*-1
            bottom = bottom*-1

        common = gcd(top, bottom)

        self.num = top//common
        self.den = bottom//common

    def __str__(self):

        return str(self.num)+"/"+str(self.den)

    def __add__(self, otherfraction):

        if isinstance(otherfraction, int):
            otherfraction = intToFraction(otherfraction)

        newnum = self.num*otherfraction.den + \
                    self.den*otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

    def __radd__(self, otherfraction):

        if isinstance(otherfraction, int):
            otherfraction = intToFraction(otherfraction)

        newnum = self.num*otherfraction.den + \
                    self.den*otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

    def __sub__(self, otherfraction):

        if isinstance(otherfraction, int):
            otherfraction = intToFraction(otherfraction)

        newnum = self.num * otherfraction.den - \
                self.den * otherfraction.num

        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

    def __mul__(self, otherfraction):

        if isinstance(otherfraction, int):
            otherfraction = intToFraction(otherfraction)

        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

    def __truediv__(self, otherfraction):

        if isinstance(otherfraction, int):
            otherfraction = intToFraction(otherfraction)

        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num

        return Fraction(newnum, newden)

    def __eq__(self, otherfraction):

        if isinstance(otherfraction, int):
            otherfraction = intToFraction(otherfraction)

        firstnum = self.num * otherfraction.den
        secondnum = self.den * otherfraction.num

        return firstnum == secondnum

    def __gt__(self, otherfraction):

        if isinstance(otherfraction, int):
            otherfraction = intToFraction(otherfraction)

        firstnum = self.num * otherfraction.den
        secondnum = self.den * otherfraction.num

        return firstnum > secondnum

    def __lt__(self, otherfraction):

        if isinstance(otherfraction, int):
            otherfraction = intToFraction(otherfraction)

        firstnum = self.num * otherfraction.den
        secondnum = self.den * otherfraction.num

        return firstnum < secondnum

    def __ge__(self, otherfraction):

        if isinstance(otherfraction, int):
            otherfraction = intToFraction(otherfraction)

        firstnum = self.num * otherfraction.den
        secondnum = self.den * otherfraction.num

        return firstnum >= secondnum

    def __le__(self, otherfraction):

        if isinstance(otherfraction, int):
            otherfraction = intToFraction(otherfraction)

        firstnum = self.num * otherfraction.den
        secondnum = self.den * otherfraction.num

        return firstnum <= secondnum

    def __ne__(self, otherfraction):

        if isinstance(otherfraction, int):
            otherfraction = intToFraction(otherfraction)

        firstnum = self.num * otherfraction.den
        secondnum = self.den * otherfraction.num

        return firstnum != secondnum

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

# HELPER METHODS #

def gcd(m,n):

    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn

    return n

def intToFraction(n):
    return Fraction(n, 1)
