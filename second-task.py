import math


def do_operation(x, y):
    return (2 * math.cos(x - math.pi / 6))/(0.5 + (math.sin(y)**2) ) + (math.fabs(y-x)/3)

x = float(input("Введите x: "))
y = float(input("Введите y: "))

result = do_operation(x, y)

print(f"результат вычисления: {result}")