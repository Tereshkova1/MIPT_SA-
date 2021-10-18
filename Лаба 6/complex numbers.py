class Complex:
    def __init__(self, re, i):
        self.re = re
        self.im = i
    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)
    def __mul__(self, other):
        return Complex(self.re * other.re + self.im * other.im *(-1), self.im * other.re + self.re * other.im)
    def __truediv__(self, other):
        return Complex((self.re * other.re - self.im * other.im) / (other.re * other.re + other.im * other.im), (other.re * self.im - self.re * other.im) / (self.im * self.im + other.im * other.im))
    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)
    def __abs__(self):
        return (self.re ** 2 + self.im ** 2) ** (1 / 2)
    def __str__(self):
        if self.im>0:
            return str(self.re) +"+" + str(self.im) + "i"
        elif self.im == 0:
            return str(self.re)
        else:
            return str(self.re) + str(self.im) + "i"

A = Complex(1, 1)
B = Complex(1, -2)
print((A+B).__str__())
print((A-B).__str__())
print((A*B).__str__())
print((A/B).__str__())
print((abs(A).__str__()))

