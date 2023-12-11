class Player:
    def __init__(self, name):
        self._name = name
        self._guessed_words = set()

    # сеттеры и геттеры

    def get_name(self):
        return self._name

    def get_guessed_words(self):
        return self._guessed_words

    def get_guessed_words_len(self):
        return len(self._guessed_words)

    def add_word(self, word):
        self._guessed_words.add(word.strip().lower())

    def word_used(self, word):
        '''
        Проверяет уникальность введенного слова.
        Возвращает True, если повторяется.
        :param word:
        :return:
        '''
        return word.strip().lower() in self._guessed_words

    def __repr__(self):
        return f"\nName: {self.get_name()}\nUsed words: {self.get_guessed_words()}, total: {self.get_guessed_words_len()}"
