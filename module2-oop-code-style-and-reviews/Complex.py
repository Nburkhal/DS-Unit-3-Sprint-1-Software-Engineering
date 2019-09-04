
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    @property
    def real(self):
        return self.r

    @property
    def imaginary(self):
        return self.i

    @property
    def value(self):
        return [self.r, self.i]  # an array makes more sense

    def __add__(self, other):
        return [self.r + other.r, self.i + other.i]


    