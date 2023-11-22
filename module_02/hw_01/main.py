from functions import *


def main():

    # создаем счетчик очков
    result = 0

    # результаты игры
    games_num = 0
    record = 0

    # получает слова
    words = read_words()

    if words:

        username = input('Введите ваше имя:\n')

        for word in words:
            # визуально разделяет раунды
            print()

            shuffled_word = shuffle_word(word)
            answer = input(f'Угадайте слово: {shuffled_word}\n')

            if answer.strip().lower() == word:
                print(f'Верно, вы получаете {POINTS_PER_ANSWER} очков')
                result += POINTS_PER_ANSWER
            else:
                print(f'Неверно! Верный ответ – {word}')

        # сохраняет результат
        write_result(username, result)

        # получает статистику
        results = read_results()

        if results:
            games_num, record = read_results()

        # выводит статистику
        print()
        print(f'Всего игр сыграно: {games_num}')
        print(f'Лучший результат: {record}')

    else:
        print('Игра аварийно завершилась')


if __name__ == '__main__':
    main()
