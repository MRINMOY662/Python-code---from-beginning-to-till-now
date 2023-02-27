
#Practice for if else statement using time module
import time

timestamp=time.strftime('%H:%M:%S')
time=int(time.strftime('%H')) 
if time < 12: 
    print("Good Morning Sir🌄.")
elif time == 12: 
    print("How are you Sir🙂.") 
elif time <= 12: 
    print("Good afternoon Sir🏜.")
elif time <= 15: 
    print("Good evening Sir🌆")               
elif time >= 23: 
    print("It's time for bed sir, you need to wake up early in the morning 🌌.")
else: 
    print("Good Night Sir🌉.") 
print("Time:",timestamp)   