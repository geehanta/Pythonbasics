from Question import Question
question1 = "What color are apples?\n  (a)Red/Green (b)Purple (c)Orange \n\n",
question2 = "What color are Bananas?\n  (a)Teal (b)Magenta (c)Yellow\n\n",
question3 = "What color are Strawberries?\n (a)Yellow (b)Red  (c)Blue\n\n"
question4 = "What color are onions?\n (a)Purple (b) Green (c) Violet\n\n"
questions = [
    Question(question1, "a"),
    Question(question2, "c"),
    Question(question3, "b"),
    Question(question4, "a" or "c")
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(questions)
        if answer == question.answer:
            score += 1
    print("You got " +str(score) + "/" + str(len(questions)) + "correct!!")

run_test(questions)