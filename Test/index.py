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
        start_up = int(input("Press any key to start or 0 to exit: "))
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
        if var == "b" and b_random_answers_list[4] == "Neutrino": # It would cause TypeError
            print(f"Correct answer :) , you've got Rs.{money}")
            question_no += 1
            money += 1000
            # x = x - 1
        elif var == "a" and a_random_answers_list[3] == "Ganymede": 
            print(f"Correct answer :) , you've got Rs.{money}")
            question_no += 1
            money += 1000
        elif var == "a" and a_random_answers_list[2] == "Gravitational force": 
            print(f"Correct answer :) , you've got Rs.{money}")
            question_no += 1
            money += 1000
        elif var == "d" and d_random_answers_list[1] == "TCP/IP": 
            print(f"Correct answer :) , you've got Rs.{money}")
            question_no += 1
            money += 1000
            # x = x - 1                   
        elif var == "d" and d_random_answers_list[0] == "Optical Character Recognition": 
            print(f"Correct answer :)")
            # x = x - 1
            print(f"Congrats You're the winner of this game \nYour total money worth Rs. {money}")
            break  
        elif var == "exit":
            print("end")
            break
        else: 
            print(wrong)
          # x = x - 1
    else:
      print(end) 

main()    
    #The errors in the code:

#The only issue with previous code was that you were comparing a string to an integer, which would raise a TypeError. By converting question_no to an integer, as you did in the updated code, you resolved this issue and your code now works as expected.

#In Python, a TypeError occurs when an operation or function is applied to an object of an inappropriate type. In your code, the TypeError occurred because the input() function always returns a string, and you cannot compare a string to an integer using the > operator.

#Here's what happened in your code:

#Initially, question_no was an integer, initialized to 1.
# When you used the input() function to get user input, the value entered by the user was always a string.
# You tried to compare the user input (a string) to question_no (an integer) using the > operator, which caused the TypeError.
# To fix this issue, you need to convert the user input from a string to an integer before you can compare it to question_no. You can do this using the int() function, like this:

# user_input = input("Enter your answer (1-4) or type 'exit' to quit: ")
# if user_input == "exit":
#     print("Goodbye!")
#     sys.exit()
# else:
#     user_answer = int(user_input)
#     if user_answer > question_no:
        # do something
    # else:
        # do something else
        
#By converting the user input to an integer using int(), you can compare it to the integer value of question_no using the > operator without causing a TypeError.
