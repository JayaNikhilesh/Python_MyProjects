print("Welcome to my Quiz!")
score = 0

playing = input("do you want to play(yes/no)? " )

if playing.lower() != "yes":
    print("Let me know if you want to play later...")
    quit()

print("Lets play Quiz now...")

answer= input("what is CPU stands for: ")

if answer.lower() == "central processing unit":
    print(" Awesome Correct Answer")
    score += 1
else:
    print("Your answer is incorrect")

answer= input("what is GPU stands for: ")
if answer.lower() == "graphical processing unit":
    print(" Awesome Correct Answer")
    score += 1
else:
    print("Your answer is incorrect")

answer= input("what is CM stands for: ")
if answer.lower() == "cheif minister":
    print(" Awesome Correct Answer")
    score += 1
else:
    print("Your answer is incorrect")

answer= input("what is PM stands for: ")
if answer.lower() == "prime minister":
    print(" Awesome Correct Answer")
    score += 1
else:
    print("Your answer is incorrect")

answer= input("what is capital of India: ")
if answer.lower() == "delhi":
    print(" Awesome Correct Answer")
    score += 1
else:
    print("Your answer is incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/5)*100) + "%.")