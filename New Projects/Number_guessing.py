import random

top = input("Type a number you want max in number guessing: ")

if top.isdigit():
    top = int(top)

    if top <= 0:
        print("Please enter a larger number than 0: ")
        quit()

else:
    print("Please enter a number next time!")
    quit()

r = random.randrange(0, top)

x = 0

while True:
    x += 1
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please enter a number next time!")
        continue

    if guess == r:
        print("You guessed correct number")
        break
    elif guess > r:
        print("You guessed larger number")
    else:
        print("You guessed smaller number")
print(x)