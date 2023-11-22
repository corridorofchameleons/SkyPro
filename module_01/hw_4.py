'''
1. В программе для доступа к значению словаря используется метод get() как более безопасный.
2. В программе ответы записываются иным способом, чем в задании. В любом случае их записывать
    во множества/списки - почему бы не сделать это на месте.

Таким образом,
- [v]  Словари созданы верно.
- [ ]  Перебор ключей словаря реализован.
- [v]  Перебор по ключу-значению реализован.
- [ ]  Динамическое создание словаря реализовано.
- [v]  Чтение из словаря по индексу (КЛЮЧУ, ВЕРОЯТНО) реализовано.
- [v]  Получение букв из строки реализовано.
- [v]  Изменение регистра реализовано.
- [v]  Получение ранга реализовано
'''

words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

words_polish = {
    'sklep': 'магазин',
    'księżyc': 'месяц',
    'wrócić': 'вернуться',
    'rower': 'велосипед',
    'chrząszcz': 'жук',
}

levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}

# правильные и неправильные ответы храним в списках
answers = {
    'correct': [],
    'incorrect': []
}

# получаем от пользователя уровень сложности и выбираем словарь, с которым будем работать
print('Выберите уровень сложности')
level = input('E - легкий, M - средний, H - сложный: ').lower()

match level:
    case 'e':
        chosen_dict = words_easy
        difficulty = 'легкий'
    case 'm':
        chosen_dict = words_medium
        difficulty = 'средний'
    case 'h':
        chosen_dict = words_hard
        difficulty = 'сложный'
    case _:
        print('Стоило играть по правилам...')
        chosen_dict = words_polish
        difficulty = 'польский'

# проходим по словарю, сохраняем результаты
print(f'Выбран уровень сложности {difficulty}, мы предложим 5 слов, подберите перевод.\n')
for k, v in chosen_dict.items():
    input('Нажмите Enter.')
    print(f'{k.title()}, {len(v)} букв, начинается на {v[0]}...')
    answer = input().lower()
    if answer == v:
        print(f'Верно, {k.title()} - это {v}')
        answers.get('correct').append(k)
    else:
        print(f'Неверно. {k.title()} - это {v}')
        answers.get('incorrect').append(k)
    # для пустой строки
    print()

# выводим статистику, предварительно сохранив количество правильных ответов
correct_answers_num = len(answers.get('correct'))

print('Правильно отвеченные слова:')
for word in answers.get('correct'):
    print(word)
print('\nНеправильно отвеченные слова:')
for word in answers.get('incorrect'):
    print(word)
print(f'\nВашг ранг:\n{levels.get(correct_answers_num)}')
