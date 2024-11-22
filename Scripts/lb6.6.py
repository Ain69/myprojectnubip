import numpy as np

# Масив
array = np.array([13, 0, -3, 73, 0, 0, 0, 0, 0, 0, 0, -7, 0, 49, 0, 0, 76, 13, -31, -59, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -12, 51, 0, 0, 0])

# Знаходимо індекси першого і останнього нульового елемента
first_zero_index = np.argmax(array == 0)
last_zero_index = len(array) - 1 - np.argmax(np.flip(array) == 0)

# Вибираємо елементи між першим і останнім нульовими
elements_between_zeros = array[first_zero_index + 1:last_zero_index]

# Підраховуємо кількість елементів
count_between_zeros = len(elements_between_zeros)

# Обчислюємо суму елементів
sum_between_zeros = np.sum(elements_between_zeros)

# Виводимо результати
print(f"Кількість елементів між першим і останнім нулем: {count_between_zeros}")
print(f"Сума елементів між першим і останнім нулем: {sum_between_zeros}")
