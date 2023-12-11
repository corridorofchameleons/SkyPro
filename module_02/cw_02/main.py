from utils_02.functions import load_random_word
from utils_02.player import Player


def main():
    # загружает заранее, чтоб потом не висела
    word = load_random_word()

    username = input('Enter your name:\n')
    # создает экземпляр пользователя
    user = Player(username)
    print(f'Hello, {user.get_name()}\n')

    print(f'Compose {word.get_words_len()} words from {word.get_word().upper()}')
    print('Words must be at least 3 letters long')
    print('To finish the game guess all words or type "stop"')
    print('Let\'s go! Your first word:\n')

    # выходит из цикла, когда пользователь угадает все слова
    while user.get_guessed_words_len() < word.get_words_len():
        user_word = input()

        if user_word.strip().lower() in ['stop', 'стоп']:
            break

        # валидация
        if len(user_word) < 3:
            print('Too short')
        # ответ пользователя не найден в правильных ответах
        elif not word.in_list(user_word):
            print('Wrong!')
        # ответ пользователя повторяется
        elif user.word_used(user_word):
            print('Already used')
        # все проверки пройдены
        else:
            print('Correct')
            user.add_word(user_word)

        print()

    print(f"Game Over. You have guessed {user.get_guessed_words_len()} words")


if __name__ == '__main__':
    main()
