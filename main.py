from collections import Counter
from math import pi

# ex. 1
print("ex. 1")
list1 = [["Ana", 8.5], ["Mihai", 6.0], ["Ion", 6.0], ["Maria", 9.0]]
first = float('inf')
second = float('inf')

for i in range(len(list1)):
    if list1[i][1] < first:
        second = first
        first = list1[i][1]
    elif list1[i][1] < second and list1[i][1] != first:
        second = list1[i][1]

res = [e[0] for e in list1 if e[1] == second]
for e in sorted(res):
    print(e)
print()

# ex. 2
print("ex. 2")
str2 = "Marco"
str3 = "ab"
str_res2 = str2[:3] * 3
str_res3 = str3[:3] * 3
print(str_res2)
print(str_res3, "\n")

# ex. 3
print("ex. 3")
a1 = [1, 10, 9, 10, 8]
b2 = [10, 9, 10, 7, 6]
b1 = [8, 10, 9, 7, 6]

def ex_3(a, b):
    for i in range(len(a) - 2):
        slice1 = a[i:i + 3]
        for j in range(len(b) - 2):
            if slice1 == b[j:j + 3]:
                return True
    return False

print(ex_3(a1, b1))
print(ex_3(a1, b2), "\n")

# ex. 4
print("ex. 4")
f = open("ex4.txt", "r")
dict4 = {}
line = f.readline()
while line:
    list_of_words = line.split()
    for e in list_of_words:
        if e not in dict4:
            dict4[e] = 1
        else:
            dict4[e] += 1
    line = f.readline()
print(dict4.items(), "\n")

f.close()

# ex. 5
print("ex. 5")
list5 = ["mar", "par", "mar", "banana", "mar", "banana"]
freq = Counter(list5)

n = 2
top_elements = freq.most_common(n)

print(freq)
print(top_elements, "\n")

# ex. 6
print("ex. 6")

a6 = [1, 2, 3]
b6 = ["a", "b", "c"]
for i, e in list(zip(a6, b6)):
    print(i, e)
print()

# ex. 7
print("ex. 7")
list7 = [[1, 2, 3, 5], ["arc", 4, 7.4], [1, "lego", 4.5, False]]
list_flatten = [i for e in list7 for i in e]
print(list_flatten, "\n")

# ex. 8
print("ex. 8")

class GeometricForm:
    def getArea(self):
        pass

    def getPerimeter(self):
        pass

class Rectangle(GeometricForm):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

    def getPerimeter(self):
        return 2 * (self.length + self.width)

class Circle(GeometricForm):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def getArea(self):
        return self.radius * self.radius * pi

    def getPerimeter(self):
        return 2 * pi * self.radius

rect = Rectangle(100, 200)
circle = Circle(50)

print(f"Rectangle: area {rect.getArea()}, perimeter: {rect.getPerimeter()}")
print(f"Circle: area {circle.getArea()}, perimeter: {circle.getPerimeter()}\n")

# ex. 9
print("ex. 9")
class Complex():
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return (self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return (self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return (self.real * other.real - self.imag * other.imag,
                self.real * other.imag + self.imag * other.real)

nr1 = Complex(3, 2)
nr2 = Complex(5, 6)
print(nr1 + nr2)
print(nr1 - nr2)
print(nr1 * nr2)