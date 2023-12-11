import requests
import random

from utils_02.basic_word import BasicWord
from settings import LINK


def load_random_word(link=LINK):
    '''
    Получает json по ссылке, выбирает случайное слово,
    возвращает экземпляр BasicWord
    :param link:
    :return:
    '''
    data = requests.get(link)
    words = [(d['word'], d['subwords']) for d in data.json()]
    word = words[random.randint(0, len(words) - 1)]
    basic_word = BasicWord(*word)
    return basic_word
