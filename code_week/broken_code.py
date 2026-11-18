import datetime
import random

print("*" * 42)
print(" Деканат МГИМО восстановлен")
print(" МЖ-МИЭП · проект про культуру и тексты")
print("*" * 42)

# Раньше программа стирала введённые ФИО и факультет. Теперь оставляет как есть.
first_name = input("Имя: ")
last_name = input("Фамилия: ")
faculties = ["МО", "МЭО", "МП", "МЖ", "МИЭП", "ФУП", "ФФЭ", "ФЛМК", "МБ", "ИМТУР"]
print("Можно выбрать:", " | ".join(faculties))
faculty = input("Факультет: ")

raw_year = input("Год рождения: ").strip()
today = datetime.date.today().year
birth_year = today - 19 if raw_year == "" else int(raw_year)
# Раньше возраст считался по длине имени. Теперь по году.
age = today - birth_year

print(f"\nАнкета: {first_name} {last_name}")
print(f"Факультет {faculty}, {age} лет")

# Капча: раньше int() стоял вокруг сравнения и всегда ломал проверку
x = random.randint(4, 12)
y = random.randint(1, 7)
typed = input(f"Сколько будет {x} + {y}? ")
human_ok = int(typed) == x + y
print("Капча принята." if human_ok else f"Нужно было {x + y}.")

# Свои языки: португальский и корейский
greetings = {
    "en": "Hello, {first_name}. Your record is saved.",
    "fr": "Bonjour, {first_name}. Le dossier est ouvert.",
    "zh": "{first_name}，档案已经保存。",
    "pt": "Ola, {first_name} {last_name}! Bem-vinda ao MGIMO.",
    "ko": "{first_name}님, MGIMO에 오신 것을 환영합니다.",
}
language_names = {
    "en": "английский",
    "fr": "французский",
    "zh": "китайский",
    "pt": "португальский",
    "ko": "корейский",
}

code = input("Код языка: en, fr, zh, pt, ko: ").strip().lower()
if code not in greetings:
    print("Код неизвестен, беру английский.")
    code = "en"
# Раньше приветствие бралось случайным языком
print(greetings[code].format(first_name=first_name, last_name=last_name))
heard = input(f"Это {language_names[code]}? да или нет: ").strip().lower()
language_point = heard.startswith("д")
if not language_point:
    print("На экране был", language_names[code])

score = int(language_point)
studied = input("Язык этого практикума: ").strip().lower()
if studied in {"python", "питон", "пайтон"}:
    print("Да.")
    score += 1
else:
    print("Сейчас работаем на Python.")

# Свой словарь предметной области. Определения совпадают с терминами.
glossary = {
    "культура": "смысловое пространство, созданное человеком, а не только этикет.",
    "хронотоп": "единство времени и пространства в художественном тексте.",
    "полифония": "несколько равноправных голосов в одном произведении.",
    "орософия": "образ культуры у Вяземского: Гора, Путь и Восходитель.",
    "просвещение": "эпоха разума между Славной революцией и 1789 годом.",
    "романтизм": "направление, где центр — личность, чувство и свобода.",
}


def quiz(glossary):
    term = random.choice(list(glossary))
    basket = [term] + random.sample([item for item in glossary if item != term], 2)
    random.shuffle(basket)
    print("\nОпределение:", glossary[term])
    for number, option in enumerate(basket, start=1):
        print(number, option)
    pick = input("Номер: ")
    if pick.isdigit() and basket[int(pick) - 1] == term:
        print("Совпало.")
        return 1
    print("Правильно было:", term)
    return 0


score += quiz(glossary)
score += quiz(glossary)

article = (
    "Культура начинается там, где человек создаёт память, "
    "образы и нормы, а не остаётся только биологическим существом."
)
candidates = [word.strip(".,") for word in article.split() if len(word.strip(".,")) > 5]
hidden = random.choice(candidates)
print("\n" + article.replace(hidden, "______", 1))
word = input("Какое слово пропущено? ")
if word.lower() == hidden.lower():
    print("Есть.")
    score += 1
else:
    print("В тексте стояло:", hidden)

print("\n" + "*" * 42)
print(f"{last_name} {first_name} | {faculty} | {birth_year} г.р.")
print("Язык анкеты:", language_names[code])
print("Баллы до бонуса:", score)
room = input("Комната Цифровой кафедры: ").strip().lower()
if room in {"3053", "одинцово"}:
    score += 1
    print("Бонус добавлен.")
else:
    print("Бонуса нет. Смотрите dd.mgimo.ru")
print("Финальный счёт деканата:", score)

# Отдельная игра по дополнительному заданию.
# В форме одно место для файла, поэтому она идёт следом в этом же .py
print("\nИгра: угадай год")
events = {
    "Славная революция в Англии": "1688",
    "Начало Великой французской революции": "1789",
    "Эссе Бахтина «Искусство и ответственность»": "1919",
    "Премьера «Кукольного дома» Ибсена": "1879",
}
hits = 0
for event in random.sample(list(events), 3):
    reply = input(f"Год события «{event}»: ").strip()
    if reply == events[event]:
        print("Верно.")
        hits += 1
    else:
        print("Нет, год:", events[event])
print(f"В игре {hits} из 3")
