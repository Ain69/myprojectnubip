import csv
import random
from faker import Faker

# Инициализация Faker с украинской локализацией
fake = Faker('uk_UA')

# Словари для генерации по батькові
male_middle_names = [
    "Олександрович", "Іванович", "Сергійович", "Петрович", "Михайлович",
    "Андрійович", "Володимирович", "Дмитрович", "Максимович", "Євгенович",
    "Васильович", "Григорійович", "Юрійович", "Олегович", "Ігорович",
    "Борисович", "Арсенович", "Романович", "Анатолійович", "Семенович"
]

female_middle_names = [
    "Олександрівна", "Іванівна", "Сергіївна", "Петрівна", "Михайлівна",
    "Андріївна", "Володимирівна", "Дмитрівна", "Максимівна", "Євгенівна",
    "Василівна", "Григорівна", "Юріївна", "Олегівна", "Ігорівна",
    "Борисівна", "Арсенівна", "Романівна", "Анатоліївна", "Семенівна"
]

# Генерация одного записи
def generate_person(gender):
    if gender == "Чоловіча":
        first_name = fake.first_name_male()
        middle_name = random.choice(male_middle_names)
    else:
        first_name = fake.first_name_female()
        middle_name = random.choice(female_middle_names)
    
    last_name = fake.last_name()
    birth_date = fake.date_of_birth(minimum_age=16, maximum_age=85).strftime('%d-%m-%Y')
    position = fake.job()
    city = fake.city()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()

    return [last_name, first_name, middle_name, gender, birth_date, position, city, address, phone, email]

# Основная функция для записи в CSV
def write_to_csv(filename, num_records=2000):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Заголовки
        writer.writerow([
            "Прізвище", "Ім'я", "По батькові", "Стать", "Дата народження",
            "Посада", "Місто проживання", "Адреса проживання", "Телефон", "Email"
        ])
        
        # Генерация записей
        for _ in range(num_records):
            gender = "Чоловіча" if random.random() < 0.6 else "Жіноча"
            person = generate_person(gender)
            writer.writerow(person)

# Генерация файла
write_to_csv("people.csv")
print("Файл успішно створено!")
