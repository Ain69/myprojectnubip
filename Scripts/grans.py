# gtrans.py
from module1 import TransLate, LangDetect, CodeLang, LanguageList

def demo_translate():
    text = "Hello"
    src_lang = "en"
    dest_lang = "fr"
    result = TransLate(text, src_lang, dest_lang)
    print(f"Переклад з {src_lang} на {dest_lang}: {result}")

def demo_langdetect():
    text = "Bonjour"
    result = LangDetect(text)
    print(f"Визначена мова для '{text}': {result}")

def demo_codelang():
    lang = "English"
    result = CodeLang(lang)
    print(f"Код мови для '{lang}': {result}")

def demo_languagelist():
    text = "Hello"
    result = LanguageList("screen", text)
    print(f"Таблиця мов для '{text}': {result}")

def main():
    print("Демонстрація функцій з module1.py:")
    demo_translate()
    demo_langdetect()
    demo_codelang()
    demo_languagelist()

if __name__ == "__main__":
    main()
