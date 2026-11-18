# Практикум Цифровой кафедры
# Вторая самостоятельная версия: журнал абитуриента МЖ-МИЭП
# Темы вопросов — культурология и зарубежная литература

from datetime import date
from random import choice, sample, shuffle


GROUPS = ["МО", "МЭО", "МП", "МЖ", "МИЭП", "ФУП", "ФФЭ", "ФЛМК", "МБ", "ИМТУР"]

PHRASES = {
    "en": "Welcome back, {person}. Your student file is open.",
    "it": "Bentornata, {person}. Il fascicolo e pronto.",
    "es": "Hola de nuevo, {person}. El expediente ya esta abierto.",
    "zh": "{person}，档案已经打开。",
    "ar": "اهلا بعودتك يا {person}. الملف جاهز.",
    "pl": "Witaj ponownie, {person}. Teczka studencka jest otwarta.",
}

NAMES = {
    "en": "английский",
    "it": "итальянский",
    "es": "испанский",
    "zh": "китайский",
    "ar": "арабский",
    "pl": "польский",
}

CARDS = [
    ("культура", "смысловое пространство, которое человек создаёт поверх биологии"),
    ("хронотоп", "связка художественного времени и пространства у Бахтина"),
    ("полифония", "несколько самостоятельных голосов внутри одного романа"),
    ("орософия", "у Вяземского это Гора, Путь и меняющийся Восходитель"),
    ("просвещение", "эпоха критики предрассудков: от 1688 года до революции 1789 года"),
    ("романтизм", "эстетика, где в центре личность, чувство и разрыв с порядком"),
]


def ask(label):
    return input(label).strip()


def student_age(raw_year):
    this_year = date.today().year
    born = this_year - 18 if raw_year == "" else int(raw_year)
    return born, this_year - born


def captcha():
    base = choice(range(11, 30))
    extra = choice(range(4, 15))
    reply = ask(f"Чтобы продолжить, посчитайте {base} + {extra}: ")
    good = reply == str(base + extra)
    print("Можно идти дальше." if good else f"Ответ был {base + extra}.")
    return good


def language_block(person):
    print("Доступные коды:", " ".join(sorted(PHRASES)))
    code = ask("Код языка, который вы учите: ").lower()
    if code not in PHRASES:
        print("Такого кода нет. Беру английский.")
        code = "en"
    print(PHRASES[code].format(person=person))
    heard = ask("Узнали язык? напишите да или нет: ").lower()
    return code, heard.startswith("д")


def programming_check():
    reply = ask("Практикум идёт на языке: ").lower()
    success = reply in {"python", "питон", "пайтон"}
    print("Верно, Python." if success else "Для этой работы нужен Python.")
    return success


def literature_quiz():
    term, meaning = choice(CARDS)
    pool = [term]
    pool.extend(sample([name for name, _ in CARDS if name != term], 3))
    shuffle(pool)
    print("\nЧто это за понятие?")
    print(meaning)
    for index, option in enumerate(pool, 1):
        print(f"[{index}] {option}")
    reply = ask("Ваш номер: ")
    if reply.isdigit() and pool[int(reply) - 1] == term:
        print("Есть попадание.")
        return True
    print("Нужный вариант:", term)
    return False


def blank_sentence():
    original = (
        "Нора уходит из кукольного дома, потому что хочет быть человеком, "
        "а не ролью, которую ей назначила семья."
    )
    long_words = [piece.strip(".,") for piece in original.split() if len(piece.strip(".,")) > 6]
    hidden = choice(long_words)
    masked = original.replace(hidden, "______", 1)
    print("\n" + masked)
    reply = ask("Какое слово стёрто? ")
    ok = reply.lower() == hidden.lower()
    print("Совпало." if ok else f"В тексте было «{hidden}».")
    return ok


def bonus_room():
    reply = ask("Последний вопрос: номер комнаты Цифровой кафедры? ")
    if reply.lower() in {"3053", "одинцово"}:
        print("Засчитано.")
        return 1
    print("Не засчитано. Можно посмотреть dd.mgimo.ru")
    return 0


print("ЖУРНАЛ АБИТУРИЕНТА")
print("МГИМО, программа МЖ-МИЭП\n")

given = ask("Как вас зовут? ")
family = ask("Ваша фамилия? ")
print("Список факультетов:", ", ".join(GROUPS))
group = ask("Факультет из списка: ")
born, age = student_age(ask("Год рождения: "))

print(f"\nЗаписали: {given} {family}")
print(f"Группа/факультет: {group}")
print(f"Сейчас вам {age}, год рождения {born}")

marks = [captcha()]
lang, lang_ok = language_block(given)
marks.append(lang_ok)
marks.append(programming_check())
marks.append(literature_quiz())
marks.append(blank_sentence())
marks.append(bonus_room() == 1)

got = sum(marks)
print("\nИтог журнала")
print(f"{family} {given} | {group} | язык: {NAMES[lang]}")
print(f"Отметок «верно»: {got} из {len(marks)}")
