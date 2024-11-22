import pandas as pd
from datetime import datetime
import os

def calculate_age(birthdate):
    """Розрахунок віку за датою народження"""
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

def categorize_by_age(data):
    """Категоризація співробітників за віковими групами"""
    data['Вік'] = data['Дата народження'].apply(calculate_age)
    
    younger_18 = data[data['Вік'] < 18]
    age_18_45 = data[(data['Вік'] >= 18) & (data['Вік'] <= 45)]
    age_45_70 = data[(data['Вік'] > 45) & (data['Вік'] <= 70)]
    older_70 = data[data['Вік'] > 70]
    
    return younger_18, age_18_45, age_45_70, older_70

def create_xlsx_from_csv(csv_filename, xlsx_filename):
    try:
        # Перевірка наявності CSV файлу
        if not os.path.exists(csv_filename):
            print("Помилка: CSV файл не знайдено!")
            return
        
        # Завантаження даних з CSV
        data = pd.read_csv(csv_filename, encoding='utf-8')
        data['Дата народження'] = pd.to_datetime(data['Дата народження'], format='%d-%m-%Y')
        
        # Категоризація за віком
        younger_18, age_18_45, age_45_70, older_70 = categorize_by_age(data)
        
        # Створення Excel файлу з аркушами
        with pd.ExcelWriter(xlsx_filename, engine='openpyxl') as writer:
            data.to_excel(writer, sheet_name="all", index=False)
            younger_18.to_excel(writer, sheet_name="younger_18", index=False)
            age_18_45.to_excel(writer, sheet_name="18-45", index=False)
            age_45_70.to_excel(writer, sheet_name="45-70", index=False)
            older_70.to_excel(writer, sheet_name="older_70", index=False)
        
        print("Ok, програма завершила свою роботу успішно.")
    except FileNotFoundError:
        print("Помилка: Неможливо відкрити файл CSV.")
    except Exception as e:
        print(f"Помилка: Неможливо створити XLSX файл. Деталі: {e}")

# Назви файлів
csv_filename = "people.csv"  # Заміна на ім'я вашого CSV файлу
xlsx_filename = "categorized_data.xlsx"

# Виклик функції
create_xlsx_from_csv(csv_filename, xlsx_filename)
