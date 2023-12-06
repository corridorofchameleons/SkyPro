import json

from utils.classes import Question  # проблемы пайчарма с импортом

FILE_PATH = 'data/questions.json'


def read_file(file=FILE_PATH):
    '''
    Reads json from a file.
    Returns a list of question objects
    :param file:
    :return:
    '''

    with open(file) as j:
        data = json.load(j)
    return [Question(question['q'], question['d'], question['a']) for question in data]


def calculate_score(list_: list[Question]) -> tuple[int, int, int]:
    '''
    Calculates score
    :param list_:
    :return:
    '''

    score = 0
    correct = 0
    total = len(list_)

    for q in list_:
        if q.is_correct():
            score += q.get_points()
            correct += 1

    return correct, total, score
