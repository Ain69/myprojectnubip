from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs
from langdetect.lang_detect_exception import LangDetectException

# Мапа підтримуваних мов
LANGUAGES = GoogleTranslator().get_supported_languages(as_dict=True)

def TransLate(text: str, scr: str = 'auto', dest: str = 'en') -> str:
    """Функція повертає текст перекладений на задану мову, або повідомлення про помилку."""
    try:
        if scr == 'auto':
            scr = detect(text)  # автоматичне визначення мови
        translated = GoogleTranslator(source=scr, target=dest).translate(text)
        return translated
    except Exception as e:
        return f"Помилка перекладу: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    """Функція визначає мову та коефіцієнт довіри для заданого тексту, або повертає повідомлення про помилку."""
    try:
        detections = detect_langs(text)
        primary_detection = detections[0]
        language = primary_detection.lang
        confidence = primary_detection.prob

        if set == "lang":
            return language
        elif set == "confidence":
            return str(confidence)
        elif set == "all":
            return f"Мова: {language}, Коефіцієнт довіри: {confidence}"
        else:
            return "Невірне значення параметра 'set'"
    except LangDetectException:
        return "Помилка визначення мови: текст занадто короткий або некоректний"
    except Exception as e:
        return f"Помилка визначення мови: {str(e)}"

def CodeLang(lang: str) -> str:
    """Функція повертає код мови або назву мови, або повідомлення про помилку."""
    try:
        if lang in LANGUAGES:
            return LANGUAGES[lang]
        elif lang in LANGUAGES.values():
            return list(LANGUAGES.keys())[list(LANGUAGES.values()).index(lang)]
        else:
            return "Помилка: Мова не знайдена"
    except Exception as e:
        return f"Помилка: {str(e)}"

def LanguageList(out: str = "screen", text: str = None) -> str:
    """Виводить таблицю всіх мов та їх кодів, а також текст, перекладений на кожну мову."""
    try:
        output = "Код мови | Мова"
        if text:
            output += " | Переклад\n" + "-"*40
        else:
            output += "\n" + "-"*25

        translations = {}
        for code, language in LANGUAGES.items():
            row = f"{code} | {language}"
            if text:
                translated_text = TransLate(text, dest=code)
                row += f" | {translated_text}"
            output += "\n" + row

        if out == "screen":
            print(output)
        elif out == "file":
            with open("language_list.txt", "w", encoding="utf-8") as file:
                file.write(output)
        else:
            return "Невірне значення параметра 'out'"

        return "Ok"
    except Exception as e:
        return f"Помилка: {str(e)}"
