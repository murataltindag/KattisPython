import math


def reverse_triangle(x):
    n = (-1 + math.sqrt(1 + 8*x)) / 2
    return int(n) if n.is_integer() else None

print(reverse_triangle(1))
print(reverse_triangle(3))
print(reverse_triangle(6))
print(reverse_triangle(10))
print(reverse_triangle(15))
print(reverse_triangle(21))
print(reverse_triangle(28))
print(reverse_triangle(36))
print(reverse_triangle(45))
print(reverse_triangle(55))
print(reverse_triangle(66))
print(reverse_triangle(78))
print(reverse_triangle(91))

print(reverse_triangle(2))
print(reverse_triangle(4))
print(reverse_triangle(5))
print(reverse_triangle(7))