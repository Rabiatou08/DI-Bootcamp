import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter}, area={self.area()})"

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius


# Tests
c1 = Circle(5)
c2 = Circle(3)
c3 = Circle(7)

print(c1)                    # Circle(radius=5, diameter=10, area=78.54)
print(f"Aire : {c1.area()}")
print(f"Diamètre : {c1.diameter}")

# Setter diamètre
c1.diameter = 20
print(f"Nouveau rayon : {c1.radius}")  # 10.0

# Additionner
c4 = c1 + c2
print(f"c1 + c2 = {c4}")

# Comparer
print(f"c1 > c2 : {c1 > c2}")
print(f"c1 == c2 : {c1 == c2}")

# Trier
circles = [c3, c2, c1]
circles_sorted = sorted(circles)
print(f"Triés : {circles_sorted}")