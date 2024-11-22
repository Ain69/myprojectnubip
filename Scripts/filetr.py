# filetr.py
from module2 import TransLate
import configparser

# Функція для читання конфігураційного файлу
def read_config():
    config = configparser.ConfigParser()
    config.read('config.txt')
    source_lang = config['DEFAULT']['source_lang']
    target_lang = config['DEFAULT']['target_lang']
    return source_lang, target_lang

# Функція для читання тексту з файлу
def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Функція для запису перекладеного тексту у файл
def write_translated_text_to_file(filename, translated_text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(translated_text)

# Основна функція
def main():
    # Читання конфігураційного файлу
    source_lang, target_lang = read_config()
    print(f"Перекладаємо з {source_lang} на {target_lang}")

    # Читання тексту з файлу
    input_text = read_text_from_file('input.txt')
    print(f"Текст для перекладу: {input_text}")

    # Переклад тексту
    translated_text = TransLate(input_text, source_lang, target_lang)
    print(f"Перекладений текст: {translated_text}")

    # Запис перекладеного тексту в новий файл
    write_translated_text_to_file('translated_text.txt', translated_text)
    print("Перекладений текст збережено у файлі 'translated_text.txt'.")

if __name__ == "__main__":
    main()
