intro = '''
Welcome To KBC Quize
'''

questions_list = [
  "Name the highest mountain in the world.",
  "How many letters are there in the English alphabet?",
  "How many weeks are there in a calendar year?",
  "Which is the fastest land animal on earth?",
  "How many fingers are there in a human body’s single hand?"
]

a_random_answers_list = [
  "Mount Manaslu", "ans 26 letters", "7", "Deer", "10 (Ten)"
]
b_random_answers_list = [
  "Mount K2", "18 letters", "24", "ans Cheetah", "ans 5 (Five)"
]
c_random_answers_list = [
  "Mount Kangchenjunga", "10 letters", "ans 52", "Lion", "12 (Twelve)"
]
d_random_answers_list = [
  "ans Mount Everest", "30 letters", "40", "Tiger", "15 (Fifteen)"
]


def chack_write_anser(options, answer_list):
  if answer_list[options].find("ans") == 0:
    return answer_list[options][4:]
  else:
    return answer_list[options]


def main():
  print(intro)
  questions_no = 1
  x = len(questions_list)
  start_game = "to start the game, 0 to exit"
  money = 0
  while x > 0:
    start_game_options = input(f"Press {questions_no} {start_game}: ")
    if start_game_options == str(questions_no):
      print(f"Q {questions_no}.> {questions_list[x - 1]}")
      optine_ans = f'''
      A.> {chack_write_anser(x - 1, a_random_answers_list)}
      B.> {chack_write_anser(x - 1, b_random_answers_list)}
      C.> {chack_write_anser(x - 1, c_random_answers_list)}
      D.> {chack_write_anser(x - 1, d_random_answers_list)}
      '''
      user_ans = input(f'{optine_ans}\n >> ')

      if user_ans == "A" or user_ans == "a":
        if a_random_answers_list[x - 1].find("ans") == 0:
          money += 5
          print(f"Correct! You are the Won {money} Rs\n")
          questions_no += 1
          x = x - 1
        else:
          print("Wrong..! Try Again!\n")
          questions_no += 1
          x = x - 1
      elif user_ans == "B" or user_ans == "b":
        if b_random_answers_list[x - 1].find("ans") == 0:
          money += 5
          print(f"Correct! You are the won {money} Rs\n")
          questions_no += 1
          x = x - 1
        else:
          print("Wrong..! Try Again!\n")
          questions_no += 1
      elif user_ans == "C" or user_ans == "c":
        if c_random_answers_list[x - 1].find("ans") == 0:
          money += 5
          x = x - 1
          print(f"Correct! You are the won {money} Rs\n")
          questions_no += 1
          x = x - 1
        else:
          print("Wrong..! Try Again!\n")
          questions_no += 1
      elif user_ans == "D" or user_ans == "d":
        if d_random_answers_list[x - 1].find("ans") == 0:
          money += 5
          print(f"Correct! You are the won {money} Rs\n")
          questions_no += 1
          x = x - 1
        else:
          print("Wrong..! Try Again!\n")
          questions_no += 1
          x = x - 1
      else:
        print("Please Press Requried Options Key...!!\n")

    elif start_game_options == "0":
      print("Thank You Sir...!!")
      break

    else:
      print("Please Press Requried Options Key...!!\n")
    # print("Please enter your programming language: ")

    start_game = "to Next the Question, 0 to exit"


main()