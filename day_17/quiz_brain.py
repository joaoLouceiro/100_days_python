class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_num]
        u_ans = input(f"Q.{self.question_num + 1}: {current_question.question} T or F? ")
        self.question_num += 1
        self.check_answer(current_question, u_ans)

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def check_answer(self, question, answer):
        answer = "True" if answer.lower() == 't' else "False"
        if question.answer == answer:
            print("Right")
            self.score += 1
        else:
            print("Wrong")
        print(f"Your score is: {self.score}/{self.question_num}")
