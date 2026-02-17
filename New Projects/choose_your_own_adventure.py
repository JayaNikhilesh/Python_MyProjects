name = input("Type your name: ")
print("Welcome to this adventure", name + "!")

answer = input("You are on a dirt road, it has come to an end. You can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river. would you like to swim or go on the bridge? ").lower()

    if answer == "swim":
        print("You were drown from river water")

    elif answer == "bridge":
        print("You went to other side safely")

    else:
        print("Invalid option")

elif answer == "right":

    answer = input("You come to a river. would you like to swim or go on the bridge? ").lower()

    if answer == "bridge".lower():
        print("The bridge you are going is collapsed and you died!")

    elif answer == "swim".lower():
        print("You went to other side safely")

else:
    print("Not a valid option!. You lose.")

print("Hope you enjoyed the game!")