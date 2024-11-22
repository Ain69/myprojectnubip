import numpy as np

def generate_array():
    # Генерація масиву з 36 елементів
    size = 36
    array = np.zeros(size, dtype=int)
    
    # Визначення кількості нульових елементів (від 30% до 50%)
    num_zeros = np.random.randint(size // 3, size // 2)  # Виправлено діапазон
    
    # Визначення кількості парних елементів (не більше 20%)
    num_even = np.random.randint(0, size // 5)
    
    # Заповнюємо масив нулями
    array[:num_zeros] = 0
    
    # Заповнюємо парними елементами
    even_numbers = np.random.randint(-99, 100, num_even)
    even_numbers = even_numbers[even_numbers % 2 == 0]  # фільтруємо лише парні
    array[num_zeros:num_zeros+len(even_numbers)] = even_numbers
    
    # Перевіримо скільки місць залишилось в масиві для непарних елементів
    remaining_size = size - num_zeros - len(even_numbers)
    
    # Заповнюємо інші елементи випадковими непарними числами, що не є нулями
    non_zero_non_even = np.random.randint(-99, 100, remaining_size)
    non_zero_non_even = non_zero_non_even[non_zero_non_even % 2 != 0]  # фільтруємо лише непарні
    array[num_zeros+len(even_numbers):num_zeros+len(even_numbers)+len(non_zero_non_even)] = non_zero_non_even
    
    # Перемішуємо масив для випадковості
    np.random.shuffle(array)
    
    return array

# Генерація масиву
array = generate_array()

print("Згенерований масив:")
print(array)

# Перевірки
print(f"Кількість нульових елементів: {np.count_nonzero(array == 0)}")
print(f"Кількість парних елементів: {np.count_nonzero(array % 2 == 0)}")
print(f"Кількість непарних елементів: {np.count_nonzero(array % 2 != 0)}")
