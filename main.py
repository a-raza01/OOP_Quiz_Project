from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_ans = Question(question["question"], question["correct_answer"])
    question_bank.append(question_ans)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


