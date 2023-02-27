import sys

intro = "Welcome To Sasta KBC Quize by mrinmoy"

questions_list = [
  "What does 'OCR' stands for?",
  "Which one of the following is the standard protocol of internet?",
  "Which one of the following is the weakest force?",
  "Which is the largest moon in the solar system?",
  "Which fundamental particle is termed as 'Ghost' particle?"
]

a_random_answers_list = [
  "Optical CPU Recognition", "HTML", "Gravitational force", "Ganymede", "Gluons"
]
b_random_answers_list = [
  "Optimal Character Rendering", "Java", "Electromagnetic force", "Titan", "Neutrino"
]
c_random_answers_list = [
  "Other Character Restoration", "Flash", "Strong-nuclear force", "Phobos", "Higgs-Boson"
]
d_random_answers_list = [
  "Optical Character Recognition", "TCP/IP", "Weak-nuclear force", "Callisto", "Muon"
]

def main():
    end = "Thanks for playing! 😎"
    wrong = "Wrong answer, Try again :("
    print(intro)
    question_no = 1
    money = 1000
    x = len(questions_list)
    while x > 0:
        start_up = input("Press any key to start or 0 to exit: ")
        if start_up == "0":
            print(end)
            sys.exit()
        print(f"Your First question for Rs.{money}")
        print(f"{question_no}.> {questions_list[-(question_no)]}")
        print(f'''
  a. {a_random_answers_list[-(question_no)]}       b. {b_random_answers_list[-(question_no)]}
  c. {c_random_answers_list[-(question_no)]}      d. {d_random_answers_list[-(question_no)]}
  ''')
        var = input("Enter your answer (A/B/C/D) or type 'exit' to quit: ").lower()
        if var == "b" and b_random_answers_list[-(question_no)] == "Neutrino":
            print(f"Correct answer :) , you've got Rs.{money}")
            question_no += 1
            money += 1000
            x -= 1
        elif var == "a" and a_random_answers_list[-(question_no)] == "Ganymede":
            print(f"Correct answer :) , you've got Rs.{money}")
            question_no += 1
            money += 1000
            x -= 1
        elif var == "a" and a_random_answers_list[-(question_no)] == "Gravitational force":
            print(f"Correct answer :) , you've got Rs.{money}")
            question_no += 1
            money += 1000
        elif var == "d" and d_random_answers_list[-(question_no)] == "TCP/IP": 
            print(f"Correct answer :) , you've got Rs.{money}")
            question_no += 1
            money += 1000
            x -= 1              
        elif var == "d" and d_random_answers_list[-(question_no)] == "Optical Character Recognition": 
            print(f"Correct answer :)")
            x -= 1
            print(f"Congrats You're the winner of this game \nYour total money worth Rs. {money}")
            break  
        elif var == "exit":
            print("end")
            break
        else: 
            print(wrong)
    else:
      print(end) 
main()    