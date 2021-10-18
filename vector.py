class Vector:
    def __init__(self, a):
        self.x, self.y, self.z = map(int, a.split(", "))
    def __add__(self, other):
        return self.x + other.x, self.y + other.y, self.z + other.z
    def __sub__(self, other):
        return self.x - other.x, self.y - other.y, self.z - other.z
    def __mul__(self, other):
        return self.x * other.x, self.y * other.y, self.z * other.z
    def __str__(self):
        return "("+str(self.x)+','+str(self.y)+','+str(self.z)+")"
    def length(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (1 / 2)
    #ploshyad
    def area(self, other):
        return (((self.x ** 2 + self.y ** 2) * (other.x ** 2 + other.y ** 2)(1 - (self.x * other.x + self.y * other.y)) ** (1 / 2)) / ((self.x ** 2 + self.y ** 2) ** (1 / 2)) * (other.x ** 2 + self.y ** 2) ** (1 / 2))
    #obyem
    def volume(u, v, w):
        return abs(u.x * (v.y * w.z - v.z * w.y) - u.y * (v.x * w.z - w.x * v.z) + u.z * (v.x * w.y - v.y * w.z))

    def centrmass(u, v, w):
        return (u.x + v.x + w.x) / 3, (u.y + v.y + w.y) / 3, (u.z + v.z + w.z) / 3

#Наиболее удаленная точка:
N = int(input())
mas = []
while N!= 0:
        point = input()
        U = Vector(point)
        mas.append(U.length())
        if U.length() == max(mas):
            s = U
        N -= 1
print(s.__str__())

a = input()
b = input()
c = input()
A = Vector(a)
B = Vector(b)
C = Vector(c)
p = area(A,B)
print(p)
print(volume(A, B, C))
print(centrmass(A, B, C))

