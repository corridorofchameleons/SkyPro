class BasicWord:
    def __init__(self, word, words):
        self._word = word
        self._subwords = set(words)  # множество выбрано для скорости

    # геттеры

    def get_word(self):
        return self._word

    def get_subwords(self):
        return self._subwords

    def get_words_len(self):
        return len(self._subwords)

    def in_list(self, user_word):
        '''
        Проверяет вхождение введенного слова в список ответов.
        Возвращает True, если найдено.
        :param user_word:
        :return:
        '''
        return user_word.strip().lower() in self._subwords

    def __repr__(self):
        return f"\nWord: {self.get_word()}\nSubwords: {self.get_subwords()}, total: {self.get_words_len()}\n"
