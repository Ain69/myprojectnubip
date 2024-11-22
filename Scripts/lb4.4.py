import pandas as pd
from datetime import datetime
import os
import matplotlib.pyplot as plt

def calculate_age(birthdate):
    """Розрахунок віку за датою народження"""
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

def analyze_csv_file(csv_filename):
    try:
        # Перевірка наявності CSV файлу
        if not os.path.exists(csv_filename):
            print("Помилка: CSV файл не знайдено!")
            return

        # Завантаження даних
        data = pd.read_csv(csv_filename, encoding='utf-8')
        data['Дата народження'] = pd.to_datetime(data['Дата народження'], format='%d-%m-%Y')
        data['Вік'] = data['Дата народження'].apply(calculate_age)
        print("Ok, файл CSV успішно відкрито.")
        
        # Рахуємо кількість співробітників чоловічої та жіночої статі
        gender_counts = data['Стать'].value_counts()
        print("\nКількість співробітників за статтю:")
        print(gender_counts)
        
        # Будуємо діаграму за статтю
        gender_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['skyblue', 'pink'])
        plt.title("Розподіл співробітників за статтю")
        plt.ylabel("")  # Прибираємо підпис осі
        plt.show()
        
        # Категоризація за віковими групами
        younger_18 = data[data['Вік'] < 18]
        age_18_45 = data[(data['Вік'] >= 18) & (data['Вік'] <= 45)]
        age_45_70 = data[(data['Вік'] > 45) & (data['Вік'] <= 70)]
        older_70 = data[data['Вік'] > 70]

        age_groups = {
            "younger_18": younger_18,
            "18-45": age_18_45,
            "45-70": age_45_70,
            "older_70": older_70
        }

        # Рахуємо кількість співробітників у кожній віковій групі
        print("\nКількість співробітників за віковими групами:")
        age_group_counts = {key: len(group) for key, group in age_groups.items()}
        for group, count in age_group_counts.items():
            print(f"{group}: {count}")

        # Будуємо діаграму за віковими групами
        plt.bar(age_group_counts.keys(), age_group_counts.values(), color='orange')
        plt.title("Кількість співробітників за віковими групами")
        plt.xlabel("Вікові групи")
        plt.ylabel("Кількість співробітників")
        plt.show()

        # Рахуємо кількість співробітників кожної статі у кожній віковій категорії
        print("\nКількість співробітників за віковими групами та статтю:")
        gender_age_group_counts = {
            key: group['Стать'].value_counts() for key, group in age_groups.items()
        }
        for group, counts in gender_age_group_counts.items():
            print(f"{group}:")
            print(counts)

            # Будуємо діаграму
            counts.plot(kind='bar', color=['skyblue', 'pink'], rot=0)
            plt.title(f"Розподіл за статтю у віковій групі {group}")
            plt.xlabel("Стать")
            plt.ylabel("Кількість співробітників")
            plt.show()

    except FileNotFoundError:
        print("Помилка: Неможливо відкрити файл CSV.")
    except Exception as e:
        print(f"Помилка: Сталася помилка під час аналізу файлу. Деталі: {e}")

# Назва CSV файлу
csv_filename = "people.csv"  # Заміна на ім'я вашого CSV файлу

# Виклик функції
analyze_csv_file(csv_filename)
