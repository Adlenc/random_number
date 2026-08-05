from random import randint


def main():
    """Основная функция игры «Угадай число»."""
    # Приветствие
    print("Добро пожаловать в игру «Угадай число»!")
    print("Я загадал число от 1 до 100. Попробуй угадать его.")

    # Загадываем случайное число от 1 до 100
    secret_number = randint(1, 100)

    # Счётчик попыток
    attempts = 0

    # Главный игровой цикл
    while True:
        # Запрашиваем ввод у пользователя
        user_input = input("Введите число: ")

        # Обработка ошибок ввода
        try:
            guess = int(user_input)
        except ValueError:
            print("Ошибка: введите целое число.")
            continue

        # Увеличиваем счётчик попыток (засчитываем любую попытку с числом)
        attempts += 1

        # Проверка диапазона
        if guess < 1 or guess > 100:
            print("Ошибка: число должно быть от 1 до 100.")
            continue

        # Сравниваем введённое число с загаданным
        if guess < secret_number:
            print("Загаданное число больше.")
        elif guess > secret_number:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляю! Вы угадали число за {attempts} попыток!")
            break


if __name__ == "__main__":
    main()
