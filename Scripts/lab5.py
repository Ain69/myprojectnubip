import string

def sort_words(words):
    """
    Сортує слова за алфавітом: спочатку українські, потім англійські.
    """
    # Визначаємо алфавіти
    ukrainian_alphabet = "абвгґдеєжзийіїклмнопрстуфхцчшщьюя"
    english_alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Розподіляємо слова за мовами
    ukrainian = sorted([word for word in words if word[0].lower() in ukrainian_alphabet])
    english = sorted([word for word in words if word[0].lower() in english_alphabet])

    # Об'єднуємо списки
    return ukrainian + english

def main():
    try:
        # Відкриваємо файл
        with open("text.txt", "r", encoding="utf-8") as file:
            text = file.read()

        # Виділяємо перше речення
        sentences = text.split(".")
        if len(sentences) == 0:
            print("Файл не містить речень.")
            return

        first_sentence = sentences[0].strip()
        print(f"Перше речення:\n{first_sentence}\n")

        # Видаляємо знаки пунктуації та розбиваємо текст на слова
        words = first_sentence.translate(str.maketrans("", "", string.punctuation)).split()
        words = [word.strip() for word in words if word]

        # Сортуємо слова
        sorted_words = sort_words(words)

        # Виводимо результати
        print("Відсортовані слова (українські спочатку, потім англійські):")
        print("\n".join(sorted_words))
        print(f"\nКількість слів: {len(sorted_words)}")

    except FileNotFoundError:
        print("Помилка: Файл 'text.txt' не знайдено.")
    except Exception as e:
        print(f"Помилка під час обробки файлу: {e}")

if __name__ == "__main__":
    main()
