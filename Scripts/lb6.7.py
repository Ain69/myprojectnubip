import matplotlib
matplotlib.use('Agg')  # Це вимикає використання графічних інтерфейсів (Tkinter)
import matplotlib.pyplot as plt
import numpy as np

# Масив
array = np.array([13, 0, -3, 73, 0, 0, 0, 0, 0, 0, 0, -7, 0, 49, 0, 0, 76, 13, -31, -59, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -12, 51, 0, 0, 0])

# Окремо виділяємо додатні, від'ємні та нульові елементи
positive = array[array > 0]
negative = array[array < 0]
zeros = array[array == 0]

# Сортуємо додатні елементи за зростанням, від'ємні - по спаданню
positive_sorted = np.sort(positive)
negative_sorted = np.sort(negative)[::-1]  # Відсортовуємо по спаданню

# Об'єднуємо результат
result_array = np.concatenate((positive_sorted, negative_sorted, zeros))

# Виводимо отриманий масив
print("Отриманий масив:")
print(result_array)

# Створюємо графік
plt.figure(figsize=(10, 6))
plt.scatter(range(len(result_array)), result_array, s=50, color='blue', alpha=0.7)

# Налаштування для осей і заголовка
plt.xlabel('Індекс елемента')
plt.ylabel('Значення елемента')
plt.title('Візуалізація перетвореного масиву')

# Зберігаємо графік у файл PNG
plt.savefig('transformed_array.png')

# Закриваємо графік, щоб не було відкритих вікон
plt.close()
