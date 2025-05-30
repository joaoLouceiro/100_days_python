from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item.get("text"), item.get("answer")))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Quiz finished")
print(f"Your final score is {quiz.score}/{quiz.question_num}")