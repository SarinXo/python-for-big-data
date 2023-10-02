import math


def found_roots(a, b, c):
    D = b**2 - 4*a*c
    if D>=0:
        return (-b + math.sqrt(D))/(2*a), (-b - math.sqrt(D))/(2*a)
    return "нет корней"

a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

result = found_roots(a, b, c)
print(f"Корень(ни) уравнения: {result}")
