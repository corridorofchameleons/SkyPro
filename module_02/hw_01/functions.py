from random import shuffle

# настройки программы
WORDS_FILENAME = 'words.txt'
RESULTS_FILENAME = 'results_fake_db.txt'

POINTS_PER_ANSWER = 10


def shuffle_word(word):
    '''
    Принимает слово, возвращает анаграмму
    :param word:
    :return:
    '''

    tmp_word = list(word)
    shuffle(tmp_word)
    return ''.join(tmp_word)


def read_words(filename=WORDS_FILENAME):
    '''
    Читает слова из файла, возвращает список слов
    :param filename:
    :return:
    '''

    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
            return lines
    except:
        print('Ошибка чтения файла')


def write_result(name, res, filename=RESULTS_FILENAME):
    '''
    Сохраняет результат
    :param filename:
    :param name:
    :param res:
    :return:
    '''

    try:
        with open(filename, 'a') as file:
                line = ':'.join([name, str(res)]) + '\n'
                file.writelines(line)
    except:
        print('Результат не удалось сохранить')


def read_results(filename=RESULTS_FILENAME):
    '''
    Читает результаты
    :param filename:
    :return:
    '''

    try:
        with open(filename, 'r') as file:
            if file:
                data = file.readlines()
                records = [int(rec.split(':')[1].strip()) for rec in data]

                # количество игр и рекорд
                games_num = len(records) if records else 0
                top_record = max(records) if records else 0

                return games_num, top_record
    except:
        print('Не удалось прочитать результаты')
