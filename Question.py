#create class question
# this is a class to store answwer and prompt
class Question:
#every question has a prompt and an answer, accept and assign as shown below
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
