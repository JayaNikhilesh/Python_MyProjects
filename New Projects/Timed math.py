import random
import time

OPERATORS = ["+","-","*"]

MIN = input("Enter minimum number you want: ")
MIN = int(MIN)
MAX = input("Enter maximum number you want: ")
MAX = int(MAX)
TOTAL  = input("Enter  number of questions you want: ")
TOTAL = int(TOTAL)

def generate():
    left = random.randint(MIN, MAX)
    right = random.randint(MIN, MAX)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press enter to start: ")
print("-------------------------")

start_time = time.time()

for i in range(TOTAL):
    expr, answer = generate()
    while True:
        guess = input("Problem #" + str(i + 1) + ":" + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("-----------------------------")
print("Nice work!\nYou finished in", total_time , "seconds!")