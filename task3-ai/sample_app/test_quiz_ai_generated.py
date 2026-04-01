"""
AI-Generated Tests from Qwen2.5-Coder 7B
Generated via Ollama API with the following prompt:
"Generate pytest unit tests for this Python code. Test the Question class,
save_quiz, load_quiz, and run_quiz functions. Include edge cases."

NOTE: These tests contain several issues as documented in reflections.txt:
- Placeholder import ("from your_module import ...")
- Missing os import
- run_quiz tests incorrectly assume SystemExit
- No input mocking for run_quiz
- Edge cases mentioned but not implemented
"""
import pytest
from your_module import Question, run_quiz, save_quiz, load_quiz  # Replace 'your_module' with the actual module name

# Test cases for Question class
def test_question_to_dict():
    question = Question("What is the capital of France?", "Paris")
    assert question.to_dict() == {"prompt": "What is the capital of France?", "answer": "Paris"}

def test_question_from_dict():
    data = {"prompt": "What is the capital of France?", "answer": "Paris"}
    question = Question.from_dict(data)
    assert isinstance(question, Question)
    assert question.prompt == "What is the capital of France?"
    assert question.answer == "Paris"

# Test cases for save_quiz and load_quiz functions
def test_save_load_quiz():
    questions = [
        Question("What is 2 + 2?", "4"),
        Question("Who wrote 'To Kill a Mockingbird'?", "Harper Lee")
    ]
    quiz_name = "test_quiz"
    save_quiz(quiz_name, questions)
    loaded_questions = load_quiz(quiz_name)
    os.remove(f"{quiz_name}.json")  # Clean up the file after test
    assert len(loaded_questions) == len(questions)
    for q1, q2 in zip(questions, loaded_questions):
        assert q1.prompt == q2.prompt
        assert q1.answer == q2.answer

# Test cases for run_quiz function
def test_run_quiz():
    questions = [
        Question("What is 2 + 2?", "4"),
        Question("Who wrote 'To Kill a Mockingbird'?", "Harper Lee")
    ]
    with pytest.raises(SystemExit) as exc_info:
        run_quiz(questions)
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 0

def test_run_quiz_with_wrong_answers():
    questions = [
        Question("What is 2 + 2?", "5"),
        Question("Who wrote 'To Kill a Mockingbird'?", "Harper Lee")
    ]
    with pytest.raises(SystemExit) as exc_info:
        run_quiz(questions)
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 0

def test_run_quiz_with_no_questions():
    questions = []
    with pytest.raises(SystemExit) as exc_info:
        run_quiz(questions)
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 0

# Run the tests
if __name__ == "__main__":
    pytest.main()