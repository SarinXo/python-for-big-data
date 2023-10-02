import random

def generate_code():
    colors = ['R', 'G', 'B']
    code = ''
    for _ in range(4):
        code += random.choice(colors)
    return code

def check_guess(code, guess):
    exact_matches = 0
    color_matches = 0
    for i in range(4):
        if guess[i] == code[i]:
            exact_matches += 1
        elif guess[i] in code:
            color_matches += 1
    return exact_matches, color_matches

def play_game():
    print("The MASTERMIND Game")
    code = generate_code()
    solved = False
    attempts = 0
    while not solved:
        guess = input("Ваше предположение: ").upper()
        if len(guess) != 4 or any(color not in ['R', 'G', 'B'] for color in guess):
            print("Неверное предположение. Пожалуйста, введите правильную отгадку с четырьмя цветами: R, G, B.")
            continue
        attempts += 1
        exact_matches, color_matches = check_guess(code, guess)
        print(f"{exact_matches} {color_matches}")
        if exact_matches == 4:
            solved = True
            print("Поздравляем! Вы решили головоломку!")
            print(f"Вам потребовалось {attempts} попыток.")

play_game()
