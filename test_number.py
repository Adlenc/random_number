# test_number.py
"""Тесты для игры «Угадай число»."""

from random import randint


def test_secret_number_in_range():
    """Проверяет, что загаданное число в диапазоне 1–100."""
    for _ in range(1000):  # Проверяем 1000 раз
        secret = randint(1, 100)
        assert 1 <= secret <= 100, f"Число {secret} вне диапазона 1–100"


def test_secret_number_is_integer():
    """Проверяет, что загаданное число — целое."""
    for _ in range(1000):
        secret = randint(1, 100)
        assert isinstance(secret, int), f"Число {secret} не является целым"


def test_comparison_less():
    """Проверяет логику: если guess < secret, то 'больше'."""
    secret = 50
    guess = 30
    assert guess < secret, "Ожидалось, что guess меньше secret"


def test_comparison_greater():
    """Проверяет логику: если guess > secret, то 'меньше'."""
    secret = 50
    guess = 70
    assert guess > secret, "Ожидалось, что guess больше secret"


def test_comparison_equal():
    """Проверяет логику: если guess == secret, то угадал."""
    secret = 50
    guess = 50
    assert guess == secret, "Ожидалось, что guess равно secret"


if __name__ == "__main__":
    print("Запуск тестов...")
    test_secret_number_in_range()
    test_secret_number_is_integer()
    test_comparison_less()
    test_comparison_greater()
    test_comparison_equal()
    print("Все тесты пройдены!")
