import requests

url = "http://ollama:11434/api/generate"

prompt = """Generate pytest unit tests for this Python code. Test the Question class, save_quiz, load_quiz, and run_quiz functions. Include edge cases.

import random
import json
import os

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
    def to_dict(self):
        return {"prompt": self.prompt, "answer": self.answer}
    @staticmethod
    def from_dict(data):
        return Question(data["prompt"], data["answer"])

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == question.answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question.answer}")
    print(f"Your final score is {score}/{len(questions)}")

def save_quiz(quiz_name, questions):
    quiz_data = [question.to_dict() for question in questions]
    with open(f"{quiz_name}.json", "w") as file:
        json.dump(quiz_data, file)

def load_quiz(quiz_name):
    if os.path.exists(f"{quiz_name}.json"):
        with open(f"{quiz_name}.json", "r") as file:
            quiz_data = json.load(file)
            return [Question.from_dict(data) for data in quiz_data]
    else:
        return []
"""

payload = {
    "model": "qwen2.5-coder:7b",
    "prompt": prompt,
    "stream": False
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    data = response.json()
    print(data["response"])
else:
    print("Error:", response.status_code, response.text)