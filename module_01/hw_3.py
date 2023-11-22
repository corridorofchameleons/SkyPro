correct_answers = 0
POINTS_PER_ANSWER = 10

questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

questions_number = len(questions)

# Начинаем тест с этого места
ready_or_not_statement = input('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать! ')

# Заходим в тест, если пользователь готов
if ready_or_not_statement.lower() != 'ready':
    print('Кажется, вы не хотите играть. Очень жаль')
else:
    for num, question in enumerate(questions):
        answer = input(questions[num] + ' ')
        if answer.lower() == answers[num]:
            print('Ответ верный!')
            correct_answers += 1
        else:
            print(f'Неправильно. Правильный ответ: {answers[num]}')

    # Считаем набранные баллы и процент правильных ответов
    score = correct_answers * POINTS_PER_ANSWER
    correct_answers_percentage = correct_answers / questions_number * 100

    # Выводим статистику
    print(f'\nВот и всё!'
          f'\nВы ответили на {correct_answers} вопросов из 3 верно.'
          f'\nВы заработали {score} баллов.'
          f'\nЭто {round(correct_answers_percentage)} процентов.')
