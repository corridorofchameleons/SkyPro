import random

from utils.functions import read_file, calculate_score


def main():

    questions = read_file()
    random.shuffle(questions)

    for i, question in enumerate(questions, 1):

        print(f'Question {i}: {question.get_question()}')
        print(f'Difficulty: {question.get_difficulty()}/5')

        question.set_user_answer(input())
        print(question.build_feedback())

    correct, total, score = calculate_score(questions)
    print(f'That\'s it!\n'
          f'Answered {correct} out of {total}\n'
          f'Score: {score}')


if __name__ == '__main__':
    main()
