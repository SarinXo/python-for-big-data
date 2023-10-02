import random

def generate_numbers(n):
    numbers = [random.randint(1, 100) for _ in range(n)]
    return numbers

def calculate_sum(numbers):
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum

def write_to_file(numbers, even_sum, odd_sum):
    with open("output.txt", "w") as file:
        file.write("Сгенерированные числа:\n")
        for num in numbers:
            file.write(str(num) + "\n")
        file.write("\n")
        file.write(f"Сумма чётных чисел: {even_sum}\n")
        file.write(f"Сумма нечётных чисел: {odd_sum}\n")

with open("input.txt", "r") as file:
    n = int(file.readline().strip())

numbers = generate_numbers(n)
even_sum, odd_sum = calculate_sum(numbers)
write_to_file(numbers, even_sum, odd_sum)