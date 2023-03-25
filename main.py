from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests
import html
import ui


response  = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")

response=response.json()

question_bank=[]
for question in response["results"]:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui=ui.UI(quiz)




