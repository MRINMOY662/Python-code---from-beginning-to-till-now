import sys

intro = '''
Welcome To Sasta KBC Quize
'''

questions_list = [
  "Name the highest mountain in the world.",
  "How many letters are there in the English alphabet?",
  "How many weeks are there in a calendar year?",
  "Which is the fastest land animal on earth?",
  "How many fingers are there in a human body’s single hand?"
]

a_random_answers_list = [
  "Mount Manaslu", "26 letters", "52", "Deer", "10 (Ten)"
]
b_random_answers_list = [
  "Mount K2", "18 letters", "24", "Cheetah", "5 (Five)"
]
c_random_answers_list = [
  "Mount Kangchenjunga", "20 letters", "48", "Lion", "12 (Twelve)"
]
d_random_answers_list = [
  "Mount Everest", "30 letters", "40", "Tiger", "15 (Fifteen)"
]

def start_game():
    input("Press Enter to start the game: ")

def play_game():
    start_game()
    question_no = 1
    start_up = 0
    prize_money = 0
    x = len(questions_list)

    while x > 0:
        print(f"\nQuestion {question_no}:")
        print(f"For Rs.{prize_money+1000}")
        print(f"{questions_list[start_up]}")
        print(f''' 
        A. {a_random_answers_list[start_up]}    B. {b_random_answers_list[start_up]}
        C. {c_random_answers_list[start_up]}    D. {d_random_answers_list[start_up]}
              ''')
        user_answer = input("Enter your answer (A/B/C/D) or type 'exit' to quit: ").lower()

        if user_answer == "exit":
            print("Thanks for playing!")
            sys.exit()

        elif user_answer == "d" and d_random_answers_list[start_up] == "Mount Everest":
            print("Correct answer!")
            prize_money += 1000
            start_up += 1
            question_no += 1
        elif user_answer == "a" and a_random_answers_list[start_up] == "26 letters":
            print("Correct answer!")
            prize_money += 1000
            start_up += 1
            question_no += 1
        elif user_answer == "a" and a_random_answers_list[start_up] == "52":
            print("Correct answer!")
            prize_money += 1000
            start_up += 1
            question_no += 1
        elif user_answer == "b" and b_random_answers_list[start_up] == "Cheetah":
            print("Correct answer!")
            prize_money += 1000
            start_up += 1
            question_no += 1
        elif user_answer == "b" and b_random_answers_list[start_up] == "5 (Five)":
            print("Correct answer!")
            prize_money += 1000
            start_up += 1
            question_no += 1
        else:
            print("Wrong answer :( Please try again!")
        
    print("Congratulations! You have won the game and a prize of Rs.", prize_money)

    return

play_game()
