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

# Якщо масив успішно зчитаний, вивести його на екран
if array is not None:
    print("Зчитаний масив з файлу:")
    print(array)
else:
    print("Масив не був зчитаний.")
