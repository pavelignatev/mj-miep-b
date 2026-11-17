import datetime
import random
import re
import time

print("=" * 45)
print("   ЭЛЕКТРОННЫЙ ДЕКАНАТ МГИМО")
print("   Версия Б · МЖ-МИЭП")
print("=" * 45)

name = input(" Введи твое имя: ")
surname = input("   Твоя фамилия: ")
departments = ["МО", "МЭО", "МП", "МЖ", "МИЭП", "ФУП", "ФФЭ", "ФЛМК", "МБ", "ИМТУР"]
print("Доступные факультеты:", ", ".join(departments))
faculty = input(" Твой факультет: ")
birth_year = input("   Год рождения: ")
current_year = datetime.date.today().year
if not birth_year:
    birth_year = current_year - 17
else:
    birth_year = int(birth_year)
age = current_year - birth_year

print()
print("Проверяем данные...")
time.sleep(1)
print()
print(f"Вас зовут: {name} {surname}")
print("Факультет:", faculty)
print("  Возраст:", age)

a = random.randint(2, 6)
b = random.randint(2, 6)
print()
captcha = input(f"Подтверди, что ты человек, введи сумму {a}+{b}: ")
answer = a + b
if int(captcha) == answer:
    print("Капча пройдена")
    is_human = True
else:
    print("Неправильный ответ, должно быть", answer)
    is_human = False

greetings = {
    "en": "Clear thinking beats complex panic, {name}.",
    "de": "Guten Tag, {name} {surname}! MGIMO Digital Department.",
    "it": "Ciao {name}! Benvenuta al corso.",
    "fr": "Salut {name} {surname}! On reparare le doyenat.",
    "es": "Hola {name}! Practica y git ayudan.",
    "ar": "مرحبا {name}! أهلا بك في المقرر.",
}
languages = {
    "en": "английский",
    "de": "немецкий",
    "it": "итальянский",
    "fr": "французский",
    "es": "испанский",
    "ar": "арабский",
}

lang = input("""
Какой иностранный язык ты изучаешь?
Введи двухбуквенный код (en, de, it, fr, es, ar): """).strip().lower()
if lang not in greetings:
    print("Такого кода нет, переходим на английский.")
    lang = "en"
shown = lang
print("\nПриветствие:\n")
print(greetings[shown].format(name=name, surname=surname))
print()
detect = input(f"Это был {languages[lang]} язык? (д)а/(н)ет): ").strip().lower()
language_ok = detect.startswith("д")
if language_ok:
    print("Верно определили язык.")
else:
    print(f"На самом деле это был {languages[shown]}.")

results = [language_ok]
print()
answer = input("Какой язык программирования ты изучаешь? ").strip()
if answer.lower() in {"python", "питон", "пайтон"}:
    print("Верно!")
    results.append(True)
else:
    print("На практикуме ожидается Python.")
    results.append(False)
print()

terms_dict = {
    "переменная": "ячейка памяти, в которой хранится значение.",
    "интерпретатор": "программа, которая выполняет исходный код построчно.",
    "строка": "текст в кавычках.",
    "список": "упорядоченная коллекция значений.",
    "словарь": "структура данных, из которой по ключу получают значение.",
    "цикл": "повтор блока команд в зависимости от условий.",
    "комментарий": "текст после #, который не влияет на ход программы.",
    "функция": "блок кода, который принимает аргументы и возвращает результат.",
    "актор": "участник международных отношений, способный влиять на события.",
    "многосторонность": "взаимодействие через международные организации и режимы.",
    "национальный интерес": "приоритеты государства во внешней политике.",
    "просвещение": "эпоха разума, критики предрассудков и образовательной утопии.",
    "романтизм": "направление, где центр — личность, чувство и свобода.",
    "орософия": "подход Вяземского: Гора, Путь и Восходитель.",
}


def ask_for_term(terms_dict, term=None, n_options=3):
    if term is None:
        term = random.choice(list(terms_dict.keys()))
    other_terms = [t for t in terms_dict if t != term]
    k = min(n_options, len(terms_dict)) - 1
    options = [term] + random.sample(other_terms, k)
    random.shuffle(options)
    print(terms_dict[term].capitalize())
    print("Это определение для термина: ")
    for i, option in enumerate(options, start=1):
        print(f"  {i}. {option}")
    while True:
        answer = input("Ваш ответ: ")
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            break
        print("Введите номер варианта.")
    if term == options[int(answer) - 1]:
        print("Верно!")
        return True
    print("Неверно. Правильный ответ:", term)
    return False


for _ in range(2):
    results.append(ask_for_term(terms_dict))


def get_words(s):
    parts = re.split(r"(\W+)", s)
    words = [(i, p) for i, p in enumerate(parts) if p.isalpha() and len(p) > 3]
    ix, random_word = random.choice(words)
    return parts[:ix], random_word, parts[ix + 1 :]


message = """
Культура и политика пересекаются: образы, язык и память общества влияют
на то, как государства объясняют свои цели и как аудитория их воспринимает.
"""

start, word, end = get_words(message)
print("".join(start + ["_" * len(word)] + end))
answer = input("Какое слово пропущено? ")
if answer.lower() == word.lower():
    print("Ответ верный")
    results.append(True)
else:
    print(f"Неверно. Правильный ответ: {word}")
    results.append(False)

print("\n" + "=" * 45)
print("ИТОГ · МЖ-МИЭП · вариант Б")
print(f"Имя и фамилия: {name} {surname}")
print(f"Факультет: {faculty}")
print(f"Год рождения: {birth_year}, возраст: {age}")
print(f"Иностранный язык: {languages[lang]}")
total = len(results)
correct = sum(results)
print(f"Ответов на вопросы: {total}, из них верно {correct}.")
print("=" * 45)

bonus = input("Бонус: номер комнаты Цифровой кафедры? ").strip()
if bonus in {"3053", "Одинцово", "одинцово"}:
    correct += 1
    print("+1 балл")
else:
    print("Подсказка: dd.mgimo.ru")
print(f"Итого баллов: {correct}")
