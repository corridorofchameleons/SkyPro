from random import shuffle

# данные для работы программы
morse_dict = {"0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
              "6": "-....", "7": "--...", "8": "---..", "9": "----.", "a": ".-", "b": "-...",
              "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
              "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
              "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
              "x": "-..-", "y": "-.--", "z": "--..", ".": ".-.-.-", ",": "--..--", "?": "..--..",
              "!": "-.-.--", "-": "-....-", "/": "-..-.", "@": ".--.-.", "(": "-.--.", ")": "-.--.-"}

word_list = ['nebula', 'scissors', 'lame', 'overdose', 'javascript']

# список ответов (до тех пор, пока нет верного ответа, ответ считается неверным)
answers = [False] * len(word_list)


def morse_encode(word: str) -> str:
    """
    Кодирует слово в точки и тире
    Возвращает преобразованное слово
    """

    encoded_symbols = []

    for letter in word:
        encoded_symbols.append(morse_dict.get(letter))

    return ' '.join(encoded_symbols)


def get_word() -> str:
    """
    Возвращает слово из списка и удаляет его
    Предварительно проверяет, что список не пустой
    """

    return word_list.pop() if word_list else None


def print_statistics() -> None:
    """
    Выводит статистику, полученную из БД (глобальной переменной)
    Общее количество вопросов функция получает именно из длины списка answers, так как
        к моменту вызова функции список word_list будет уже пуст
    """

    total = len(answers)
    correct = answers.count(True)
    incorrect = answers.count(False)

    print(f'Всего задачек: {total}\n'
          f'Отвечено верно: {correct}\n'
          f'Отвечено неверно: {incorrect}\n')


# В самом начале работы программа перемешивает слова
shuffle(word_list)

print('\nСегодня мы потренируемся расшифровывать морзянку.\nНажмите Enter и начнем')
input()

for i in range(len(word_list)):

    # получаем слово
    curr_word = get_word()

    # проверяет, что get_word() не вернул None (пустая строка допустима) и запускает раунд
    if curr_word is not None:
        word_encoded = morse_encode(curr_word)

        print(f'Слово {i + 1}: {word_encoded}')
        answer = input()

        if answer.lower() == curr_word:
            print(f'Верно, {curr_word.title()}!\n')
            answers[i] = True
        else:
            print(f'Неверно, {curr_word.title()}!\n')

    else:
        break

# получаем статистику
print_statistics()
