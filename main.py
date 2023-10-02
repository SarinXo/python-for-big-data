import datetime

def calculate_seconds_in_years():
    x = int(input("Введите номер компьютера: "))
    current_year = datetime.datetime.now().year
    years = current_year + x
    seconds_in_a_year = 365 * 24 * 60 * 60
    total_seconds = years * seconds_in_a_year
    return total_seconds

result = calculate_seconds_in_years()

print(f"Количество секунд в X годах: {result}")