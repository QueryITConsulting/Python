##Computer game

##Answering of computer science related quiz
import datetime
from calendar import calendar, month
from calendar import year
today=datetime.day()
##month=calenda
print(today)
print("================Quiz 1================")
print()
score=0
playing=input("Do you want to play ? : ")
if playing.lower() !="yes":
    quit()
else:
    print("Let the Game begin::::")
    print()

answer=input("What does the initials CPU stand for : \n")
if answer.lower() == "central processing unit":
    print("Correct !")
    score=score+1
else:
    print("Incorrect")
    print()
    
answer=input("What does the initials RAM stand for : \n ")
if answer.lower() == "random access memory":
    print("Correct !")
    score=score+1
else:
    print("Incorrect")
    print()
    
    
answer=input("What does the initials IO stand for : \n ")
if answer.lower() == "input output":
    print("Correct !")
    score=score+1
else:
    print("Incorrect")
    print()
    
    
answer=input("What does the initials GPU stand for : \n")
if answer.lower() == "graphics processing unit":
    print("Correct !")
    score=score+1
else:
    print("Incorrect")
    print()
    
answer=input("What does the initials MEM stand for : \n")
if answer.lower() == "memory":
    print("Correct !")
    score=score+1
else:
    print("Incorrect")
    print()
    
print("===============End of the game=======================")  
print()
print()
print("Your scored  :  " + str(score)  + "   correctly")  
print()
print()
print("Your percentage score is : " + str((score/5)*100) )
print()
print()
        
        