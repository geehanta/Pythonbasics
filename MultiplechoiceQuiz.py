from Question import Question
questionPrompts= [
    "What color are apples? \n  (a)Red/Green (b)Purple (c)Orange \n \n",
    "What color are Bananas? \n  (a)Teal (b)Magenta (c)Yellow \n \n",
    "What color are Strawberries? \n (a)Yellow (b)Red  (c)Blue \n \n"
]
questions = [
    Question(questionPrompts[0], "a"),
    Question(questionPrompts[1], "c"),
    Question(questionPrompts[2], "b")
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(questionPrompts[0])
        answer2 = input(questionPrompts[1])
        answer3 = input(questionPrompts[2])
        if answer == question.answer:
            score += 1
        elif answer2 == question.answer:
            score += 1
        elif answer3 == question.answer:
            score += 1
    print("You got " +str(score) + "/" + str(len(questions)) + "correct!!")

run_test(questions)