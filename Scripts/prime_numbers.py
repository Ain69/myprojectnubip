# prime_numbers.py

def is_prime(n):
    """Перевірка, чи є число простим."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes(a, b):
    """Виведення всіх простих чисел між a та b (не обов'язково a < b)."""
    if a > b:
        a, b = b, a  # Переміщаємо a та b у правильний порядок
    for num in range(a, b + 1):
        if is_prime(num):
            print(num)

# Запитуємо числа у користувача
a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
print_primes(a, b)
