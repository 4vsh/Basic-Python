import random

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 0

    for key in questions:
        print("+------------------------------------------------------------------------------------+")
        print(key)

        for i in all_answers[question_num]:
            print(i)

        user_guess = input("Enter your answer here: ").lower()
        guesses.append(user_guess)

        correct_guesses += check_answer(questions[key].lower(), user_guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(correct_ans, user_guess):
    if correct_ans == user_guess:
        print("Congratulations! You got it right.")
        return 1
    else:
        print("Oops! Better luck next time.")
        return 0


def display_score(correct_guesses, guesses):
    print("+----------------+")
    print("Results:")
    print("+----------------+")

    print("Correct Answers: ", end="")
    for key in questions:
        print(questions[key], end=" ")

    print("\nYour Answers: ", end="")
    for guess in guesses:
        print(guess, end=" ")

    score = int((correct_guesses / len(questions)) * 100)
    print(f"\nYour total score is: {score}%")


def play_again():
    while True:
        pagain = input("Want to play again? (yes or no): ").lower()
        if pagain in ["yes", "no"]:
            return pagain == "yes"
        else:
            print("Please enter 'yes' or 'no'.")


#---------------------
questions = {
    "Who created Python programming language?": "A",
    "What is the height of Mount Everest from sea level?": "C",
    "Where is Mount Everest located?": "B",
    "Which of the following is the farthest human-made object from Earth?": "B",
    "What is the full form of IP?": "D"
}

all_answers = [
    ["A. Guido Van Rossum", "B. Mark Zuckerberg", "C. Elon Musk", "D. Aavash Aryal"],
    ["A. 8848m", "B. 8848km", "C. 8848.86m", "D. 8848.46m"],
    ["A. Japan", "B. Nepal", "C. Mongolia", "D. India"],
    ["A. Kepler-102al7", "B. Voyager 1", "C. Hubble Telescope", "D. James Webb Telescope"],
    ["A. Intranet Protocol", "B. Internal Protocol", "C. InterNetwork Protocol", "D. Internet Protocol"]
]

new_game()

while play_again():
    new_game()

print("Thanks for playing! Made with love by Aavash :)")
