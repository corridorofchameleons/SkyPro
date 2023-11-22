correct_answers = 0
score = 0

questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

# Начинаем тест с этого места
ready_or_not_statement = input('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать! ')

# Заходим в тест, если пользователь готов
if ready_or_not_statement.lower() != 'ready':
    print('Кажется, вы не хотите играть. Очень жаль')
else:

    for num, question in enumerate(questions):
        answer = input(f"\nВопрос {num + 1}: {questions[num]} ")    # Сразу забираем первый ответ
        attempts = 3    # осталось попыток

        # Цикл привязываем к попыткам, очки будут считаться обратно пропорционально
        for _ in range(attempts, 0, -1):

            # Если верно, то все хорошо, начисляем очки, переходим к следующему вопросу
            if answer.lower() == answers[num]:
                print('Ответ верный!')
                correct_answers += 1
                break

            # Если неверно
            else:
                # уменьшаем коэффициент
                attempts -= 1
                # Последняя попытка израсходована
                if attempts == 0:
                    print(f'Увы, но нет. Верный ответ: {answers[num]}')
                    break
                # Еще остается хотя бы одна попытка
                else:
                    print(f'Осталось попыток: {attempts}, попробуйте еще раз!')
                    answer = input()

        score += attempts * 10

    # Выводим статистику
    print(f'\nВот и всё!'
          f'\nВы ответили на {correct_answers} вопросов из 3 верно.'
          f'\nВы набрали {score} баллов.')
