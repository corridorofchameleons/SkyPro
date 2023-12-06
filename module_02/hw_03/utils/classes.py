class Question:

    def __init__(self, question, difficulty, answer):
        self._question = question
        self._answer = answer
        self._difficulty = difficulty
        self._correct = False
        self._user_answer = None
        self._score = self._difficulty * 10

    def get_question(self):
        return self._question

    def get_difficulty(self):
        return self._difficulty

    def get_points(self):
        return self._score

    def set_user_answer(self, user_answer):
        self._user_answer = user_answer

    def is_correct(self):
        return self._correct

    def build_question(self):
        return f"Question: {self._question}\nDifficulty: {self._difficulty}/5\n"

    def build_feedback(self):
        if self._user_answer.lower().strip() == self._answer.lower().strip():
            self._correct = True
            return f"Correct! You've earned {self._score} points\n"
        else:
            return f"Incorrect! The answer is {self._answer}\n"
