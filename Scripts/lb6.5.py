import numpy as np

# Масив
array = np.array([13, 0, -3, 73, 0, 0, 0, 0, 0, 0, 0, -7, 0, 49, 0, 0, 76, 13, -31, -59, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -12, 51, 0, 0, 0])

# Знаходимо елементи з парними значеннями
even_elements = array[array % 2 == 0]

# Підрахуємо кількість парних елементів
even_count = len(even_elements)

# Обчислюємо добуток парних елементів
even_product = np.prod(even_elements)

# Виводимо результати
print(f"Кількість парних елементів: {even_count}")
print(f"Добуток парних елементів: {even_product}")
