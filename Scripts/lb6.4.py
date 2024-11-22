import matplotlib
matplotlib.use('Agg')  # Забезпечує роботу без графічного інтерфейсу
import matplotlib.pyplot as plt
import numpy as np

# Файл, з якого будемо зчитувати масив
filename = 'generated_array.txt'

def read_array_from_file(filename):
    try:
        # Читання масиву з текстового файлу
        array = np.loadtxt(filename, dtype=int)
        return array
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return None

# Зчитування масиву з файлу
array = read_array_from_file(filename)

# Якщо масив успішно зчитаний
if array is not None:
    # Отримуємо індекси парних та нульових елементів
    even_indices = np.where(array % 2 == 0)[0]  # Парні елементи
    zero_indices = np.where(array == 0)[0]      # Нульові елементи

    # Створюємо точкову діаграму
    plt.figure(figsize=(10, 6))
    
    # Відображаємо всі елементи масиву як точки
    plt.scatter(range(len(array)), array, s=50, color='blue', label='Інші елементи', alpha=0.7)
    
    # Відображаємо парні елементи червоним кольором
    plt.scatter(even_indices, array[even_indices], s=100, color='red', label='Парні елементи', edgecolors='black', alpha=0.9)
    
    # Відображаємо нульові елементи зеленим кольором
    plt.scatter(zero_indices, array[zero_indices], s=100, color='green', label='Нульові елементи', edgecolors='black', alpha=0.9)

    # Додаємо значення на діаграму для парних елементів
    for i in even_indices:
        plt.text(i, array[i] + 1, str(array[i]), color='red', ha='center', fontsize=12)

    # Налаштування для осей і легенди
    plt.xlabel('Індекс елемента')
    plt.ylabel('Значення елемента')
    plt.title('Візуалізація масиву з виділенням парних і нульових елементів')
    plt.legend()

    # Зберігаємо графік у файл
    plt.savefig('array_visualization.png')  # Можна також зберегти у форматі .pdf, .svg тощо
    print("Графік збережено у файл 'array_visualization.png'.")

else:
    print("Масив не був зчитаний.")
